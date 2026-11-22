# Mr. Picked

Website and free-report API for Mr. Picked (mrpicked.eu): AI search visibility (GEO) and local SEO for local businesses, in 6 languages.

**GitHub `main` is the source of truth.** Always Pull before editing, never force-push, never use "Push branch as origin/main" over newer GitHub commits.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- Required env: `DATABASE_URL` — Postgres connection string

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

- `artifacts/picked/site/` — the live website: static HTML pages (EN, SL, HR, IT, DE, HU + industry pages in EN/SL), `assets/app.js`, `assets/style.css`, icons, `llms.txt`, `robots.txt`, `sitemap.xml`.
- `artifacts/picked/generator/` — Python generator for every `index.html` and the sitemap. Edit copy here, then run `python3 artifacts/picked/generator/build.py`. Do not hand-edit generated HTML.
- `artifacts/picked/scripts/` — `serve.mjs` (dev server) and `build.mjs` (copies `site/` to `dist/public` for deploy).
- `artifacts/api-server/` — Express API: `POST /api/report-requests` (form → email to info@mrpicked.eu + confirmation to the visitor), `GET /api/media/:filename` (explainer video from object storage).
- `lib/api-spec/openapi.yaml` — API contract.

## Architecture decisions

- The website is plain static HTML (all text in the HTML) for SEO/GEO: AI crawlers and Google read it without running JavaScript. Do not rewrite it into React or a client-rendered SPA.
- Every language and industry page is a real folder (`/sl/`, `/sl/avtovleka/` …), so there is no SPA rewrite in production.
- Default language comes from `navigator.language` (English fallback), remembered in localStorage `mp-lang`. No IP/VPN detection.
- Form requests carry a `requestId` reused on retry, so double clicks do not send two emails.

## Product

Landing pages with live AI demo, pricing builder (Visible 390 €, Recommended 690 €, Concierge 990 € + 490 € setup, add-ons), ROI calculator, explainer video, free AI report form.

## User preferences

_Populate as you build — explicit user instructions worth remembering across sessions._

## Gotchas

_Populate as you build — sharp edges, "always run X before Y" rules._

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
