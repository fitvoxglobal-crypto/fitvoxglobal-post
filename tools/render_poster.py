#!/usr/bin/env python3
"""Render a Fitvox poster artboard (.dc.html) to a 1080x1350 JPEG for Instagram.

Usage: python3 tools/render_poster.py <poster.dc.html> <out.jpg>

Needs: python3 + playwright, /usr/bin/google-chrome, npm (for the two fonts).
The logo comes from assets/logo-f.png in this repo.
"""
import os
import re
import subprocess
import sys
import tarfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(ROOT, "assets", "logo-f.png")
FONT_DIR = "/tmp/fitvox-fonts"
ACCENT = "#86D6AB"


def ensure_font(package, woff2_name):
    target = os.path.join(FONT_DIR, package.split("/")[-1])
    path = os.path.join(target, "package", "files", woff2_name)
    if os.path.exists(path):
        return path
    os.makedirs(target, exist_ok=True)
    out = subprocess.run(["npm", "pack", package], cwd=target, capture_output=True, text=True, check=True)
    tgz = os.path.join(target, out.stdout.strip().splitlines()[-1])
    with tarfile.open(tgz) as t:
        t.extractall(target)
    return path


def main(src, out_jpg):
    html = open(src, encoding="utf-8").read()
    m = re.search(r"<x-dc>.*?</helmet>\s*(<div style=.*)</x-dc>", html, re.S)
    if not m:
        sys.exit("could not find the poster markup in " + src)
    inner = m.group(1).replace("{{accent}}", ACCENT)
    inner = re.sub(r'src="/_blob/[0-9a-f]+"', 'src="file://%s"' % LOGO, inner)
    jak = ensure_font("@fontsource-variable/plus-jakarta-sans", "plus-jakarta-sans-latin-wght-normal.woff2")
    mon = ensure_font("@fontsource-variable/montserrat", "montserrat-latin-wght-italic.woff2")
    page = (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'><style>"
        "@font-face{font-family:'Plus Jakarta Sans';src:url('file://%s') format('woff2');font-weight:200 800}"
        "@font-face{font-family:'Montserrat';font-style:italic;src:url('file://%s') format('woff2');font-weight:100 900}"
        "body{margin:0}</style></head><body>%s</body></html>" % (jak, mon, inner)
    )
    tmp = "/tmp/fitvox-poster.html"
    open(tmp, "w", encoding="utf-8").write(page)

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome",
                              args=["--no-sandbox", "--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        pg.goto("file://" + tmp)
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(500)
        pg.screenshot(path=out_jpg, type="jpeg", quality=95,
                      clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
        b.close()
    print("rendered", out_jpg)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
