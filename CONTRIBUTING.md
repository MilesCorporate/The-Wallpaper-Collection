# Contributing to The Wallpaper Collection

Thanks for wanting to add to the museum. Two ground rules: **no duplicates**, and **no phone screenshots or social-media assets** in the annual folders.

## What belongs where

| Folder | Put here | Don't put here |
|--------|----------|----------------|
| `20xx Wallpaper/` | Desktop wallpaper art for that year | Phone wallpapers, avatars, logos, press kits |
| `Phone Wallpapers/` | Portrait mobile wallpapers (`iOS/`, `Android/`, `NASA Artemis II/`, `Misc/`) | Desktop or ultrawide art |
| `Social Assets/` | Avatars, social banners, brand press kits | Anything you would actually set as a wallpaper |
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
- Spaces are tolerated in legacy files, but new files should use hyphens.

## Formats

- **JPG** for photographic wallpapers (quality ≥ 90).
- **WebP** for flat/gradient/illustration art — the repo stores those as WebP q92; PNG is no longer used for new additions unless the image needs lossless alpha.
- **HEIC** only for Apple-native sets; add a note in the folder if Windows users need `scripts/heic2jpg.sh`.

## Before you open a PR

```bash
python3 scripts/stats.py          # does the collection still add up?
python3 scripts/stats.py --check  # README numbers in sync?
```

- Run a duplicate check: identical files are rejected (the same artwork in two years is not a feature).
- Keep the README numbers in sync — run `python3 scripts/stats.py --check` before opening a PR.
- One logical change per PR: new pack, reorganization, or docs — not all three.

## Rights

Only contribute images you have the right to redistribute. By opening a PR you confirm the file may be hosted publicly in this repository; the original rights holder keeps all rights to the artwork.
