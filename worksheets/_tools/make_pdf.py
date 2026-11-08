# -*- coding: utf-8 -*-
"""A3横の紙面HTMLを、生徒用／赤刷りの2種のPDFにする。

Artifact は画面で見るためのもの。配るのは PDF。
google-chrome の headless で印刷し、pdfunite で冊子にまとめる。
"""
import io, os, re, subprocess, sys, tempfile, shutil

# google-chrome の headless はこの環境で起動しない。playwright 同梱の headless-shell を使う。
CHROME = "/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell"

_WRAP = """<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<style>html,body{margin:0}</style>
</head><body>
{body}
{teacher}
</body></html>"""

_TEACHER = '<script>document.body.classList.add("teacher");</script>'

# 印刷時はネットワークを使わない（Google Fonts を待って止まるため）。
# この環境にある日本語フォントは IPAGothic だけなので、明朝も同じ族に落とす。
_FONTS = ('<style>:root{--serif:"IPAGothic","IPA Pゴシック",sans-serif;'
          '--sans:"IPAGothic","IPA Pゴシック",sans-serif}'
          'h1,h2,h3,.hdr .ji{font-weight:700}</style>')
_LINK = re.compile(r'<link[^>]*fonts\.(?:googleapis|gstatic)\.com[^>]*>')


def _render(src_html, out_pdf, teacher, workdir):
    body = _LINK.sub("", io.open(src_html, encoding="utf-8").read()) + _FONTS
    tmp = os.path.join(workdir, os.path.basename(src_html))
    with io.open(tmp, "w", encoding="utf-8") as f:
        f.write(_WRAP.replace("{body}", body)
                     .replace("{teacher}", _TEACHER if teacher else ""))
    prof = tempfile.mkdtemp(dir=workdir)
    cmd = [CHROME, "--disable-gpu", "--no-sandbox",
           "--no-pdf-header-footer", "--virtual-time-budget=3000",
           "--disable-background-networking", "--disable-component-update",
           "--disable-default-apps", "--disable-extensions", "--disable-sync",
           "--no-first-run", "--no-default-browser-check", "--disable-dev-shm-usage",
           "--user-data-dir=" + prof,
           "--print-to-pdf=" + out_pdf, "file://" + tmp]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    if not os.path.exists(out_pdf):
        raise RuntimeError("PDF が出ませんでした: %s\n%s" % (src_html, r.stderr[-800:]))
    return out_pdf


def pages(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    n = size = "?"
    for line in out.splitlines():
        if line.startswith("Pages:"):     n = line.split()[-1]
        if line.startswith("Page size:"): size = line.split(":", 1)[1].strip()
    return n, size


def main(srcs, outdir, name):
    os.makedirs(outdir, exist_ok=True)
    work = tempfile.mkdtemp()
    try:
        made = {}
        for kind, teacher in (("生徒用", False), ("赤刷り", True)):
            parts = []
            for s in srcs:
                base = os.path.splitext(os.path.basename(s))[0]
                p = os.path.join(work, "%s_%s.pdf" % (base, kind))
                _render(s, p, teacher, work)
                n, size = pages(p)
                print("  %-22s %s  %sページ  %s" % (base, kind, n, size))
                if n != "1":
                    print("    ※ 1ページに収まっていません（%sページ）" % n)
                parts.append(p)
            out = os.path.join(outdir, "%s_%s.pdf" % (name, kind))
            if len(parts) == 1:
                shutil.copy(parts[0], out)
            else:
                subprocess.run(["pdfunite"] + parts + [out], check=True)
            made[kind] = out
            print("→ %s  (%sページ)" % (out, pages(out)[0]))
        return made
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    # 使い方: make_pdf.py <出力先ディレクトリ> <冊子名> <html...>
    main(sys.argv[3:], sys.argv[1], sys.argv[2])
