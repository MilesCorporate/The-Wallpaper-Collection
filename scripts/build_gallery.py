#!/usr/bin/env python3
"""Build a local, browsable gallery.

Thumbnails and index.html are written to ./gallery/, which is gitignored:
the gallery is a local browsing aid, not part of the published archive.

    python3 scripts/build_gallery.py            # 420px thumbs, 10 workers
    python3 scripts/build_gallery.py --size 640
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
from concurrent.futures import ProcessPoolExecutor

from PIL import Image

Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "gallery")
THUMBS = os.path.join(OUT, "thumbs")
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif"}
SIZE = 420


def collect() -> list[str]:
    files = []
    for dp, dn, fs in os.walk(ROOT):
        dn[:] = [d for d in dn if not d.startswith(".") and d != "gallery"]
        for f in fs:
            if os.path.splitext(f)[1].lower() in IMAGE_EXT:
                files.append(os.path.relpath(os.path.join(dp, f), ROOT))
    return sorted(files)


def make_thumb(rel: str) -> dict | None:
    try:
        src = os.path.join(ROOT, rel)
        name = hashlib.md5(rel.encode()).hexdigest()[:16] + ".webp"
        dst = os.path.join(THUMBS, name)
        with Image.open(src) as im:
            w, h = im.size
            im.thumbnail((SIZE, SIZE), Image.LANCZOS)
            im.convert("RGB").save(dst, "WEBP", quality=80, method=4)
        return {"p": rel, "t": name, "w": w, "h": h, "f": rel.split(os.sep)[0]}
    except Exception:
        return None


HTML = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>The Wallpaper Collection — gallery</title>
<style>
  :root { color-scheme: dark; }
  body { margin: 0; background: #0d0d10; color: #e8e8ea; font: 14px/1.5 -apple-system, "SF Pro Text", system-ui, sans-serif; }
  header { position: sticky; top: 0; z-index: 5; display: flex; gap: 12px; align-items: center;
           padding: 12px 18px; background: rgba(13,13,16,.88); backdrop-filter: blur(12px);
           border-bottom: 1px solid #232329; flex-wrap: wrap; }
  h1 { font-size: 15px; margin: 0 12px 0 0; font-weight: 600; letter-spacing: .02em; }
  input, select { background: #17171c; color: #e8e8ea; border: 1px solid #2c2c34; border-radius: 8px;
                  padding: 7px 10px; font-size: 13px; outline: none; }
  input { width: 240px; } input:focus { border-color: #5b5bd6; }
  #count { color: #8a8a94; margin-left: auto; font-variant-numeric: tabular-nums; }
  main { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px; padding: 14px 18px 60px; }
  figure { margin: 0; background: #15151a; border-radius: 10px; overflow: hidden; position: relative; }
  img { width: 100%; aspect-ratio: 4/3; object-fit: cover; display: block; background: #0b0b0e; }
  figcaption { padding: 6px 9px 8px; font-size: 11px; color: #9a9aa4; white-space: nowrap;
               overflow: hidden; text-overflow: ellipsis; }
  figcaption b { color: #d6d6dc; font-weight: 500; }
  @media (prefers-color-scheme: light) {
    :root { color-scheme: light; } body { background: #f6f6f8; color: #1c1c1f; }
    header { background: rgba(246,246,248,.9); border-color: #e2e2e8; }
    input, select { background: #fff; color: #1c1c1f; border-color: #d8d8e0; }
    figure { background: #fff; } figcaption { color: #6b6b76; } figcaption b { color: #2a2a30; }
  }
</style>
</head>
<body>
<header>
  <h1>The Wallpaper Collection</h1>
  <input id="q" placeholder="搜索文件名…" autofocus>
  <select id="f"><option value="">全部分类</option></select>
  <select id="o">
    <option value="name">按名称</option>
    <option value="size">按分辨率</option>
    <option value="folder">按分类</option>
  </select>
  <span id="count"></span>
</header>
<main id="grid"></main>
<script>
const DATA = __DATA__;
const grid = document.getElementById('grid');
const q = document.getElementById('q'), f = document.getElementById('f'), o = document.getElementById('o');
const count = document.getElementById('count');
const folders = [...new Set(DATA.map(d => d.f))].sort();
for (const name of folders) { const el = document.createElement('option'); el.value = el.textContent = name; f.appendChild(el); }

function render() {
  const term = q.value.trim().toLowerCase();
  const folder = f.value;
  let rows = DATA.filter(d => (!folder || d.f === folder) && (!term || d.p.toLowerCase().includes(term)));
  if (o.value === 'size') rows.sort((a, b) => b.w * b.h - a.w * a.h);
  else if (o.value === 'folder') rows.sort((a, b) => a.f.localeCompare(b.f) || a.p.localeCompare(b.p));
  else rows.sort((a, b) => a.p.localeCompare(b.p));
  const frag = document.createDocumentFragment();
  for (const d of rows.slice(0, 600)) {
    const fig = document.createElement('figure');
    const img = document.createElement('img');
    img.loading = 'lazy'; img.src = 'thumbs/' + d.t; img.alt = d.p; img.title = d.p;
    const cap = document.createElement('figcaption');
    cap.innerHTML = '<b>' + d.f + '</b> · ' + d.p.split('/').slice(1).join('/');
    fig.append(img, cap); frag.appendChild(fig);
  }
  grid.replaceChildren(frag);
  count.textContent = rows.length + ' / ' + DATA.length;
}
q.addEventListener('input', render); f.addEventListener('change', render); o.addEventListener('change', render);
render();
</script>
</body>
</html>
"""


def main() -> None:
    global SIZE
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=SIZE)
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 4)
    args = ap.parse_args()
    SIZE = args.size

    os.makedirs(THUMBS, exist_ok=True)
    files = collect()
    print(f"{len(files)} images → {OUT}")
    rows = []
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        for i, r in enumerate(ex.map(make_thumb, files, chunksize=16), 1):
            if r:
                rows.append(r)
            if i % 250 == 0:
                print(f"  {i}/{len(files)}")
    page = HTML.replace("__DATA__", json.dumps(rows, ensure_ascii=False, separators=(",", ":")))
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"done: {len(rows)} thumbnails → gallery/index.html")


if __name__ == "__main__":
    main()
