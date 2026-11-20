#!/usr/bin/env python3
"""Perceptual near-duplicate scan.

Catches the duplicates SHA-256 cannot see: the same artwork at a different
resolution, re-encoded (JPEG <-> WebP), or very lightly re-cropped.

    python3 scripts/near_dupes.py                 # default tolerance
    python3 scripts/near_dupes.py --rmse 4        # stricter
    python3 scripts/near_dupes.py --json out.json

Method: every image is reduced to a 32x32 RGB thumbnail. Two images are
compared only when their aspect ratios are close, and then by RMS difference
of the thumbnails (0 = identical after scaling, ~30+ = unrelated). Thumbnails
are compared in both normal and horizontally flipped orientation, so a
mirrored re-export still matches.

Read-only. Needs Pillow + numpy (the bundled DSH runtime has both).
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp"}
SKIP_DIRS = {"gallery", "scripts"}
SIDE = 32
# rmse below this = "same artwork, different pixels"
DEFAULT_RMSE = 3.0
# aspect ratios must agree to within this factor before we even compare
RATIO_TOLERANCE = 0.03


def thumb(path: str) -> np.ndarray | None:
    """RGBA thumbnail, alpha composited over mid-grey.

    Alpha matters: white-on-transparent logo sets are pixel-identical in RGB
    once the alpha channel is dropped, and would otherwise all collide.
    """
    try:
        with Image.open(path) as im:
            has_alpha = im.mode in ("RGBA", "LA", "PA") or "transparency" in im.info
            im = im.convert("RGBA").resize((SIDE, SIDE), Image.LANCZOS)
            bg = Image.new("RGBA", (SIDE, SIDE), (128, 128, 128, 255))
            bg.alpha_composite(im)
            out = np.asarray(bg, dtype=np.float32)
            if has_alpha:
                return out
            # opaque image: flatten alpha so it contributes nothing to the score
            out[:, :, 3] = 0.0
            return out
    except Exception:
        return None


def collect() -> list[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames
                             if not d.startswith(".") and d not in SKIP_DIRS)
        for name in sorted(filenames):
            if os.path.splitext(name)[1].lower() in IMAGE_EXT:
                out.append(os.path.relpath(os.path.join(dirpath, name), ROOT))
    return out


def rgb_rmse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(np.mean((a[:, :, :3] - b[:, :, :3]) ** 2)))


def alpha_rmse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(np.mean((a[:, :, 3] - b[:, :, 3]) ** 2)))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rmse", type=float, default=DEFAULT_RMSE)
    ap.add_argument("--json")
    args = ap.parse_args()

    files = collect()
    print(f"thumbnailing {len(files)} images…", file=sys.stderr)
    entries = []
    for i, rel in enumerate(files, 1):
        t = thumb(os.path.join(ROOT, rel))
        if t is not None:
            entries.append({"path": rel, "thumb": t, "flip": np.ascontiguousarray(t[:, ::-1])})
        if i % 500 == 0:
            print(f"  {i}/{len(files)}", file=sys.stderr)

    # bucket by aspect ratio so we never brute-force the whole collection
    buckets: dict[float, list[dict]] = {}
    for e in entries:
        buckets.setdefault(round(float(np.log(e["thumb"].shape[1] / e["thumb"].shape[0])), 1), []).append(e)

    pairs = []
    keys = sorted(buckets)
    for gi, ka in enumerate(keys):
        group = list(buckets[ka])
        # neighbouring ratio buckets are close enough to be worth comparing
        for kb in keys[gi:]:
            if kb - ka > RATIO_TOLERANCE:
                break
            if kb != ka:
                group = group + buckets[kb]
        m = len(group)
        for i in range(m):
            a = group[i]
            for j in range(i + 1, m):
                b = group[j]
                if a["path"] == b["path"]:
                    continue
                d = rgb_rmse(a["thumb"], b["thumb"])
                f = rgb_rmse(a["thumb"], b["flip"])
                da, fa = alpha_rmse(a["thumb"], b["thumb"]), alpha_rmse(a["thumb"], b["flip"])
                best, best_alpha = (d, da) if d <= f else (f, fa)
                if best <= args.rmse and best_alpha <= args.rmse:
                    pairs.append({"rmse": round(best, 2), "alpha_rmse": round(best_alpha, 2),
                                  "mirrored": f < d, "a": a["path"], "b": b["path"]})
    pairs.sort(key=lambda p: p["rmse"])

    # union-find so a chain of re-exports collapses into one cluster
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for p in pairs:
        ra, rb = find(p["a"]), find(p["b"])
        if ra != rb:
            parent[ra] = rb
    groups: dict[str, list[str]] = {}
    for x in list(parent):
        groups.setdefault(find(x), []).append(x)
    clusters = sorted((sorted(v) for v in groups.values() if len(v) > 1),
                      key=len, reverse=True)

    cross = [c for c in clusters if len({p.split(os.sep)[0] for p in c}) > 1]
    print(f"\n== {len(pairs)} pair(s) at thumbnail RMSE ≤ {args.rmse}")
    print(f"== {len(clusters)} cluster(s) total, {len(cross)} of them span shelves\n")
    for c in clusters:
        shelves = sorted({p.split(os.sep)[0] for p in c})
        tag = "CROSS" if len(shelves) > 1 else "same "
        print(f"[{tag}] {len(c)} file(s)  {' · '.join(shelves)}")
        for p in c:
            print(f"         {p}")
        print()

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"pairs": pairs, "clusters": clusters,
                       "pair_count": len(pairs), "cluster_count": len(clusters)},
                      fh, indent=2, ensure_ascii=False)
        print(f"wrote {args.json}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
