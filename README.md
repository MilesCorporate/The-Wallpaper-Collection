# The Wallpaper Collection

<p align="center">
  <strong>Eight years of desktop taste — one repo. ~5.9 GiB of media. 2,688 images + 18 videos. 28 flat shelves, zero subfolders.</strong><br>
  <sub>八年策展 · 一个仓库 · 每层只有一级文件夹 · 拿来即用 · 不必再乱搜壁纸</sub>
</p>

<p align="center">
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers"><img src="https://img.shields.io/github/stars/MilesCorporate/The-Wallpaper-Collection?style=for-the-badge&logo=github&label=Stars&color=ffcc00" alt="GitHub stars"></a>
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection/network/members"><img src="https://img.shields.io/github/forks/MilesCorporate/The-Wallpaper-Collection?style=for-the-badge&logo=github&label=Forks&color=4078c0" alt="GitHub forks"></a>
  <img src="https://img.shields.io/badge/images-2%2C688-blue?style=for-the-badge" alt="2688 images">
  <img src="https://img.shields.io/badge/size-5.9%20GiB-9b59b6?style=for-the-badge" alt="5.9 GiB media">
  <img src="https://img.shields.io/badge/folders-28-2ecc71?style=for-the-badge" alt="28 folders">
  <img src="https://img.shields.io/badge/depth-1%20level-e67e22?style=for-the-badge" alt="One folder level">
</p>

<p align="center">
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection"><img src="https://img.shields.io/badge/⭐_Star_this_repo-ff4785?style=for-the-badge&logo=github" alt="Star"></a>
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection/fork"><img src="https://img.shields.io/badge/🍴_Fork_&_own_it-24292f?style=for-the-badge&logo=github" alt="Fork"></a>
</p>

<p align="center">
  <a href="#english">English</a> · <a href="#中文">中文</a> · <a href="#get-it-in-30-seconds">Quick start</a> · <a href="#flat-by-design">Flat layout</a> · <a href="#starter-packs">Starter packs</a> · <a href="#star--fork--why-it-matters">Why Star / Fork</a> · <a href="MIGRATION.md">Migration</a>
</p>

> [!IMPORTANT]
> **2026-10-28 · Every shelf is now exactly one level deep — `Folder/image.jpg`, no subfolders inside any of them.**
> **804 files** moved up out of **68 nested folders**; **78 subfolders** are gone, **7 byte-identical duplicates** collapsed, **0 unique images lost**. **Why:** the macOS wallpaper pane only reads the folder you point it at — it does not walk into subfolders, so a folder-of-folders shows an empty shelf. Now *System Settings → Wallpaper → Add Folder…* → pick any of the **28 shelves** and every image inside appears.
>
> **2026-10-28 · 目录已扁平化：`文件夹/图片`，28 个收藏文件夹里不再有任何子文件夹。** **804 个文件**从 **68 个嵌套目录**上移、**78 个子文件夹**全部消失、**7 张逐字节重复图**合并，**没有丢失任何独有图片**。**原因：** macOS 壁纸面板只读取你选中的那一层文件夹，不会递归进子文件夹——所以「文件夹套文件夹」在壁纸面板里等于空目录。现在把任意一个**顶层文件夹**添加到壁纸面板，里面的图片会全部出现。

> [!NOTE]
> **2026-10-21 · History was rewritten.** Every old commit and tag now has a new SHA and ~480 files moved (`*.png` → `*.webp`; new `Phone Wallpapers/`, `Social Assets/`, `Ultrawide Wallpapers/` lanes). A clone or fork from before that date must be re-cloned — see **[MIGRATION.md](MIGRATION.md)**.
>
> **2026-10-21 · 历史已重写。** 旧 commit 与 tag 全部换了 SHA，约 480 个文件迁移。此前 clone 或 fork 的请重新 clone，或按 **[MIGRATION.md](MIGRATION.md)** 处理。

---

> **Enjoying this archive?** A **Star** helps others discover it on GitHub. A **Fork** saves the entire museum to your account — your backup, your remix, your PRs welcome.  
> **喜欢这份收藏？** 点 **Star** 让更多人看见；**Fork** 一份到你自己账号，永久备份，也欢迎贡献壁纸。

---

## English

<a id="english"></a>

### Your screen deserves better than a search result

Most wallpaper repos are a dump of random downloads — mislabeled files, duplicate resolutions, no story. **The Wallpaper Collection** is the opposite: a **personal museum** built since **2018**, organized into **28 top-level shelves** whose only job is to be *selectable*: one folder, one vibe, every image directly inside it.

Clone it once. Browse by mood, device, or era. Stop hunting the same Unsplash tab every Monday.

**If this repo saves you even one afternoon of searching — [leave a star](https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers).** It costs nothing. It helps this project reach the next person who needs it.

---

<a id="get-it-in-30-seconds"></a>

## Get it in 30 seconds

