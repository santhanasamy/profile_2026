# /// script
# requires-python = ">=3.10"
# dependencies = ["markdown>=3.5", "pyyaml>=6"]
# ///
"""Local preview for a GitHub Pages (Jekyll) site without installing Jekyll.

Renders a Markdown page through the site's own layout, includes, and theme CSS,
then optionally serves it and/or prints it to PDF with headless Chrome.

It is an approximation of the GitHub Pages build: Python-Markdown is used
instead of kramdown, and only the Liquid tags common in simple layouts are
supported ({{ content }}, {{ site.* | default: ... }}, {{ page.* }},
{% include file %}, {% seo %}). Unknown Liquid tags are removed.

Usage (from anywhere):
    uv run tools/preview.py                       # build .preview/index.html
    uv run tools/preview.py --serve --open        # build, serve, open browser
    uv run tools/preview.py --pdf                 # also write .preview/index.pdf
    uv run tools/preview.py --site ~/Ws/other_site --page about.md
"""

from __future__ import annotations

import argparse
import functools
import http.server
import re
import shutil
import subprocess
import sys
import threading
import webbrowser
from pathlib import Path

import markdown
import yaml

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LIQUID_VAR = re.compile(r"\{\{\s*(.*?)\s*\}\}", re.DOTALL)
LIQUID_TAG = re.compile(r"\{%\s*(.*?)\s*%\}", re.DOTALL)
STYLESHEET = re.compile(r'<link[^>]+href="\{\{[^"]*assets/css/style\.css[^"]*\}\}"[^>]*>')

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "google-chrome",
    "chromium",
    "chromium-browser",
    "msedge",
]


def split_front_matter(text: str) -> tuple[dict, str]:
    m = FRONT_MATTER.match(text)
    if not m:
        return {}, text
    return (yaml.safe_load(m.group(1)) or {}), text[m.end():]


def theme_css_url(config: dict) -> str | None:
    """pages-themes/slate@v0.2.0 -> https://pages-themes.github.io/slate/assets/css/style.css"""
    theme = config.get("remote_theme") or config.get("theme")
    if not theme:
        return None
    name = str(theme).split("@")[0].split("/")[-1].removeprefix("jekyll-theme-")
    return f"https://pages-themes.github.io/{name}/assets/css/style.css"


def lookup(path: str, scope: dict) -> object:
    cur: object = scope
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def render_var(expr: str, scope: dict) -> str:
    parts = [p.strip() for p in expr.split("|")]
    value = None
    head = parts[0]
    if head.startswith(("'", '"')):
        value = head.strip("'\"")
    else:
        value = lookup(head, scope)
    for flt in parts[1:]:
        if flt.startswith("default:") and not value:
            arg = flt.split(":", 1)[1].strip()
            value = arg.strip("'\"") if arg[:1] in "'\"" else lookup(arg, scope)
    return "" if value is None else str(value)


def render_liquid(template: str, scope: dict, includes_dir: Path) -> str:
    def tag(m: re.Match) -> str:
        words = m.group(1).split()
        if not words:
            return ""
        if words[0] == "include" and len(words) > 1:
            inc = includes_dir / words[1]
            return render_liquid(inc.read_text(), scope, includes_dir) if inc.exists() else ""
        if words[0] == "seo":
            title = scope["page"].get("title") or scope["site"].get("title") or ""
            return f"<title>{title}</title>"
        return ""

    out = LIQUID_TAG.sub(tag, template)
    return LIQUID_VAR.sub(lambda m: render_var(m.group(1), scope), out)


def build(site: Path, page: Path, out_dir: Path) -> Path:
    config = yaml.safe_load((site / "_config.yml").read_text()) if (site / "_config.yml").exists() else {}
    config = config or {}
    meta, body = split_front_matter(page.read_text())
    html_body = markdown.markdown(body, extensions=["tables", "attr_list", "md_in_html", "fenced_code"])

    layout_name = meta.get("layout", "default")
    layout = site / "_layouts" / f"{layout_name}.html"
    css = theme_css_url(config)
    if layout.exists():
        template = layout.read_text()
        link = f'<link rel="stylesheet" href="{css}">' if css else ""
        template = STYLESHEET.sub(link, template)
    else:
        link = f'<link rel="stylesheet" href="{css}">' if css else ""
        template = ("<!doctype html><html><head><meta charset='utf-8'>" + link +
                    "{% seo %}{% include head-custom.html %}</head><body>{{ content }}</body></html>")

    scope = {"site": config, "page": meta, "content": html_body}
    html = render_liquid(template, scope, site / "_includes")

    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / (page.stem + ".html")
    out.write_text(html)
    return out


def find_chrome() -> str | None:
    for c in CHROME_CANDIDATES:
        if Path(c).exists() or shutil.which(c):
            return c if Path(c).exists() else shutil.which(c)
    return None


def print_pdf(url: str, pdf: Path) -> bool:
    chrome = find_chrome()
    if not chrome:
        print("PDF skipped: Chrome/Chromium/Edge not found.", file=sys.stderr)
        return False
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", url],
                   check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return pdf.exists()


def serve(directory: Path, port: int) -> http.server.ThreadingHTTPServer:
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args: object) -> None:
            pass

    handler = functools.partial(QuietHandler, directory=str(directory))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def main() -> int:
    default_site = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description="Preview a GitHub Pages (Jekyll) site locally.")
    ap.add_argument("--site", type=Path, default=default_site, help="site root (default: this repo)")
    ap.add_argument("--page", default="index.md", help="page to render, relative to --site")
    ap.add_argument("--out", type=Path, default=None, help="output dir (default: <site>/.preview)")
    ap.add_argument("--serve", action="store_true", help="serve the output over http://127.0.0.1:PORT")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--open", action="store_true", help="open the page in the default browser")
    ap.add_argument("--pdf", action="store_true", help="print the page to PDF with headless Chrome")
    args = ap.parse_args()

    site = args.site.expanduser().resolve()
    page = site / args.page
    if not page.exists():
        print(f"Page not found: {page}", file=sys.stderr)
        return 1
    out_dir = (args.out or site / ".preview").expanduser().resolve()

    out = build(site, page, out_dir)
    print(f"Built   {out}")

    httpd = None
    if args.serve or args.pdf:
        try:
            httpd = serve(out_dir, args.port)
        except OSError:
            print(f"Port {args.port} is busy; assuming a preview server is already running there.")
    url = f"http://127.0.0.1:{args.port}/{out.name}"

    if args.pdf:
        pdf = out.with_suffix(".pdf")
        if print_pdf(url, pdf):
            print(f"PDF     {pdf}")
    if args.open:
        webbrowser.open(url if (args.serve or httpd) else out.as_uri())
    if args.serve:
        print(f"Serving {url}  (Ctrl+C to stop; rerun the build in another terminal after edits)")
        try:
            threading.Event().wait()
        except KeyboardInterrupt:
            pass
    if httpd:
        httpd.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
