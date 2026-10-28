# Contributing to The Wallpaper Collection

Thanks for wanting to add to the museum. Three ground rules: **no subfolders**, **no duplicates**, and **no phone screenshots or social-media assets** in the annual folders.

## Folder layout — one level, always

Every shelf is a **single top-level folder that contains images directly**. No subfolders, not even "just this once".

```
The Wallpaper Collection/
├── 2026 Wallpaper/          ← images live here
│   ├── ferrari-296-gt-7680x2160.jpg
│   └── …
├── Phone Wallpapers/
│   └── …
└── README.md
```

**Why:** the macOS wallpaper pane only reads the folder you select — it does not recurse. A subfolder is invisible to it, and to Windows slideshow and most wallpaper tools. The same rule keeps `ls`, globs and archives simple.

- New work goes into an **existing shelf**.
- A genuinely new lane earns a **new top-level folder** — discussed in an Issue first.
- Never add `Foo/Bar/` to an existing shelf; flatten it.
- `python3 scripts/stats.py --check` fails if a subfolder appears, so a stale nesting is caught before merge.

## What belongs where

| Folder | Put here | Don't put here |
|--------|----------|----------------|
| `20xx Wallpaper/` | Desktop wallpaper art for that year | Phone wallpapers, avatars, logos, press kits |
| `Phone Wallpapers/` | Portrait mobile wallpapers (iPhone, Android, Artemis II, misc) | Desktop or ultrawide art |
| `Social Assets/` | Avatars, social banners, brand press kits | Anything you would actually set as a wallpaper |
| `Ultrawide Wallpapers/` | Anything ≥ 2.05:1 and ≥ 2560×1000 | 16:9 desktop art |
| Thematic vaults (`BugattiDestrier`, `Texture`, …) | Subject-specific sets | Random one-offs |

## Quality bar

- **Desktop wallpapers:** at least **1920 px on the long edge**; 2560 px+ preferred. Anything below 1080p needs a reason.
- **Phone wallpapers:** at least 1200 px on the long edge.
- No visible compression artifacts, no watermarks, no screenshot UI chrome.
- Prefer the **largest original** you have; don't upscale.

## Naming

```
<subject>-<width>x<height>.<ext>      e.g. ferrari-296-gt-3440x1440.jpg
```

- Lowercase file extensions (`.jpg`, `.webp`, `.png`).
- No trailing spaces before the extension.
- Keep photographer attribution when the source provides it (`*-unsplash.jpg`).
- When a sub-theme matters, put it **in the filename**, not in a folder (`Cyberpunk2077_Wallpapers_Arasaka_3840x2160_EN.webp`).
- Spaces are tolerated in legacy files, but new files should use hyphens.

## Formats

- **JPG** for photographic wallpapers (quality ≥ 90).
- **WebP** for flat/gradient/illustration art — the repo stores those as WebP q92; PNG is no longer used for new additions unless the image needs lossless alpha.
- **HEIC** only for Apple-native sets; add a note in the folder if Windows users need `scripts/heic2jpg.sh`.

## Before you open a PR

```bash
python3 scripts/stats.py          # does the collection still add up?
python3 scripts/stats.py --check  # README numbers + flat layout in sync?
```

- **No subfolders.** If a path looks like `Shelf/Sub/`, flatten it before opening the PR.
- Run a duplicate check: identical files are rejected (the same artwork in two years is not a feature).
- Keep the README numbers in sync — run `python3 scripts/stats.py --check` before opening a PR.
- One logical change per PR: new pack, reorganization, or docs — not all three.

## Rights

Only contribute images you have the right to redistribute. By opening a PR you confirm the file may be hosted publicly in this repository; the original rights holder keeps all rights to the artwork.
