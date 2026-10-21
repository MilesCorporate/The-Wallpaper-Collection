# Migration guide — 2026-10-21

On **2026-10-21** this repository was rewritten and restructured. If you cloned or forked it before that date, read this first — a plain `git pull` will now fail with *"refusing to merge unrelated histories"*.

## What changed

| Change | Detail |
|---|---|
| **History rewritten** | All 131 old commits and 6 tags have new SHAs. The content is preserved; the object IDs are not. |
| **Repository shrank** | 8.9 GB → 5.7 GB (checkout 10.2 GiB → 5.8 GiB) |
| **PNG → WebP** | 703 PNGs re-encoded to WebP q92: `foo.png` → `foo.webp`, same folder |
| **Files moved** | ~480 files into `Phone Wallpapers/`, `Social Assets/`, `Ultrawide Wallpapers/` |
| **Duplicate removed** | `Year of 2021/` deleted — it was byte-identical to `2021 Wallpaper/` |

## Do I need to do anything?

| Your situation | Go to |
|---|---|
| You just browse or download | Nothing to do — use the ZIP or a fresh clone |
| You cloned, no local commits | [Fix A](#fix-a--existing-clone-no-local-work) |
| You forked, no custom commits | [Fix B](#fix-b--fork-without-custom-commits) |
| You have your own commits on top | [Fix C](#fix-c--forkclone-with-your-own-commits) |
| You only want the latest files | [Fix D](#fix-d--i-just-want-the-images) |

## Fix A — existing clone, no local work

```bash
cd The-Wallpaper-Collection
git fetch origin
git reset --hard origin/main
git clean -fd          # optional: drop files that no longer exist upstream
```

That is all. `git pull` is not the right tool here.

## Fix B — fork without custom commits

On GitHub: open your fork → **Sync fork** → if it offers **Discard commits**, take it.

If GitHub refuses because the histories are unrelated, use the command line instead:

```bash
git remote add upstream https://github.com/MilesCorporate/The-Wallpaper-Collection.git
git fetch upstream
git reset --hard upstream/main
git push --force origin main
```

## Fix C — fork/clone with your own commits

Your commits are safe; they simply sit on the old history. Replay them onto the new one.

**Option 1 — rebase** (if `95d3b2c` is in your history):

```bash
# skip the first line if you already have an `upstream` remote
git remote add upstream https://github.com/MilesCorporate/The-Wallpaper-Collection.git
git fetch upstream
git branch backup/my-work            # safety net
git rebase --onto upstream/main 95d3b2c main
git push --force-with-lease origin main
```

`95d3b2c` was the last commit of the old history. If you forked earlier, replace it with the last upstream commit in your branch — the commit right before your first own commit (`git log --oneline --graph` helps).

**Option 2 — patches** (works regardless of fork point):

```bash
git remote add upstream https://github.com/MilesCorporate/The-Wallpaper-Collection.git
git format-patch --stdout <your-fork-point>..main > ~/my-wallpaper-changes.patch
git fetch upstream
git reset --hard upstream/main
git am ~/my-wallpaper-changes.patch
```

Expect conflicts where your changes touch files that moved — the mapping below tells you where they went. Resolve, then push.

> Either way your fork is not damaged: the old history still exists inside it.

**Open pull requests:** PRs opened against the old history can no longer be merged. Rebase your branch as above, then open a fresh PR against the new `main`.

## Fix D — I just want the images

```bash
git clone --depth 1 https://github.com/MilesCorporate/The-Wallpaper-Collection.git
```

Or use **Code → Download ZIP** on GitHub.

## Where did my file go?

| Old path | New path |
|---|---|
| `Year of 2021/**` | removed — identical to `2021 Wallpaper/**` |
| `Artemis II/**` | `Phone Wallpapers/NASA Artemis II/**` |
| `2021 Wallpaper/iPhone 12 Wallpaper/**` | `Phone Wallpapers/iOS/iPhone 12/**` |
| `2018-2020 Wallpaper/The Crew 2/**` | `Social Assets/The Crew 2/**` |
| `Aura Wallpaper/**` (mobile sizes) | `Phone Wallpapers/Android/Aura/**` |
| `Stokes/*_iPhone*` | `Phone Wallpapers/iOS/Stokes/` |
| other portrait images from year folders | `Phone Wallpapers/{iOS,Android,Misc}/<year>/` |
| `v2-*.jpg` avatars, `images.jpg`, `download.png` | `Social Assets/Avatars/` or `Social Assets/Misc/` |
| any image ≥ 2.05:1 and ≥ 2560×1000 | `Ultrawide Wallpapers/{21x9,32x9,Panorama}/` (same filename; one collision became `1201491 (2).jpg`) |
| `*.png` anywhere | `*.webp` in the same folder |

Scripts that glob `*.png` will now match nothing — switch to `*.webp` (or both).

## About WebP

The 703 PNGs were re-encoded to WebP quality 92, cutting 4.0 GB of PNG down to ~0.4 GB. Measured on a sample: **PSNR 38.1 dB / SSIM 0.982** — invisible at normal viewing distance, slightly soft at 1:1 on hard edges.

- **Windows 10:** install *WebP Image Extensions* from the Microsoft Store. **Windows 11** opens them natively.
- **macOS / Linux / browsers:** native support.
- Need PNG back? `sips -s format png in.webp --out out.png` (macOS) or `magick in.webp out.png` (ImageMagick). The original detail is already lost, though.

## Why?

Three reasons: a byte-identical duplicate tree doubled the checkout; PNGs were 39% of the repository with no quality benefit; and phone / social / ultrawide images were scattered across nine year folders. The full changelog is in [README.md](README.md#update-log).
