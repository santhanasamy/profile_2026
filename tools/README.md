# Local preview

`tools/preview.py` previews this GitHub Pages site locally, without installing Jekyll or Ruby.

It renders a Markdown page using the site's own files:
- the layout from `_layouts/`
- includes from `_includes/`, so the custom CSS and print rules in `head-custom.html` apply
- the theme stylesheet named in `_config.yml`

It can also serve the page on localhost and print it to PDF, so you can check the print layout.

## Requirements
- [uv](https://docs.astral.sh/uv/). It installs the script's Python dependencies (`markdown`, `pyyaml`) automatically on first run.
- Optional: Google Chrome, Chromium or Microsoft Edge, for `--pdf`.

## Usage
Run from the repo root:

```bash
uv run tools/preview.py                 # build .preview/index.html
uv run tools/preview.py --serve --open  # build, serve at http://127.0.0.1:8765, open the browser
uv run tools/preview.py --pdf           # also write .preview/index.pdf (print layout)
```

To preview another branch, switch to it and build again:

```bash
git switch feature/profile_mobile_focused_11_2026
uv run tools/preview.py --pdf --open
```

You can also preview any other Jekyll / GitHub Pages site or page:

```bash
uv run tools/preview.py --site ~/Ws/another_site --page about.md --serve
```

| Option | Default | Purpose |
|---|---|---|
| `--site PATH` | this repo | Site root (the folder with `_config.yml`) |
| `--page FILE` | `index.md` | Page to render, relative to `--site` |
| `--out DIR` | `<site>/.preview` | Output folder (git-ignored) |
| `--serve` | off | Serve the output on localhost |
| `--port N` | `8765` | Port for `--serve` / `--pdf` |
| `--open` | off | Open the page in the default browser |
| `--pdf` | off | Print to `<page>.pdf` with headless Chrome |

The page doesn't refresh itself. After editing, run the build again and reload the browser tab. If `--serve` is still running in another terminal, it serves the new build automatically.

## Differences from the real GitHub Pages build
- **Markdown renderer:** Python-Markdown instead of kramdown. Tables, `{: .class}` attribute lists and `<div markdown="1">` blocks work, but small spacing differences are possible.
- **Liquid templates:** only the tags simple layouts use are supported: `{{ content }}`, `{{ site.* | default: ... }}`, `{{ page.* }}`, `{% include %}` and `{% seo %}`. Other tags are dropped.
- **Theme stylesheet:** loaded from `pages-themes.github.io`, so the first load needs internet access.

Check the live page after publishing.

`tools/` and `.preview/` are listed under `exclude` in `_config.yml`, so they are never published to the site.
