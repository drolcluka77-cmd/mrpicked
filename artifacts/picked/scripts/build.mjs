// Production build: the site is plain static HTML, so the build copies it as-is.
import { cpSync, rmSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";

const site = fileURLToPath(new URL("../site/", import.meta.url));
const out = fileURLToPath(new URL("../dist/public/", import.meta.url));
rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });
cpSync(site, out, { recursive: true });
console.log("Copied static site to dist/public");
