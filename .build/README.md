# Mr. Picked site generator

The pages are static HTML generated from the copy in this folder.

    python3 .build/build.py .build/copy.json .

- `copy.json` — base copy (hospitality wording), package names, prices and add-ons.
- `content.py` — generic main-page copy (6 languages), industry pages (EN + SL), ROI defaults, page titles.
- `build.py` — writes every `index.html` and `sitemap.xml`.

Static files (`assets/`, icons, `llms.txt`, `robots.txt`) are edited directly.
