#!/usr/bin/env python3
"""Convert a Markdown file to a client-ready A4 PDF using headless Chrome.

Usage:
    python3 tools/md-to-pdf.py docs/daftar-modul-dan-harga.md [output.pdf]

No third-party Python packages required.
"""

import html
import os
import re
import subprocess
import sys
import tempfile

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
]

CSS = """
@page { size: A4; margin: 16mm 14mm 18mm 14mm; }

* { box-sizing: border-box; }

body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.55;
  color: #1a1a1a;
  margin: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

h1 {
  font-size: 19pt;
  line-height: 1.25;
  margin: 0 0 14px 0;
  padding-bottom: 10px;
  border-bottom: 2.5px solid #1a1a1a;
  letter-spacing: -0.2px;
}

h2 {
  font-size: 12.5pt;
  margin: 22px 0 8px 0;
  padding-bottom: 5px;
  border-bottom: 1px solid #d8d8d8;
  letter-spacing: 0.2px;
}

h3 {
  font-size: 10.5pt;
  margin: 14px 0 6px 0;
  color: #333;
}

p { margin: 0 0 9px 0; }

ul { margin: 0 0 10px 0; padding-left: 18px; }
li { margin-bottom: 4px; }

blockquote {
  margin: 0 0 14px 0;
  padding: 11px 14px;
  background: #f4f6f8;
  border-left: 4px solid #1a1a1a;
  font-size: 10.5pt;
}

blockquote p { margin: 0; }

table {
  width: 100%;
  border-collapse: collapse;
  margin: 0 0 14px 0;
  font-size: 9.5pt;
}

thead { display: table-header-group; }

th {
  background: #1a1a1a;
  color: #ffffff;
  text-align: left;
  font-weight: 600;
  padding: 7px 8px;
  border: 1px solid #1a1a1a;
}

td {
  padding: 6px 8px;
  border: 1px solid #d5d5d5;
  vertical-align: top;
}

tbody tr:nth-child(even) td { background: #fafafa; }

tr { page-break-inside: avoid; }

td:last-child, th:last-child { white-space: nowrap; }

strong { font-weight: 600; }

code {
  font-family: "SF Mono", Menlo, monospace;
  font-size: 9pt;
  background: #f0f0f0;
  padding: 1px 4px;
  border-radius: 3px;
}

hr { border: none; border-top: 1px solid #d8d8d8; margin: 18px 0; }
"""


def inline(text):
    """Escape HTML then apply inline markdown formatting."""
    out = html.escape(text, quote=False)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"`(.+?)`", r"<code>\1</code>", out)
    out = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", out)
    return out


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def align_of(spec):
    spec = spec.strip()
    if spec.endswith(":") and spec.startswith(":"):
        return "center"
    if spec.endswith(":"):
        return "right"
    return "left"


def convert(markdown):
    lines = markdown.splitlines()
    body = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("### "):
            body.append("<h3>%s</h3>" % inline(stripped[4:]))
            i += 1
            continue

        if stripped.startswith("## "):
            body.append("<h2>%s</h2>" % inline(stripped[3:]))
            i += 1
            continue

        if stripped.startswith("# "):
            body.append("<h1>%s</h1>" % inline(stripped[2:]))
            i += 1
            continue

        if stripped.startswith(">"):
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            body.append("<blockquote><p>%s</p></blockquote>" % inline(" ".join(quote)))
            continue

        if stripped.startswith("|") and i + 1 < n and lines[i + 1].strip().startswith("|"):
            header = split_row(stripped)
            aligns = [align_of(c) for c in split_row(lines[i + 1])]
            i += 2

            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1

            thead = "".join(
                '<th style="text-align:%s">%s</th>' % (aligns[j] if j < len(aligns) else "left", inline(cell))
                for j, cell in enumerate(header)
            )
            tbody = []
            for row in rows:
                cells = "".join(
                    '<td style="text-align:%s">%s</td>' % (aligns[j] if j < len(aligns) else "left", inline(cell))
                    for j, cell in enumerate(row)
                )
                tbody.append("<tr>%s</tr>" % cells)

            body.append(
                "<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>"
                % (thead, "".join(tbody))
            )
            continue

        if stripped.startswith("- "):
            items = []
            while i < n and lines[i].strip().startswith("- "):
                items.append(inline(lines[i].strip()[2:]))
                i += 1
            body.append("<ul>%s</ul>" % "".join("<li>%s</li>" % it for it in items))
            continue

        if set(stripped) <= {"-"} and len(stripped) >= 3:
            body.append("<hr/>")
            i += 1
            continue

        paragraph = []
        while i < n and lines[i].strip() and not lines[i].strip().startswith(("#", ">", "|", "- ")):
            paragraph.append(lines[i].strip())
            i += 1
        if paragraph:
            body.append("<p>%s</p>" % inline(" ".join(paragraph)))

    return (
        "<!DOCTYPE html><html lang=\"id\"><head><meta charset=\"utf-8\">"
        "<title>Daftar Modul dan Harga</title><style>%s</style></head>"
        "<body>%s</body></html>" % (CSS, "".join(body))
    )


def find_chrome():
    for path in CHROME_CANDIDATES:
        if os.path.exists(path):
            return path
    return None


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0

    source = sys.argv[1]
    if not os.path.isfile(source):
        print("File tidak ditemukan: %s" % source)
        return 1
    target = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(source)[0] + ".pdf"

    chrome = find_chrome()
    if not chrome:
        print("Chrome/Chromium tidak ditemukan.")
        return 1

    with open(source, encoding="utf-8") as fh:
        markdown = fh.read()

    page_html = convert(markdown)

    tmp_html = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp_html.write(page_html)
    tmp_html.close()

    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        "--print-to-pdf=" + os.path.abspath(target),
        "file://" + os.path.abspath(tmp_html.name),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    os.unlink(tmp_html.name)

    if not os.path.exists(target):
        print(result.stderr[-2000:])
        print("Gagal membuat PDF.")
        return 1

    size_kb = os.path.getsize(target) / 1024
    print("PDF dibuat: %s (%.1f KB)" % (target, size_kb))
    return 0


if __name__ == "__main__":
    sys.exit(main())