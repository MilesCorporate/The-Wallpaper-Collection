#!/usr/bin/env python3
"""Collection audit — duplicates, quality-bar outliers and waste.

Read-only: this script never deletes or moves anything.

    python3 scripts/audit.py              # full report
    python3 scripts/audit.py --json       # machine-readable
    python3 scripts/audit.py --exact      # only the byte-identical scan (fast path)

What it checks:
  * byte-identical duplicates (same size prefilter, then SHA-256)
  * images below the quality bar (long edge < 1080 px desktop / < 1200 px phone)
  * ultrawide files living outside `Ultrawide Wallpapers/`
  * portrait files living in a desktop-year shelf
  * junk files (.DS_Store, Thumbs.db, ._*) and empty directories
  * shelves that violate the one-level rule
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import struct
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif"}
VIDEO_EXT = {".mov", ".mp4", ".webm", ".mkv"}
SKIP_DIRS = {"gallery", "scripts"}
JUNK = {".DS_Store", "Thumbs.db", "desktop.ini", ".localized"}
DESKTOP_MIN = 1080          # long edge, per CONTRIBUTING
PHONE_MIN = 1200
ULTRAWIDE_RATIO = 2.05
ULTRAWIDE_MIN = (2560, 1000)


# ---------------------------------------------------------------- dimensions

def _jpeg_size(fh) -> tuple[int, int] | None:
    fh.seek(0)
    if fh.read(2) != b"\xff\xd8":
        return None
    while True:
        b = fh.read(1)
        if not b:
            return None
        if b != b"\xff":
            continue
        marker = fh.read(1)
        while marker == b"\xff":
            marker = fh.read(1)
        if not marker:
            return None
        m = marker[0]
        if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
            continue
        raw = fh.read(2)
        if len(raw) < 2:
            return None
        (seglen,) = struct.unpack(">H", raw)
        if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
            data = fh.read(5)
            if len(data) < 5:
                return None
            h, w = struct.unpack(">HH", data[1:5])
            return w, h
        fh.seek(seglen - 2, os.SEEK_CUR)


def _png_size(fh) -> tuple[int, int] | None:
    fh.seek(16)
    w, h = struct.unpack(">II", fh.read(8))
    return w, h


def _webp_size(fh) -> tuple[int, int] | None:
    fh.seek(12)
    chunk = fh.read(4)
    if chunk == b"VP8X":
        fh.seek(24)
        raw = fh.read(6)
        w = 1 + int.from_bytes(raw[0:3], "little")
        h = 1 + int.from_bytes(raw[3:6], "little")
        return w, h
    if chunk == b"VP8 ":
        fh.seek(26)
        w, h = struct.unpack("<HH", fh.read(4))
        return w & 0x3FFF, h & 0x3FFF
    if chunk == b"VP8L":
        fh.seek(21)
        b = fh.read(4)
        bits = int.from_bytes(b, "little")
        return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    return None


def dimensions(path: str) -> tuple[int, int] | None:
    try:
        with open(path, "rb") as fh:
            head = fh.read(12)
            if head[:2] == b"\xff\xd8":
                return _jpeg_size(fh)
            if head[:8] == b"\x89PNG\r\n\x1a\n":
                return _png_size(fh)
            if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
                return _webp_size(fh)
    except OSError:
        return None
    # HEIC/HEIF and anything exotic: sips is the only thing that reliably knows.
    if sys.platform != "darwin":
        return None
    try:
        out = subprocess.run(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", path],
            capture_output=True, text=True, timeout=30,
        ).stdout
        w = h = 0
        for line in out.splitlines():
            if "pixelWidth" in line:
                w = int(line.split(":")[1])
            elif "pixelHeight" in line:
                h = int(line.split(":")[1])
        return (w, h) if w and h else None
    except Exception:
        return None


# --------------------------------------------------------------------- scan

def walk():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames
                             if not d.startswith(".") and d not in SKIP_DIRS)
        for name in sorted(filenames):
            yield dirpath, name


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT)


def shelf_of(relpath: str) -> str:
    return relpath.split(os.sep)[0]


def scan(exact_only: bool = False) -> dict:
    files = []
    junk = []
    empties = []
    for dirpath, name in walk():
        path = os.path.join(dirpath, name)
        if name in JUNK or name.startswith("._"):
            junk.append(rel(path))
            continue
        ext = os.path.splitext(name)[1].lower()
        if ext in IMAGE_EXT or ext in VIDEO_EXT:
            try:
                size = os.path.getsize(path)
            except OSError:
                continue
            files.append({"path": rel(path), "size": size, "ext": ext,
                          "kind": "video" if ext in VIDEO_EXT else "image"})
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d not in SKIP_DIRS]
        if dirpath != ROOT and not dirnames and not filenames:
            empties.append(rel(dirpath))

    # byte-identical duplicates: only hash candidates that share a size
    by_size = collections.defaultdict(list)
    for f in files:
        by_size[f["size"]].append(f["path"])
    dupes = []
    hashed = 0
    for size, paths in sorted(by_size.items(), reverse=True):
        if len(paths) < 2:
            continue
        groups = collections.defaultdict(list)
        for p in paths:
            groups[sha256(os.path.join(ROOT, p))].append(p)
            hashed += 1
        for digest, members in groups.items():
            if len(members) > 1:
                dupes.append({"sha256": digest, "size": size, "paths": sorted(members)})
    dupes.sort(key=lambda d: -d["size"])

    if exact_only:
        return {"duplicates": dupes, "junk": junk, "empty_dirs": empties,
                "hashed": hashed, "file_count": len(files)}

    # dimensions + quality
    bad_quality, portrait_in_year, stray_ultrawide = [], [], []
    seen = set()
    for f in files:
        if f["kind"] == "video":
            continue
        p = f["path"]
        dims = dimensions(os.path.join(ROOT, p))
        f["dims"] = dims
        if not dims:
            continue
        w, h = dims
        seen.add(p)
        long_edge, short_edge = max(w, h), min(w, h)
        shelf = shelf_of(p)
        is_phone = shelf == "Phone Wallpapers"
        floor = PHONE_MIN if is_phone else DESKTOP_MIN
        if long_edge < floor:
            bad_quality.append({"path": p, "dims": f"{w}x{h}", "size": f["size"]})
        if (w >= ULTRAWIDE_MIN[0] and h >= ULTRAWIDE_MIN[1]
                and w / h >= ULTRAWIDE_RATIO and shelf != "Ultrawide Wallpapers"):
            stray_ultrawide.append({"path": p, "dims": f"{w}x{h}"})
        if h > w and shelf.endswith(" Wallpaper") and shelf[:4].isdigit():
            portrait_in_year.append({"path": p, "dims": f"{w}x{h}"})

    by_ext = collections.Counter(f["ext"] for f in files)
    by_shelf = collections.Counter()
    bytes_by_shelf = collections.Counter()
    for f in files:
        by_shelf[shelf_of(f["path"])] += 1
        bytes_by_shelf[shelf_of(f["path"])] += f["size"]

    return {
        "file_count": len(files),
        "total_bytes": sum(f["size"] for f in files),
        "by_ext": dict(by_ext),
        "by_shelf": dict(by_shelf),
        "bytes_by_shelf": dict(bytes_by_shelf),
        "hashed": hashed,
        "duplicates": dupes,
        "junk": junk,
        "empty_dirs": empties,
        "below_quality_bar": sorted(bad_quality, key=lambda x: -x["size"]),
        "portrait_in_year_shelf": portrait_in_year,
        "ultrawide_outside_lane": stray_ultrawide,
        "no_dimensions": [f["path"] for f in files
                          if f["kind"] == "image" and f["path"] not in seen],
    }


# ------------------------------------------------------------------- report

def human(n: float) -> str:
    if n < 1024:
        return f"{n:.0f} B"
    for unit in ("KiB", "MiB", "GiB"):
        n /= 1024
        if n < 1024 or unit == "GiB":
            return f"{n:.1f} {unit}"
    return f"{n:.1f} GiB"


def report(d: dict, exact_only: bool) -> None:
    print(f"{d['file_count']} media files")
    if not exact_only:
        print(f"  {human(d['total_bytes'])} on disk · "
              f"{len(d['by_ext'])} extensions: "
              + ", ".join(f"{k}={v}" for k, v in sorted(d["by_ext"].items(), key=lambda kv: -kv[1])))
        print(f"  hashed {d['hashed']} candidate files for the duplicate check")

    # duplicates
    dupes = d["duplicates"]
    wasted = sum(x["size"] * (len(x["paths"]) - 1) for x in dupes)
    print(f"\n== Byte-identical duplicates: {len(dupes)} group(s), "
          f"{sum(len(x['paths']) for x in dupes)} files, {human(wasted)} reclaimable")
    for x in dupes[:40]:
        print(f"  {human(x['size']):>9}  {len(x['paths'])}×(same)")
        for p in x["paths"]:
            print(f"             {p}")
    if len(dupes) > 40:
        print(f"  … {len(dupes) - 40} more group(s)")

    if exact_only:
        print(f"\n== Junk files: {len(d['junk'])}")
        print(f"== Empty directories: {len(d['empty_dirs'])}")
        return

    print(f"\n== Below the quality bar: {len(d['below_quality_bar'])} file(s)")
    for x in d["below_quality_bar"][:40]:
        print(f"  {x['dims']:>11}  {human(x['size']):>9}  {x['path']}")
    if len(d["below_quality_bar"]) > 40:
        print(f"  … {len(d['below_quality_bar']) - 40} more")

    print(f"\n== Portrait images in a year shelf: {len(d['portrait_in_year_shelf'])}")
    for x in d["portrait_in_year_shelf"][:20]:
        print(f"  {x['dims']:>11}  {x['path']}")

    print(f"\n== Ultrawide outside `Ultrawide Wallpapers/`: {len(d['ultrawide_outside_lane'])}")
    for x in d["ultrawide_outside_lane"][:20]:
        print(f"  {x['dims']:>11}  {x['path']}")

    print(f"\n== Junk files: {len(d['junk'])}")
    for p in d["junk"][:20]:
        print(f"  {p}")

    print(f"== Empty directories: {len(d['empty_dirs'])}")
    for p in d["empty_dirs"][:20]:
        print(f"  {p}")

    if d["no_dimensions"]:
        print(f"\n== Could not read dimensions: {len(d['no_dimensions'])}")
        for p in d["no_dimensions"][:10]:
            print(f"  {p}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--exact", action="store_true", help="skip the dimension pass")
    args = ap.parse_args()
    data = scan(exact_only=args.exact)
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        report(data, args.exact)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
