#!/usr/bin/env python3
"""
Convert .txt content files into simple HTML pages.

Usage:
  python tools/convert_txt_to_html.py --root . --out same
  python tools/convert_txt_to_html.py --root . --out out_dir

Notes:
- This script is intentionally simple and safe for static hosting.
- It will create/overwrite .html files next to each .txt file unless --out is different.
"""
from __future__ import annotations
import argparse, html, pathlib, re, datetime

def title_from_path(p: pathlib.Path) -> str:
    name = p.stem.replace('-', ' ').replace('_',' ').strip()
    return name[:1].upper() + name[1:] if name else "Document"

def wrap_html(title: str, body: str) -> str:
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(title)}"/>
  <style>
    body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif; margin:40px auto; max-width:860px; padding:0 16px; line-height:1.7;}}
    pre{{white-space:pre-wrap; word-break:break-word; background:#f6f6f6; padding:16px; border-radius:12px;}}
    a{{color:inherit;}}
    .meta{{opacity:.7; font-size:14px; margin:0 0 18px;}}
  </style>
</head>
<body>
  <div class="meta">Generated {now}</div>
  <h1>{html.escape(title)}</h1>
  <pre>{html.escape(body)}</pre>
</body>
</html>"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Site root to scan")
    ap.add_argument("--out", default="same", help="'same' or an output directory")
    ap.add_argument("--glob", default="**/*.txt", help="Glob pattern for txt files")
    args = ap.parse_args()

    root = pathlib.Path(args.root).resolve()
    out_mode = args.out

    txt_files = [p for p in root.glob(args.glob) if p.is_file()]
    if not txt_files:
        print("No .txt files found.")
        return

    for txt in txt_files:
        rel = txt.relative_to(root)
        title = title_from_path(txt)
        body = txt.read_text(encoding="utf-8", errors="ignore")
        html_doc = wrap_html(title, body)

        if out_mode == "same":
            out_path = txt.with_suffix(".html")
        else:
            out_dir = pathlib.Path(out_mode).resolve()
            out_path = (out_dir / rel).with_suffix(".html")
            out_path.parent.mkdir(parents=True, exist_ok=True)

        out_path.write_text(html_doc, encoding="utf-8")
        print("Wrote", out_path)

if __name__ == "__main__":
    main()
