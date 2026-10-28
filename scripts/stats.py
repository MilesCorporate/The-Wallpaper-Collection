#!/usr/bin/env python3
"""Collection statistics — the single source of truth for README numbers.

Usage:
    python3 scripts/stats.py            # human-readable table
    python3 scripts/stats.py --json     # machine-readable
    python3 scripts/stats.py --write    # sync the "By the numbers" tables in README.md
    python3 scripts/stats.py --check    # exit 1 if README is stale or a shelf has a subfolder
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif"}
VIDEO_EXT = {".mov", ".mp4", ".webm", ".mkv"}

# (key, regex with group1=prefix, group2=number, group3=suffix)
PATTERNS = [
    ("images", r"(\| \*\*Image files\*\* \| \*\*)([\d,]+)(\*\*)"),
    ("images", r"(\| \*\*图片数量\*\* \| \*\*)([\d,]+)(\*\*)"),
    ("videos", r"(\| \*\*Video files\*\* \| \*\*)([\d,]+)(\*\*)"),
    ("videos", r"(\| \*\*视频数量\*\* \| \*\*)([\d,]+)(\*\*)"),
    ("gib", r"(\| \*\*Working-tree media size\*\* \| \*\*~)([\d.]+)( GiB\*\*)"),
    ("gib", r"(\| \*\*工作区媒体容量\*\* \| \*\*约 )([\d.]+)( GiB\*\*)"),
    ("folders", r"(\| \*\*Top-level categories\*\* \| \*\*)(\d+)(\*\* folders)"),
    ("folders", r"(\| \*\*顶层分类\*\* \| \*\*)(\d+)(\*\* 个)"),
]


def scan() -> dict:
    folders = {}
    total_images = total_videos = total_bytes = 0
    for name in sorted(os.listdir(ROOT)):
        path = os.path.join(ROOT, name)
        if name.startswith(".") or name in {"gallery", "scripts"} or not os.path.isdir(path):
            continue
        images = videos = size = 0
        nested = []
        for dp, dn, fs in os.walk(path):
            dn[:] = [d for d in dn if not d.startswith(".")]
            if os.path.normpath(dp) != path:
                nested.append(os.path.relpath(dp, ROOT))
            for f in fs:
                ext = os.path.splitext(f)[1].lower()
                if ext in IMAGE_EXT:
                    images += 1
                elif ext in VIDEO_EXT:
                    videos += 1
                else:
                    continue
                size += os.path.getsize(os.path.join(dp, f))
        folders[name] = {"images": images, "videos": videos, "bytes": size, "nested": nested}
        total_images += images
        total_videos += videos
        total_bytes += size
    return {
        "folders": folders,
        "totals": {
            "folders": len(folders),
            "images": total_images,
            "videos": total_videos,
            "bytes": total_bytes,
            "gib": round(total_bytes / 1024**3, 2),
            "nested": sum(len(v["nested"]) for v in folders.values()),
        },
    }


def layout_problems(stats: dict) -> list[str]:
    """Every shelf must be flat: macOS wallpaper settings do not recurse."""
    return [p for v in stats["folders"].values() for p in v["nested"]]


def human(n: float) -> str:
    if n < 1024:
        return f"{n:.0f} B"
    for unit in ("KiB", "MiB", "GiB"):
        n /= 1024
        if n < 1024 or unit == "GiB":
            return f"{n:.1f} {unit}"
    return f"{n:.1f} GiB"


def print_table(stats: dict) -> None:
    rows = sorted(stats["folders"].items(), key=lambda kv: -kv[1]["bytes"])
    width = max(len(k) for k in stats["folders"]) + 2
    print(f"{'folder'.ljust(width)}{'images':>7}{'videos':>7}{'size':>12}")
    for name, v in rows:
        print(f"{name.ljust(width)}{v['images']:>7}{v['videos']:>7}{human(v['bytes']):>12}")
    t = stats["totals"]
    print("-" * (width + 26))
    print(f"{'TOTAL'.ljust(width)}{t['images']:>7}{t['videos']:>7}{human(t['bytes']):>12}")


def sync(readme: str, stats: dict, write: bool) -> list[str]:
    t = stats["totals"]
    want = {
        "images": f"{t['images']:,}",
        "videos": str(t["videos"]),
        "gib": f"{t['gib']:.1f}",
        "folders": str(t["folders"]),
    }
    problems: list[str] = []

    for key, pat in PATTERNS:
        def repl(m, key=key):
            cur = m.group(2)
            if cur != want[key]:
                problems.append(f"{key}: README says {cur}, actual {want[key]}")
                return m.group(1) + want[key] + m.group(3)
            return m.group(0)
        readme = re.sub(pat, repl, readme)

    if write and problems:
        with open(README, "w", encoding="utf-8") as fh:
            fh.write(readme)
    return sorted(set(problems))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    stats = scan()
    if args.json:
        print(json.dumps(stats, indent=2, ensure_ascii=False))
        return 0

    print_table(stats)
    nested = layout_problems(stats)
    if nested:
        print("\nLayout violation — shelves must be one level deep"
              " (the macOS wallpaper pane does not recurse):", file=sys.stderr)
        for p in nested:
            print("  -", p, file=sys.stderr)
    if args.write or args.check:
        with open(README, encoding="utf-8") as fh:
            readme = fh.read()
        problems = sync(readme, stats, args.write)
        if args.write:
            print(f"\nREADME updated ({len(problems)} value(s))." if problems else "\nREADME already up to date.")
        elif problems:
            print("\nREADME is stale:", file=sys.stderr)
            for p in problems:
                print("  -", p, file=sys.stderr)
            return 1
        else:
            print("\nREADME matches the working tree.")
        if args.check and nested:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
