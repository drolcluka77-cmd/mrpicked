# Mr. Picked site generator

The website in `../site/` is static HTML generated from the copy in this folder.
Run from the repository root (no dependencies, Python 3 only):

    python3 artifacts/picked/generator/build.py

- `copy.json` — base copy (hospitality wording), package names, prices and add-ons.
- `content.py` — generic main-page copy (6 languages), industry pages (EN + SL), ROI defaults, page titles.
- `build.py` — writes every `index.html` and `sitemap.xml` into `../site/`, plus the video texts and form messages.

Static files in `../site/` (`assets/app.js`, `assets/style.css`, icons, `llms.txt`, `robots.txt`) are edited directly.
Never edit the generated `index.html` files by hand: change the generator and rebuild.

The forms POST to `/api/report-requests` and the video loads from `/api/media/…`, both served by `artifacts/api-server`.