| Action | What to do |
|--------|------------|
| **Bookmark** | [**Star the repo**](https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers) — stay updated, boost visibility |
| **Own a copy** | [**Fork**](https://github.com/MilesCorporate/The-Wallpaper-Collection/fork) — full collection under *your* GitHub (backup + customize) |
| **Use locally** | Clone (media files ~5.9 GiB, Git history included in the clone) |
| **Use on macOS** | *System Settings → Wallpaper → Add Folder…* → any of the 28 shelves |

```bash
# Clone the full collection
git clone https://github.com/MilesCorporate/The-Wallpaper-Collection.git

# Optional: shallow clone (faster, less git history)
git clone --depth 1 https://github.com/MilesCorporate/The-Wallpaper-Collection.git
```

Then open the folder for your device — or jump to [**Starter packs**](#starter-packs) below.

**Repo:** [github.com/MilesCorporate/The-Wallpaper-Collection](https://github.com/MilesCorporate/The-Wallpaper-Collection)

---

<a id="flat-by-design"></a>

## Flat by design — one level, on purpose

The macOS wallpaper pane reads **one folder**, not a tree. Point it at a folder that only contains subfolders and you get an empty-looking album — the images one level down are simply invisible. That is the entire reason this repository has no nesting.

```
The-Wallpaper-Collection/
├── 2018-2020 Wallpaper/      ← 603 images, directly inside
├── 2021 Wallpaper/           ← 351 images + 18 videos, directly inside
├── 2022 Wallpaper/           ← 151 images
├── …                         ← 23 more shelves, same rule
├── Ultrawide Wallpapers/     ← 188 images
├── Phone Wallpapers/         ← 173 images
├── README.md
└── scripts/                  ← tooling, not wallpapers
```

**The rule:** `Shelf/` contains images; it never contains a folder.

- **28 shelves, one level, no exceptions.** Adding a subfolder is a bug, not a style choice.
- **Every shelf is a valid wallpaper album.** 1 file or 603 — the folder itself is the unit macOS understands.
- **Shells get simpler too.** No `**` globs, no `find -maxdepth` guesswork: `ls "Ultrawide Wallpapers"` is the whole lane.

### Make it a macOS wallpaper album in 20 seconds

1. **System Settings → Wallpaper → Add Folder…**
2. Pick a shelf, e.g. `~/Pictures/The-Wallpaper-Collection/2026 Wallpaper`
3. Done — macOS rotates through every image in that folder, and skips nothing, because nothing hides in a subfolder.

Want the whole museum in one place? Add the repository root, then drill into whichever shelf you want — each one is already flat.

*The same holds true for **Windows** (picture slideshow → *Browse*), **GNOME / KDE** slideshow extensions, and **Wallpaper Engine**'s folder watch: they all read a folder non-recursively.*

<details>
<summary><strong>What changed in the flattening (2026-10-28)</strong></summary>

| Change | Detail |
|---|---|
| **Files moved up** | 804 files from 68 nested folders (`Phone Wallpapers/iOS/…`, `2021/CyberPunk 2077/Arasaka/`, `Windows11/Wallpaper/ThemeA/`, `Social Assets/The Crew 2/01_SCREENSHOTS/`, …) |
| **Folders removed** | 78 — the 68 above plus 10 intermediate parents — including the two-deep `Windows11-DefaultWallpaper/4K/Wallpaper/Windows/` path |
| **Duplicates collapsed** | 7 byte-identical Surface images (the Oct-2018 event set and the 27-image Surface set shared them) |
| **Content lost** | none — every remaining file is unique |
| **Sub-theme names** | preserved where they matter in the filenames themselves (`Cyberpunk2077_Wallpapers_Arasaka_3840x2160_EN.webp`, `Surface Laptop 2 - Cobalt.jpg`, `0 - Aura #1 - 1920x1080.webp`) |

</details>

---

<a id="starter-packs"></a>

## Starter packs — four paths in, no overwhelm

Pick one lane. Star the repo if it lands. Fork when you want your own vault.

| Pack | Open these folders first | Best for |
|------|--------------------------|----------|
| **New machine** | `2026 Wallpaper` → `2025 Wallpaper` → `macOS-Collections` → `Apple Park` | Fresh 4K/5K/6K setup, Mac or PC |
| **Ultrawide / sim racing** | `Ultrawide Wallpapers` → `2026 Wallpaper` (F1, automotive) | 21:9 / 32:9 monitors |
| **Vibe / fandom** | `黑猫的野望壁纸包` · `2021 Wallpaper` (Cyberpunk) · `Phone Wallpapers` (Artemis II) | Anime, Night City, NASA |
| **Automotive / design** | `BugattiDestrier` · `2026 Wallpaper` (search F1, Audi, Mercedes-AMG) | Hypercars, racing, industrial design |

---

<a id="star--fork--why-it-matters"></a>

## Star & Fork — why it matters

### Star — 2 seconds, real impact

- **Free bookmark** with release notifications when the collection grows  
- **Signals quality** to GitHub search and awesome-list curators  
- **Supports the maintainer** — curation is manual; stars are the thank-you  

[**Star The Wallpaper Collection**](https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers)

### Fork — make it yours

- **Personal backup** of ~5.9 GiB of media / 2,688 images + 18 videos on *your* account
- **Customize** — keep only the years/themes you love  
- **Contribute back** — PR new wallpapers into the shared museum  
- **Share** — point friends to *your* fork with your own notes  

[**Fork The Wallpaper Collection**](https://github.com/MilesCorporate/The-Wallpaper-Collection/fork)

### Spread the word

Know someone still using a blurry Pinterest crop? Send them:

`https://github.com/MilesCorporate/The-Wallpaper-Collection`

Tweet / post template:

> 8 years of curated wallpapers — 2,688 images + 18 videos, Cyberpunk, NASA Artemis II, Bugatti, anime, macOS 6K collections. 28 flat folders, no subfolders. Free repo.
> https://github.com/MilesCorporate/The-Wallpaper-Collection

---

### Why this collection hits different

| What you get | Why it matters |
|--------------|----------------|
| **Curated, not scraped** | Every one of the 28 shelves has a reason to exist — annual archive, brand drop, or dedicated aesthetic lane |
| **Flat, not nested** | One folder level means the macOS wallpaper pane, Windows slideshow and every folder picker can actually see the images |
| **Resolution-ready** | From 1080p classics to **4K / 5K / 6K / 8K** and **ultrawide (3440×1440+)**, including Formula 1, automotive, and Mac-native masters |
| **Device-aware sets** | iPad (YTECHB), iPhone 12 official, ultrawide packs, dark/light **paired** macOS gradients |
| **Culture + craft** | Cyberpunk corp factions, anime opus (**190** pieces), Apple Park **HEIC** campus set, **Artemis II** lunar flyby, and a dedicated **Bugatti** drop |
| **Living archive** | **2026** alone is **511.5 MiB / 221 images** — the active growth lane, not a stale snapshot |

---

### By the numbers

| Metric | Value |
|--------|-------|
| **Collection span** | 2018 → 2026 |
| **Top-level categories** | **28** folders |
| **Folder depth** | **1 level** — no subfolders, by design |
| **Working-tree media size** | **~5.9 GiB** (images and videos) |
| **Image files** | **2,688** (JPG, WebP, HEIC, HEIF — PNG retired to WebP) |
| **Video files** | **18** (MOV, iPhone 12 Live set in `2021 Wallpaper`) |
| **Resolution band** | 1080p through **8K** |
| **Largest single theme** | `黑猫的野望壁纸包` — **734.7 MiB**, **190** anime wallpapers |
| **Newest spotlight** | `2026 Wallpaper` — **511.5 MiB**, **221** images |
| **Fresh thematic drop** | `BugattiDestrier` — **33** Bugatti Solitaire Destrier wallpapers |

---

### Who this is for

- **Desktop maximalists** — ultrawide, multi-monitor, 4K/5K who want files that actually fill the canvas  
- **Mac people** — HEIC Apple Park, `macOS-Collections` 6K stills, macOS-style gradients, iPhone/iPad official lanes  
- **Gamers & sci-fi heads** — Cyberpunk 2077 corporate sets, The Crew 2, ROG/MSI era, WallpaperEngine-ready vibes  
- **Photography lovers** — Unsplash curation across years, Getty picks, landscape and astro  
- **Anime / illustration fans** — the largest dedicated pack in the repo  
- **Car & design people** — Bugatti Solitaire Destrier, F1, Audi RS, and Mercedes-AMG visual lanes
- **Space nerds** — **NASA Artemis II** Earth–Moon–Orion views
- **Archivists** — year-by-year folders that tell the story of what was worth saving each season  

---

### How the archive is organized

```
The-Wallpaper-Collection/
├── 📅 Annual shelves (2018–2026)   ← time machine: what was hot each year
├── 🎨 Thematic vaults              ← deep dives: brands, games, textures, automotive
├── 🖥️ Ultrawide Wallpapers         ← 21:9, 32:9 and panorama, in one lane
├── 📱 Phone Wallpapers             ← every portrait screen, in one lane
├── 📣 Social Assets                ← avatars, banners, press kits (not wallpapers)
└── README.md                       ← you are here
```

**Annual shelves** = chronological taste. **Thematic shelves** = obsession-level depth on one vibe. Nothing is nested; the folder name is the whole taxonomy.

---

### The 28 shelves, at a glance

#### Annual — a timeline of taste

| Shelf | Images | Size | In one line |
|-------|-------:|-----:|-------------|
| `2018-2020 Wallpaper` | 603 | 1018.8 MiB | Foundation era: Fluent, Surface, ROG, MSI, Windows |
| `2021 Wallpaper` | 351 + 18 video | 817.4 MiB | Gaming renaissance: Cyberpunk factions, iPhone 12 Live |
| `2022 Wallpaper` | 151 | 293.1 MiB | Quality over quantity |
| `2023 Wallpaper` | 104 | 226.9 MiB | Modern minimalism |
| `2024 Wallpaper` | 89 | 225.4 MiB | Diverse fusion, transition year |
| `2025 Wallpaper` | 209 | 643.0 MiB | The evolution year — best all-round shelf |
| `2026 Wallpaper` | 221 | 511.5 MiB | Current flagship lane |

#### Device & format lanes

| Shelf | Images | Size | In one line |
|-------|-------:|-----:|-------------|
| `Ultrawide Wallpapers` | 188 | 489.9 MiB | Everything ≥ 2.05:1 — 21:9, 32:9, panorama |
| `Phone Wallpapers` | 173 | 89.8 MiB | iOS, Android, NASA Artemis II, misc — all portrait |
| `Social Assets` | 125 | 21.2 MiB | Avatars, banners, The Crew 2 press kit — not wallpapers |

#### Thematic vaults, brands & OS-native

| Shelf | Images | Size | In one line |
|-------|-------:|-----:|-------------|
| `黑猫的野望壁纸包` | 190 | 734.7 MiB | Anime cathedral — the largest pack |
| `macOS-Collections` | 16 | 209.1 MiB | Apple's 6K collection stills (up to 6106×4512) |
| `BugattiDestrier` | 33 | 141.4 MiB | BUGATTI Solitaire Destrier hypercar drop |
| `Apple Park` | 9 | 129.3 MiB | HEIC campus architecture |
| `Stokes` | 10 | 95.8 MiB | Expressive fine-art leaning |
| `Unsplash` | 20 | 77.4 MiB | Photographer-attributed professional work |
| `CyberPunk Wallpaper` | 29 | 70.3 MiB | Neon noir standalone |
| `Texture` | 11 | 68.0 MiB | Stone, fabric, metal, organic surfaces |
| `MKBHDWallpapers` | 27 | 38.9 MiB | Tech aesthetic, 8K polygon, Bleeding Edge |
| `CrystalWallpapers` | 22 | 32.1 MiB | Crystal & refraction renders |
| `Windows11-DefaultWallpaper` | 36 | 27.7 MiB | Theme A–D, 4K, touch keyboard, Spotlight |
| `Facets` | 5 | 13.0 MiB | Polygonal / geometric abstract |
| `GettyImages` | 20 | 10.0 MiB | Stock photography selections |
| `wallpapers_pack` | 3 | 8.6 MiB | General mixed pack |
| `Mac Internal` | 14 | 4.8 MiB | Mac-internal design language experiments |
| `Look Back` | 7 | 2.5 MiB | Vintage nostalgia |
| `Aura Wallpaper` | 21 | 990.4 KiB | The Aura gradient system, desktop sizes |
| `LinksPhotograph` | 1 | 160.8 KiB | Compact reference archive |

---

## Annual collections — a timeline of taste

### `2018-2020 Wallpaper` · 1018.8 MiB · 603 images  
**The foundation era**

Where the standards were set. This is the **brand-and-platform** chapter, and every set now sits directly in the shelf — the filename tells you which one it came from:

- **Fluent Design Collection** — Microsoft's design language, clean and confident (`Abstract Office.webp`, `Data Stream.jpg`, …)  
- **Surface Collection** — WallpaperHub-era Surface exclusives (`Surface Laptop 2 - Cobalt.jpg`, `Surface Studio 2.jpg`, …)  
- **MSI** & **ROG** — gaming hardware identity, esports energy (`ROG_wallpaper_…`, `wallpaper_1591…`)  
- **The Crew 2** press kit — the full social-media drop now lives in `Social Assets`  
- **Windows Wallpapers Collection** — official Windows aesthetics (`Windows 10 Bliss.jpg`, `Betta Fish.jpg`, …)  
- **October 2018 Event Collection** — event-era Surface/Headphones drops  

*Perfect if you want nostalgic Windows/Surface/ROG energy on a modern panel.*

---

### `2021 Wallpaper` · 817.4 MiB · 351 images + 18 videos  
**The gaming renaissance**

The year the repo went **loud**:

- **CyberPunk 2077** — corporate faction packs: **Arasaka**, **Kang Tao**, **Militech**, **Trauma Team** (each PNG now a WebP, faction name in the filename)  
- **Hello** — minimalist greeting-series designs  
- **Holiday** — seasonal warmth  
- **Yosemite** — national-park grandeur  
- **iPhone 12 Live** — the 18 **MOV** files, the only videos in the collection  

*If your desktop should feel like Night City with optional Apple polish.*

---

### `2022 Wallpaper` · 293.1 MiB · 151 images  
**Quality over quantity**

A tighter year — fewer files, higher bar. The curation philosophy shifted from “collect everything good” to **“only keep what still slaps.”**

---

### `2023 Wallpaper` · 226.9 MiB · 104 images  
**Modern minimalism**

Clean lines, calm palettes, contemporary restraint. Ideal for **focus setups** and laptops you do not want visually shouting.

---

### `2024 Wallpaper` · 225.4 MiB · 89 images  
**Diverse fusion**

Mixed styles reflecting how design trends collided — abstract, photo, tech, moody darks. A **transition year** into the AI-and-ultrawide era.

---

### `2025 Wallpaper` · 643.0 MiB · 209 images  
**The evolution year**

The most **well-rounded** single-year shelf in the repo:

- **Dark / Light paired 4K gradients** (`*_DM-4K` / `*_LM-4K`) — built for macOS theme switching  
- **Massive Mac-native masters** (e.g. `20250901_Mac.jpg` tier — multi-megabyte detail)  
- **YTECHB iPad** curation — tablet aspect ratios done right  
- **AI art (aishot and similar)** — generative aesthetics without abandoning photography  
- **Automotive & F1** — Ferrari, Mercedes-AMG, BMW, concept cars at **1440w+**  
- **Unsplash 2025** — fresh professional work  
- **Nature** — rivers, mountains, oceans, weather drama  

*This is the folder you open first for a new machine setup.*

---

### `2026 Wallpaper` · 511.5 MiB · 221 images  
**The current flagship lane**

Not a teaser folder — a **full-season drop**:

- **Unsplash 2026** — photographer-attributed filenames (`*-unsplash.jpg`)  
- **Nature & wildlife** — whales, landscapes, atmospheric skies  
- **Automotive & racing** — Audi RS, Formula 1 (Ferrari, Mercedes-AMG W17), high-res wides  
- **macOS heritage & new** — Mavericks nostalgia, `*_Mac.webp` series, Rose gradients  
- **Pexels / mixed pro stock** — variety without losing cohesion  

**If you only sync one folder this month, sync this one.**

---

## Thematic vaults — obsession, packaged

### `黑猫的野望壁纸包` · 734.7 MiB · 190 images  
**The anime cathedral**

The **largest themed pack** in the entire repository. Otaku culture, illustration-forward compositions, Japanese animation aesthetics at full volume. If you want one folder that defines “collection personality,” it is this one.

---

### `macOS-Collections` · 209.1 MiB · 16 images  
**Apple's 6K collection stills**

Official macOS collection artwork at **6K** — mostly 6016 px wide, up to **6106×4512** — the wide, cinematic scenes Apple ships as 6K desktop pictures. Pairs beautifully with a Retina display and macOS's own colour management; includes the dark/server-room variants (`10-5-Server-6k.jpg`, `10-6-Server-6k.jpg`).

---

### `BugattiDestrier` · 141.4 MiB · 33 images
**The hypercar room**

A dedicated **BUGATTI Solitaire Destrier** drop: sculptural bodywork, dark studio compositions, close details, and high-contrast automotive design. One model, one visual language, no filler — for the desktop that should feel like a concept car under a spotlight.

---

### `Apple Park` · 129.3 MiB · 9 HEIC images  
**Campus as art**

Premium **HEIC** photography of Apple Park — not wallpapers ripped from press JPEGs, but **architectural studies**:

| File | Subject |
|------|---------|
| `ApplePark.heic` | Campus panorama |
| `Arch.heic` | Curved architecture |
| `Entrance.heic` | Main entrance |
| `Fountain.heic` | Central fountain |
| `Lobby.heic` | Interior minimalism |
| `Pathway.heic` | Gardens & walkways |
| `Shadow.heic` | Light and shadow play |
| `Stairwell.heic` | Iconic spiral staircase |
| `Fitness.heic` | Fitness center interior |

*Best on Retina Mac displays; convert for Windows if needed (see [Formats](#file-formats--compatibility)).*

---

### `Phone Wallpapers` · 89.8 MiB · 173 images  
**The mobile lane — one folder for every portrait screen**

Phone art used to be scattered through the year folders (and, until October 2026, split into `iOS/`, `Android/`, `Misc/` subfolders). Now it is one flat shelf — exactly what you want to sync or point a phone-side picker at:

- **iPhone 12 official set** + **Teardown** wallpapers (16 stills plus 6 teardown pieces)  
- **Android** picks from 2018–2022, plus the **Aura** mobile gradients (`0 - Aura #1 - Mobile - 1242x2688.webp`, …)  
- **NASA Artemis II** — the 22 official mission wallpapers (1080×1920), Earth–Moon–Orion (`02-artemis-ii-*.jpg`)  
- **Misc** — everything else phone-shaped, mixed in one place  

*One folder to sync to a phone; desktop folders stay desktop-only.*

---

### `Ultrawide Wallpapers` · 489.9 MiB · 188 images  
**21:9, 32:9 and panorama — one lane for wide screens**

Every image at **2.05:1 or wider** (min 2560 px wide, 1000 px tall) lives here, as one flat album:

| Aspect | Typical resolutions | Images |
|--------|---------------------|-------:|
| 21:9 | 3440×1440, 2560×1080, 3840×1600, 5162×2160 | 142 |
| 32:9 | 5120×1440, 7680×2160 | 36 |
| Panorama | ≥ 4.0, 7500×1261+ murals | 10 |

*Add this one folder to wallpaper rotation and every panel gets something; check exact dimensions in Finder's preview when you need a pixel-perfect fit.*

---

### `Social Assets` · 21.2 MiB · 125 images  
**Avatars, banners, press kits — deliberately not wallpapers**

- **The Crew 2** — the full Ubisoft press kit: Facebook covers, Twitter/Instagram/YouTube avatars, banners, key art  
- **Avatars** — small square profile images pulled out of 2018–2021  
- **Misc** — stray downloads (`images.jpg`, `download.jpeg`) that were never wallpapers  

*Kept for reference, separated so the wallpaper shelves stay clean.*

---

### `MKBHDWallpapers` · 38.9 MiB · 27 images  
**Tech aesthetic, creator-curated**

Marques Brownlee–adjacent tech wallpaper culture: **8K polygon** series, **Bleeding Edge** dark tech, numbered **1622xxx** series, vibrant color-tech hybrids. Built for people who care about **industrial design on a pixel grid**.

---

### `CrystalWallpapers` · 32.1 MiB · 22 images  
**Crystal & refraction**

Refractive surfaces, gem-like renders, glassy abstractions — formerly split into `Crystal/`, `Encorified/`, `New/` and `Unused/`, now one album. Gorgeous on **2K and 4K** where fine detail matters.

---

### `CyberPunk Wallpaper` · 70.3 MiB · 29 images  
**Neon noir standalone**

Extra Night City energy beyond the 2021 faction folders — dystopian futures, chrome and rain.

---

### `Aura Wallpaper` · 990.4 KiB · 21 images  
**Gradient system**

Desktop variants of the Aura gradient family — from simple two-tone to complex multi-stop blends (`0 - Aura #1 - 1920x1080.webp` through `4 - Aura #2 - 2560x1600.webp`). The mobile sizes live in `Phone Wallpapers`; the ultrawide sizes in `Ultrawide Wallpapers`.

---

### `Texture` · 68.0 MiB · `Stokes` · 95.8 MiB · `Facets` · 13.0 MiB  
**Surface, art, geometry**

- **Texture** — materials: stone, fabric, metal, organic surfaces  
- **Stokes** — expressive fine-art leaning  
- **Facets** — polygonal / geometric abstract  

The “my wallpaper is subtle but expensive” trio.

---

### `Unsplash` · 77.4 MiB · `GettyImages` · 10.0 MiB · `LinksPhotograph` · 160.8 KiB  
**Photography lane**

Hand-picked **Unsplash**, professional **Getty** selections, and a compact **LinksPhotograph** reference archive.

---

### `Mac Internal` · 4.8 MiB · `Windows11-DefaultWallpaper` · 27.7 MiB  
**OS-native energy**

Mac-internal design language experiments and **official Windows 11** default variants — Theme A–D, 4K, Spotlight, touch-keyboard assets — for purists who want **platform-authentic** backgrounds. The Windows `Desktop.ini` theme metadata was dropped when the theme folders were flattened; the images themselves are all still here.

---

### `Look Back` · 2.5 MiB · `wallpapers_pack` · 8.6 MiB  
**Retro & misc**

Vintage nostalgia (`Look Back`) plus a general mixed **`wallpapers_pack`** for surprises.

---

## Sources — quality bar, not quantity bar

| Source | What you are getting |
|--------|----------------------|
| **Unsplash** | Photographer-attributed professional work ([license](https://unsplash.com/license)) |
| **WallpaperEngine / Steam Workshop** | Community motion & static art (subscription/software may apply) |
| **MKBHD ecosystem** | Tech-forward visual culture |
| **Getty Images** | Stock photography selections — respect licensing for commercial use |
| **Apple / Microsoft / MSI / ROG** | Brand-official or brand-era releases |
| **NASA** | Artemis II mission media |
| **Automotive / design** | Curated vehicle imagery — respect the original rights holders |
| **AI platforms** | Midjourney, DALL·E, Stable Diffusion-era pieces in modern year folders |
| **Personal curation** | Anything here passed a human “keep” decision |

---

## Pick your setup

### 4K / 5K displays

Start with **`2025 Wallpaper`** and **`2026 Wallpaper`**, then **`MKBHDWallpapers`**, **`macOS-Collections`** (6K) and **`Apple Park`** (HEIC). You paid for pixels — use them.

### Ultrawide (21:9 / 32:9)

**`Ultrawide Wallpapers`** — 188 images, one album, all ≥ 2.05:1. No more hunting `3440x1440` across nine year folders.

### Automotive / design

Start with **`BugattiDestrier`** for a focused hypercar set, then browse **`2026 Wallpaper`** for F1, Audi RS, Mercedes-AMG, and other wide automotive imagery.

### 1080p / older hardware

Everything scales down fine. Prioritize **`Texture`**, **`Stokes`**, **`2022–2023`** years for smaller file weights.

### iPad

**`2025 Wallpaper`** — YTECHB / iPad-optimized aspect ratios.

### iPhone

**`Phone Wallpapers`** — iPhone 12 official stills, Teardown, and Artemis II; the Live set is 18 MOV files in `2021 Wallpaper`.

### Android

**`Phone Wallpapers`** — 16:9 and 18:9 assets abound, plus the Aura mobile gradients.

### WallpaperEngine (dynamic)

Install via Steam. Some Workshop items need subscription. GPU recommended; disable aggressive battery saver for motion wallpapers.

---

<a id="file-formats--compatibility"></a>

## File formats & compatibility

| Format | Best for | Notes |
|--------|----------|-------|
| **JPEG** | Photos, large scenes | Smaller size, great for Unsplash/nature |
| **WebP** | Gradients, illustration, UI-clean art | Repo standard (q92); PNG sources were re-encoded in Oct 2026 |
| **HEIC / HEIF** | Apple Park set and other images | Native support varies; Windows may need HEIF extensions or conversion |
| **MOV** | iPhone 12 Live wallpapers (18 files in `2021 Wallpaper`) | Plays in QuickTime; macOS can use them as dynamic wallpapers |
| **PNG** | Legacy only | Kept only where lossless alpha is mandatory |

**Windows HEIC / HEIF tip:** Microsoft Store → *HEIF Image Extensions*, or run `bash scripts/heic2jpg.sh` to create JPEG siblings in place.

---

## Tooling

| Script | What it does |
|--------|--------------|
| `python3 scripts/stats.py` | Per-folder image/video counts and sizes. `--check` verifies this README **and** that no shelf has grown a subfolder, `--write` fixes the numbers |
| `python3 scripts/build_gallery.py` | Builds a local HTML gallery with lazy thumbnails in `gallery/` (gitignored) |
| `bash scripts/heic2jpg.sh` | Converts HEIC/HEIF to JPEG siblings for Windows / Linux |

---

## Copyright & fair use

This repository is a **personal curated archive** shared for appreciation and reference.

- **Rights remain with original creators and rights holders.**  
- **Personal desktop use** is the intended context.  
- **Commercial use** requires licenses from the relevant rights holder (Getty, brands, NASA media guidelines, etc.).  
- **Do not** redistribute the entire collection as a commercial product.  
- **Unsplash** — follow the [Unsplash License](https://unsplash.com/license).  
- **WallpaperEngine** — requires valid Steam/Workshop terms.  

Found a rights issue? Open a GitHub Issue — takedown-friendly.

---

## Curation philosophy

1. **Would I actually set this?** — keeper test  
2. **Does the folder teach a story?** — year or theme, never “misc_(final)(2)”  
3. **One level, always** — a shelf holds images, not folders; macOS only reads the level you point at  
4. **Resolution honesty** — keep native high-res; avoid upscaled mush  
5. **Annual closure** — each year gets its lane; active work lives in the current year folder  
6. **Special drops earn a folder, not a subfolder** — NASA Artemis II fits inside `Phone Wallpapers` as a filename prefix, not a nested directory  

---

## Update log

| When | What changed |
|------|----------------|
| **Oct 28, 2026** | **Flat layout.** All 28 shelves reduced to one level: **804 files** moved up, **78** empty subfolders removed, **7** byte-identical duplicates collapsed (Oct-2018/Surface set). `macOS-Collections` documented. Repo now **28 folders / 2,688 images / 18 videos / ~5.9 GiB**, ready for *System Settings → Wallpaper → Add Folder…* |
| **Oct 21, 2026** | Re-curated: phone wallpapers → `Phone Wallpapers/`, press kits & avatars → `Social Assets/`; byte-identical `Year of 2021` tree removed; new `Ultrawide Wallpapers/` lane; PNG art re-encoded to WebP q92; repo then **28 folders / 2,685 images / 18 videos / ~5.8 GiB**, `.git` down from 8.9 GB to 5.7 GB — existing clones/forks: see **[MIGRATION.md](MIGRATION.md)** |
| **Oct 8, 2026** | Stats checked against the working tree: **27 folders**, **3,079 images**, **36 videos**, ~**10.2 GiB** of media; `2026 Wallpaper` has **272 images / ~963 MiB** |
| **Aug 7, 2026** | README stats refresh: ~18 GB, **3,033 images**, **26 folders**; added **`BugattiDestrier`** (33 images / 141 MB) |
| **Jun 2026** | README v10 showcase edition; previous stats snapshot (2,918 files, 25 categories) |
| **2026** | Earlier snapshot: `2026 Wallpaper` → **242 images / 831 MB**; added the **NASA Artemis II** set (22 phone wallpapers) |
| **2025** | **252 images / 1.1 GB** — AI art, iPad series, ultrawide, macOS DM/LM pairs, F1/automotive |
| **2024** | 383 MB — style fusion year |
| **2023** | 309 MB — minimalism pass |
| **2021** | Cyberpunk corp factions peak; iPhone 12 official |
| **2018** | Collection born — Fluent, Surface, ROG, MSI standards |

---

## Acknowledgments

**Unsplash** photographers, **WallpaperEngine** creators, **MKBHD** & **YTECHB**, **NASA** for Artemis II public imagery, game art teams (**Cyberpunk 2077**, **The Crew 2**), **Apple** & **Microsoft** design ecosystems, automotive designers and photographers, AI artists pushing new aesthetics, and every independent photographer whose work made the cut.

---

## Contact & contribute

**Want this collection to grow?** Star it. Fork it. Open a PR. That is how open-source archives win.

| How to help | Link |
|-------------|------|
| **Star** (bookmark + discoverability) | [github.com/MilesCorporate/The-Wallpaper-Collection/stargazers](https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers) |
| **Fork** (your copy + PRs) | [github.com/MilesCorporate/The-Wallpaper-Collection/fork](https://github.com/MilesCorporate/The-Wallpaper-Collection/fork) |
| **Issues** — suggest a folder, report copyright | [New Issue](https://github.com/MilesCorporate/The-Wallpaper-Collection/issues/new) |
| **Recommendations** | Wallpaper links worth a permanent shelf |

**Contribution ideas:** new year folder drops · thematic packs · better README tables · device-specific starter lists · translations.

**One rule to remember:** add files to an existing shelf or propose a new top-level shelf — never a subfolder. See [CONTRIBUTING.md](CONTRIBUTING.md).

Photographers, designers, and fellow curators — welcome.

---

<p align="center">
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers"><img src="https://img.shields.io/badge/⭐_Star_if_this_helped-ff4785?style=for-the-badge" alt="Star"></a>
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection/fork"><img src="https://img.shields.io/badge/🍴_Fork_the_museum-24292f?style=for-the-badge" alt="Fork"></a>
</p>

---

### Collection highlights — trophy case

| Trophy | Holder |
|--------|--------|
| Largest theme | `黑猫的野望壁纸包` (734.7 MiB, 190 images) |
| Most versatile year | `2025 Wallpaper` (209 images, DM/LM pairs, Mac masters, F1) |
| Current growth engine | `2026 Wallpaper` (221 images, 511.5 MiB) |
| Newest automotive drop | `BugattiDestrier` (33 Bugatti wallpapers) |
| Most “premium device” | `Apple Park` (9× HEIC architectural) |
| Highest native resolution | `macOS-Collections` (6K, up to 6106×4512) |
| Most “wow, that is real space” | `Phone Wallpapers` (22 Artemis II mission wallpapers) |
| Deepest game lore | `2021 Wallpaper` (Cyberpunk corporate factions) |

---

**Last updated:** October 28, 2026 · **Version:** v12.0 Flat Layout Edition · **Release:** v5.0.0

**Discoverability tags:** `wallpaper` `wallpapers` `4k-wallpaper` `ultrawide` `macos` `unsplash` `cyberpunk` `anime-wallpaper` `nasa` `curated` `desktop-background`

---

---

## 中文

<a id="中文"></a>

<p align="center">
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers"><img src="https://img.shields.io/badge/⭐_Star_收藏-ff4785?style=for-the-badge&logo=github" alt="Star"></a>
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection/fork"><img src="https://img.shields.io/badge/🍴_Fork_到自己账号-24292f?style=for-the-badge&logo=github" alt="Fork"></a>
</p>

### 你的桌面，值得比「搜索结果第一张」更好

大多数壁纸仓库只是随机下载的堆叠——文件名混乱、分辨率重复、没有脉络。**The Wallpaper Collection** 恰恰相反：自 **2018** 年起持续维护的**个人壁纸博物馆**，按**年份**与**主题**编排成 **28 个顶层文件夹**，每个文件夹只做一件事——被你直接选中：**一级目录，图片全部平铺在里面**。

克隆一次。按心情、设备或年代浏览。不必每周再在 Unsplash 里翻同一批标签。

**若这份仓库帮你省下了搜索时间 — 请 [点个 Star](https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers)，让更多人发现它。**

---

### 30 秒上手

| 操作 | 说明 |
|------|------|
| **收藏** | [**Star**](https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers) — 关注更新，提高仓库曝光 |
| **拥有副本** | [**Fork**](https://github.com/MilesCorporate/The-Wallpaper-Collection/fork) — 完整备份到你自己的 GitHub |
| **本地使用** | 克隆（媒体文件约 5.9 GiB，历史已含在克隆体积内） |
| **macOS 使用** | 系统设置 → 墙纸 → 添加文件夹… → 任选一个顶层文件夹 |

```bash
git clone https://github.com/MilesCorporate/The-Wallpaper-Collection.git
# 或浅克隆：git clone --depth 1 https://github.com/MilesCorporate/The-Wallpaper-Collection.git
```

仓库地址：[github.com/MilesCorporate/The-Wallpaper-Collection](https://github.com/MilesCorporate/The-Wallpaper-Collection)

---

### 扁平目录 — 为什么只有一层

macOS 的墙纸面板只读取**你选中的那一层文件夹**，不会递归进子文件夹。选中一个「里面只有文件夹」的目录，等于选中一个空相册。所以本仓库的规则很简单：

```
The-Wallpaper-Collection/
├── 2018-2020 Wallpaper/   ← 603 张，直接平铺
├── 2021 Wallpaper/        ← 351 张图片 + 18 个视频
├── 2022 Wallpaper/        ← 151 张
├── …                      ← 其余同理
├── Ultrawide Wallpapers/  ← 188 张
├── Phone Wallpapers/      ← 173 张
└── README.md
```

**规则：`文件夹/` 里只有图片，永远不再套文件夹。**

- **28 个顶层文件夹，一级到底，没有例外。**
- **每个文件夹都是一个可直接使用的壁纸相册**——22 张或 603 张都行，macOS 认的就是这个单元。
- **命令行也变简单了：** 不需要 `**` 通配和 `-maxdepth`，`ls "Ultrawide Wallpapers"` 就是全部。

**在 macOS 上 20 秒接入：**

1. **系统设置 → 墙纸 → 添加文件夹…**
2. 选一个文件夹，例如 `~/Pictures/The-Wallpaper-Collection/2026 Wallpaper`
3. 完成——该文件夹里的每张图都会进入轮换，不会因为藏在子目录里被跳过。

想一次性把整个博物馆加进来？添加仓库根目录即可，macOS 会把 28 个顶层文件夹分别作为相册列出，每一个都已经是扁平的。

*Windows 的「幻灯片放映 → 浏览」、GNOME / KDE 的幻灯片插件、Wallpaper Engine 的文件夹监控，同样都只读一层——所以这样的结构在哪都好用。*

<details>
<summary><strong>2026-10-28 扁平化改了什么</strong></summary>

| 变更 | 明细 |
|---|---|
| **文件上移** | **804 个**文件从 **68 个嵌套目录**移入所属顶层文件夹（`Phone Wallpapers/iOS/…`、`2021/CyberPunk 2077/Arasaka/`、`Windows11/Wallpaper/ThemeA/`、`Social Assets/The Crew 2/01_SCREENSHOTS/` 等） |
| **删除目录** | **78 个** —— 上面 68 个，加上 10 个只装文件夹的中间层；包括深达两级的 `Windows11-DefaultWallpaper/4K/Wallpaper/Windows/` |
| **合并重复** | **7 张**逐字节相同的 Surface 图片（2018 年 10 月活动合集与 27 张 Surface 合集里各有一份） |
| **丢失内容** | **无**——剩下的每张图都唯一 |
| **子主题信息** | 保留在文件名里（`Cyberpunk2077_Wallpapers_Arasaka_3840x2160_EN.webp`、`Surface Laptop 2 - Cobalt.jpg`、`0 - Aura #1 - 1920x1080.webp`） |

</details>

---

### 入门精选包（不用一次翻完 28 个文件夹）

| 套装 | 先看这些 | 适合 |
|------|----------|------|
| **新机装机** | `2026 Wallpaper` → `2025 Wallpaper` → `macOS-Collections` → `Apple Park` | 4K/5K/6K、Mac 或 Windows |
| **超宽 / 赛车** | `Ultrawide Wallpapers` → `2026 Wallpaper`（F1、豪车） | 21:9 / 32:9 |
| **氛围 / 同人** | `黑猫的野望壁纸包` · `2021 Wallpaper`（赛博朋克） · `Phone Wallpapers`（Artemis II） | 动漫、赛博朋克、NASA |
| **豪车 / 工业设计** | `BugattiDestrier` · `2026 Wallpaper`（搜 F1、Audi、Mercedes-AMG） | 超跑、赛车、汽车设计 |

---

### 为什么值得 Star / Fork

- **Star**：免费书签、接收更新、帮项目在 GitHub 上被更多人看见 → [**点此 Star**](https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers)  
- **Fork**：约 5.9 GiB 媒体文件 / 2,688 张图片与 18 个视频落到你的账号；Git 历史会增加容量，可删减定制并 PR 贡献壁纸 → [**点此 Fork**](https://github.com/MilesCorporate/The-Wallpaper-Collection/fork)

分享链接：`https://github.com/MilesCorporate/The-Wallpaper-Collection`

---

### 为什么这份收藏不一样

| 你得到什么 | 意义 |
|------------|------|
| **策展，而非爬虫** | 28 个顶层文件夹各有存在理由——年度档案、品牌专题或风格专线 |
| **扁平，而非套娃** | 只有一级目录，macOS 墙纸面板、Windows 幻灯片和任何文件选择器都能直接看到图片 |
| **分辨率到位** | 从 1080p 经典到 **4K / 5K / 6K / 8K** 与 **超宽屏（3440×1440+）**，含 F1、豪车与 Mac 级大图 |
| **设备友好** | iPad（YTECHB）、iPhone 12 官方、超宽合集、深浅色**配对** macOS 渐变 |
| **文化与工艺** | 赛博朋克公司阵营、动漫大作（**190** 张）、Apple Park **HEIC** 园区、**Artemis II** 绕月视角与 **Bugatti** 专题 |
| **仍在生长** | 仅 **2026** 文件夹就达 **511.5 MiB / 221 张**——活跃更新线，不是过时快照 |

---

### 数据一览

| 指标 | 数值 |
|------|------|
| **时间跨度** | 2018 → 2026 |
| **顶层分类** | **28** 个文件夹 |
| **目录深度** | **1 级**——没有子文件夹 |
| **工作区媒体容量** | **约 5.9 GiB**（图片与视频） |
| **图片数量** | **2,688** 张（JPG / WebP / HEIC / HEIF — PNG 已转 WebP） |
| **视频数量** | **18** 个（MOV，iPhone 12 Live，位于 `2021 Wallpaper`） |
| **分辨率** | 1080p 至 **8K** |
| **最大主题包** | `黑猫的野望壁纸包` — **734.7 MiB**，**190** 张 |
| **最新主力** | `2026 Wallpaper` — **511.5 MiB**，**221** 张 |
| **全新专题** | `BugattiDestrier` — **33** 张 BUGATTI Solitaire Destrier 壁纸 |

---

### 适合谁

- **桌面发烧友** — 超宽、多屏、4K/5K，需要真正能铺满画面的文件  
- **Mac 用户** — HEIC 园区摄影、`macOS-Collections` 6K 原图、macOS 风格渐变、iPhone/iPad 官方系列  
- **玩家与科幻迷** — 赛博朋克阵营、The Crew 2、ROG/MSI 年代感  
- **摄影爱好者** — 历年 Unsplash 精选、Getty、风光与星空  
- **动漫插画党** — 全库最大的独立主题包  
- **豪车与设计党** — BUGATTI Solitaire Destrier、F1、Audi RS、Mercedes-AMG 视觉线
- **航天迷** — **NASA Artemis II** 地月猎户座视角
- **收藏党** — 按年归档，记录「那一年什么值得留下」  

---

### 目录逻辑

```
The-Wallpaper-Collection/
├── 📅 年度系列（2018–2026）  ← 时间轴：每年流行什么
├── 🎨 主题典藏               ← 单点深挖：品牌、游戏、材质、NASA、汽车设计
├── 🖥️ Ultrawide Wallpapers   ← 21:9 / 32:9 / 全景
├── 📱 Phone Wallpapers       ← 所有竖屏手机壁纸
├── 📣 Social Assets          ← 头像、社交横幅、品牌物料
└── README.md
```

**年度文件夹** = 品味编年史。**主题文件夹** = 一种审美的全集。**全部只有一级，图片直接平铺。**

---

### 28 个文件夹一览

| 文件夹 | 图片 | 体积 | 一句话 |
|--------|-----:|-----:|--------|
| `2018-2020 Wallpaper` | 603 | 1018.8 MiB | 奠基时代：Fluent、Surface、ROG、MSI、Windows |
| `2021 Wallpaper` | 351 + 18 视频 | 817.4 MiB | 游戏复兴：赛博朋克阵营、iPhone 12 Live |
| `2022 Wallpaper` | 151 | 293.1 MiB | 重质不重量 |
| `2023 Wallpaper` | 104 | 226.9 MiB | 现代简约 |
| `2024 Wallpaper` | 89 | 225.4 MiB | 多元融合 |
| `2025 Wallpaper` | 209 | 643.0 MiB | 进化之年，最全能 |
| `2026 Wallpaper` | 221 | 511.5 MiB | 当前旗舰 |
| `Ultrawide Wallpapers` | 188 | 489.9 MiB | 21:9 / 32:9 / 全景，一张专辑 |
| `Phone Wallpapers` | 173 | 89.8 MiB | iOS / Android / Artemis II / 杂项竖屏 |
| `Social Assets` | 125 | 21.2 MiB | 头像、横幅、The Crew 2 物料 |
| `黑猫的野望壁纸包` | 190 | 734.7 MiB | 动漫主场，全库最大 |
| `macOS-Collections` | 16 | 209.1 MiB | 苹果 6K 收藏图（最高 6106×4512） |
| `BugattiDestrier` | 33 | 141.4 MiB | BUGATTI 超跑专题 |
| `Apple Park` | 9 | 129.3 MiB | 苹果园区 HEIC 建筑摄影 |
| `Stokes` | 10 | 95.8 MiB | 艺术感插画 |
| `Unsplash` | 20 | 77.4 MiB | 专业摄影 |
| `CyberPunk Wallpaper` | 29 | 70.3 MiB | 霓虹反乌托邦补充 |
| `Texture` | 11 | 68.0 MiB | 材质 |
| `MKBHDWallpapers` | 27 | 38.9 MiB | 科技美学、8K 多边形 |
| `CrystalWallpapers` | 22 | 32.1 MiB | 水晶 / 折射 |
| `Windows11-DefaultWallpaper` | 36 | 27.7 MiB | Windows 11 官方主题 A–D / 4K |
| `Facets` | 5 | 13.0 MiB | 多边形 / 几何抽象 |
| `GettyImages` | 20 | 10.0 MiB | Getty 精选 |
| `wallpapers_pack` | 3 | 8.6 MiB | 杂选 |
| `Mac Internal` | 14 | 4.8 MiB | Mac 内部设计语言 |
| `Look Back` | 7 | 2.5 MiB | 复古 |
| `Aura Wallpaper` | 21 | 990.4 KiB | Aura 渐变体系（桌面尺寸） |
| `LinksPhotograph` | 1 | 160.8 KiB | 摄影参考存档 |

---

### 年度系列 — 品味时间线

- **`2018-2020 Wallpaper` · 1018.8 MiB · 603 张** — 奠基时代：Fluent Design、Surface、MSI、ROG、Windows 官方、2018 活动合集。套装已全部平铺，靠文件名区分（`Surface Laptop 2 - Cobalt.jpg`、`ROG_wallpaper_…`）。
- **`2021 Wallpaper` · 817.4 MiB · 351 张 + 18 个视频** — 游戏复兴：赛博朋克**荒坂 / 康陶 / 军用科技 / 创伤小组**、Hello、Holiday、Yosemite，以及 iPhone 12 Live（18 个 MOV）。
- **`2022 Wallpaper` · 293.1 MiB · 151 张** — 重质不重量，筛选更严。
- **`2023 Wallpaper` · 226.9 MiB · 104 张** — 现代简约，适合专注办公。
- **`2024 Wallpaper` · 225.4 MiB · 89 张** — 多元融合，通向 AI 与超宽屏时代。
- **`2025 Wallpaper` · 643.0 MiB · 209 张** — 进化之年：深浅色 4K 配对渐变、Mac 原生大图、YTECHB iPad、AI 艺术、F1/豪车。**换新机首选。**
- **`2026 Wallpaper` · 511.5 MiB · 221 张** — 当前旗舰：Unsplash 2026、自然与野生动物、F1/奔驰/奥迪宽屏、macOS 经典与新渐变。**本月只同步这一个文件夹也值。**

---

### 主题典藏 — 执念，打包好了

| 文件夹 | 容量 | 卖点 |
|--------|------|------|
| `黑猫的野望壁纸包` | 734.7 MiB · 190 张 | 全库最大 — 动漫/宅文化主场 |
| `macOS-Collections` | 209.1 MiB · 16 张 | 苹果官方 6K 收藏图，最高 6106×4512 |
| `BugattiDestrier` | 141.4 MiB · 33 张 | BUGATTI Solitaire Destrier 超跑视觉 |
| `Apple Park` | 129.3 MiB · 9 张 HEIC | 苹果园区建筑摄影，Retina 绝配 |
| `Phone Wallpapers` | 89.8 MiB · 173 张 | 手机竖屏专线 — iPhone 12、Android、Artemis II、杂项 |
| `Ultrawide Wallpapers` | 489.9 MiB · 188 张 | 21:9 / 32:9 / 全景，全部 ≥ 2.05:1 |
| `Social Assets` | 21.2 MiB · 125 张 | 头像、社交横幅、育碧 The Crew 2 物料 |
| `MKBHDWallpapers` | 38.9 MiB · 27 张 | 科技美学、8K 多边形、Bleeding Edge |
| `CrystalWallpapers` | 32.1 MiB · 22 张 | 水晶/折射合集 |
| `CyberPunk Wallpaper` | 70.3 MiB · 29 张 | 霓虹反乌托邦独立补充 |
| `Aura Wallpaper` | 990.4 KiB · 21 张 | Aura 渐变体系（桌面尺寸） |
| `Texture` / `Stokes` / `Facets` | 68.0 / 95.8 / 13.0 MiB | 材质 · 艺术 · 几何 |
| `Unsplash` / `GettyImages` / `LinksPhotograph` | 77.4 / 10.0 MiB / 160.8 KiB | 专业摄影通道 |
| `Mac Internal` / `Windows11-DefaultWallpaper` | 4.8 / 27.7 MiB | 平台原生气质 |
| `Look Back` / `wallpapers_pack` | 2.5 / 8.6 MiB | 复古与杂选 |

---

### 使用建议（按设备）

| 设备 | 推荐入口 |
|------|----------|
| **4K / 5K / 6K** | `2025` + `2026` → `MKBHD` → `macOS-Collections` → `Apple Park` |
| **超宽屏** | `Ultrawide Wallpapers`（188 张，一张专辑） |
| **1080p** | `Texture`、`Stokes`、`2022–2023` |
| **iPad** | `2025 Wallpaper`（YTECHB）、`Phone Wallpapers` 竖屏图 |
| **iPhone** | `Phone Wallpapers`；Live 动态壁纸见 `2021 Wallpaper`（18 个 MOV） |
| **WallpaperEngine** | Steam 安装；动态壁纸建议独显 |

**HEIC / HEIF（Windows）：** 安装 HEIF 扩展，或用 ImageMagick / GIMP / 在线工具转换。

---

### 工具

| 脚本 | 作用 |
|------|------|
| `python3 scripts/stats.py` | 按文件夹统计图片/视频数量与体积；`--check` 校验本文数字**并检查是否又长出子文件夹**，`--write` 自动修正 |
| `python3 scripts/build_gallery.py` | 本地生成带懒加载缩略图的 `gallery/index.html`（已 gitignore） |
| `bash scripts/heic2jpg.sh` | 批量把 HEIC/HEIF 转成同名 JPG，方便 Windows / Linux |

---

### 版权说明

本仓库为**个人策展收藏**，供欣赏与参考。

- 图片权利归原作者与权利方所有  
- 以**个人桌面使用**为主  
- **商业使用**须另行取得授权（Getty、品牌方、NASA 媒体政策等）  
- 请勿将整库商业化再分发  
- Unsplash 遵循 [Unsplash License](https://unsplash.com/license)  

版权问题请通过 GitHub Issues 联系。

---

### 更新记录

| 时间 | 变更 |
|------|------|
| **2026 年 10 月 28 日** | **扁平化改版。** 28 个文件夹全部收成一级：**804 个文件**上移、**78 个**子目录删除、**7 张**逐字节重复图合并（2018 活动合集 / Surface 合集）；补充 `macOS-Collections` 说明。现为 **28 个文件夹 / 2,688 张 / 18 个视频 / ~5.9 GiB**，可直接在「系统设置 → 墙纸 → 添加文件夹…」里使用 |
| **2026 年 10 月 21 日** | 重新策展：手机壁纸 → `Phone Wallpapers/`，头像/物料 → `Social Assets/`，超宽 → `Ultrawide Wallpapers/`；删除逐字节重复的 `Year of 2021`；PNG 全部转 WebP q92；当时为 **28 个文件夹 / 2,685 张 / 18 个视频 / ~5.8 GiB**，`.git` 从 8.9 GB 降到 5.7 GB — 已有的 clone/fork 请看 **[MIGRATION.md](MIGRATION.md)** |
| **2026 年 10 月 8 日** | 按工作区复核统计：**27 个文件夹**、**3,079 张图片**、**36 个视频**，媒体约 **10.2 GiB**；`2026 Wallpaper` 为 **272 张 / 约 963 MiB** |
| **2026 年 8 月 7 日** | README 数据刷新：约 18 GB、**3,033 张**、**26 个文件夹**；新增 **`BugattiDestrier`**（33 张 / 141 MB） |
| **2026 年 6 月** | README v10 展示版；此前数据快照（2,918 张、25 类） |
| **2026** | 较早快照：`2026 Wallpaper` 为 **242 张 / 831 MB**；新增 **`Artemis II`**（22 张） |
| **2025** | **252 张 / 1.1 GB** — AI、iPad、超宽、macOS 深浅配对、F1/豪车 |
| **2021** | 赛博朋克阵营高峰；iPhone 12 官方 |
| **2018** | 收藏库创立 |

---

### 联系与贡献

**想让收藏库持续变大？** Star、Fork、提 Issue、发 PR — 开源档案馆就是这样长大的。

| 方式 | 链接 |
|------|------|
| **Star** | [点 Star](https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers) |
| **Fork** | [Fork 到自己](https://github.com/MilesCorporate/The-Wallpaper-Collection/fork) |
| **Issue** | [提交建议 / 版权](https://github.com/MilesCorporate/The-Wallpaper-Collection/issues/new) |

欢迎推荐值得单独成夹的壁纸、提交新专题、改进文档与中文说明。

**唯一需要注意的规则：** 新图请加进现有顶层文件夹，或提议一个**新的顶层文件夹**——不要再套子文件夹。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

<p align="center">
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection/stargazers"><img src="https://img.shields.io/badge/⭐_有帮助就点Star-ff4785?style=for-the-badge" alt="Star"></a>
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection/fork"><img src="https://img.shields.io/badge/🍴_Fork整个博物馆-24292f?style=for-the-badge" alt="Fork"></a>
</p>

---

### 收藏奖杯榜

| 奖项 | 得主 |
|------|------|
| 最大主题 | `黑猫的野望壁纸包` |
| 最全能单年 | `2025 Wallpaper` |
| 当前增长引擎 | `2026 Wallpaper` |
| 最新汽车专题 | `BugattiDestrier`（33 张 BUGATTI 壁纸） |
| 最 premium 设备向 | `Apple Park`（HEIC） |
| 最高原生分辨率 | `macOS-Collections`（6K，最高 6106×4512） |
| 最震撼真实太空 | `Phone Wallpapers`（22 张 NASA Artemis II 壁纸） |
| 最深游戏叙事 | `2021 Wallpaper`（赛博朋克公司阵营） |

---

**最后更新：** 2026 年 10 月 28 日 · **版本：** v12.0 Flat Layout Edition · **Release：** v5.0.0

<p align="center">
  <strong>⭐ Star · 🍴 Fork · 🔗 Share</strong><br>
  <a href="https://github.com/MilesCorporate/The-Wallpaper-Collection">MilesCorporate/The-Wallpaper-Collection</a>
</p>

*Eight years. Twenty-eight flat shelves. One clone — star it if it earns a place on your desktop.*

*八年积累 · 二十八个扁平文件夹 · 好用的话请 Star —— 你的一个点击，是下一个用户找到它的捷径。*
