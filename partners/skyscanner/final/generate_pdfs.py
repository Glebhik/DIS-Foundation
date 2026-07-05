#!/usr/bin/env python3
"""
DIS Group × Skyscanner — PDF Document Generator
Converts markdown documents to professional PDFs using xhtml2pdf.
"""

import os
import re
import markdown
from xhtml2pdf import pisa

BASE = "/Users/user1/Desktop/DIS-Foundation/partners/skyscanner"
OUT  = "/Users/user1/Desktop/DIS-Foundation/partners/skyscanner/final"

DOCS = [
    ("COVER_LETTER.md",       "01_Cover_Letter.pdf"),
    ("EXECUTIVE_ONE_PAGER.md","02_Executive_One_Pager.pdf"),
    ("TECHNICAL_OVERVIEW.md", "04_Technical_Overview.pdf"),
]

# ─── CSS TEMPLATE ────────────────────────────────────────────────────────────
CSS = """
@page {
    size: A4;
    margin: 1.8cm 2.4cm 2.2cm 2.4cm;
}

* {
    font-family: Helvetica, Arial, sans-serif;
    color: #111827;
    box-sizing: border-box;
}

body {
    font-size: 10.5pt;
    line-height: 1.5;
    color: #111827;
}

/* ── HEADINGS ── */
h1 {
    font-size: 20pt;
    font-weight: bold;
    color: #0E2C54;
    margin-top: 0.4cm;
    margin-bottom: 0.3cm;
    border-bottom: 2pt solid #0E2C54;
    padding-bottom: 0.15cm;
}

h2 {
    font-size: 14pt;
    font-weight: bold;
    color: #0E2C54;
    margin-top: 0.5cm;
    margin-bottom: 0.2cm;
    border-bottom: 0.75pt solid #E2E8F0;
    padding-bottom: 0.1cm;
}

h3 {
    font-size: 11pt;
    font-weight: bold;
    color: #1E40AF;
    margin-top: 0.3cm;
    margin-bottom: 0.15cm;
}

h4 {
    font-size: 10pt;
    font-weight: bold;
    color: #374151;
    margin-top: 0.2cm;
    margin-bottom: 0.1cm;
}

/* ── PARAGRAPHS ── */
p {
    margin-top: 0.1cm;
    margin-bottom: 0.25cm;
    orphans: 2;
    widows: 2;
}

em {
    color: #4B5563;
    font-style: italic;
}

strong {
    font-weight: bold;
    color: #111827;
}

/* ── BLOCKQUOTE ── */
blockquote {
    border-left: 3pt solid #2563EB;
    margin: 0.3cm 0 0.3cm 0;
    padding: 0.2cm 0.4cm;
    background-color: #F0F6FF;
    color: #1E3A5F;
    font-style: italic;
    font-size: 10pt;
}

/* ── HORIZONTAL RULE ── */
hr {
    border: none;
    border-top: 1pt solid #E2E8F0;
    margin: 0.4cm 0;
}

/* ── LISTS ── */
ul, ol {
    margin: 0.1cm 0 0.25cm 0.5cm;
    padding-left: 0.4cm;
}

li {
    margin-bottom: 0.12cm;
    line-height: 1.45;
}

/* ── TABLES ── */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.3cm 0;
    font-size: 9.5pt;
}

thead tr th {
    background-color: #0E2C54;
    color: #FFFFFF;
    font-weight: bold;
    padding: 0.18cm 0.22cm;
    text-align: left;
    border: 0.5pt solid #1E3A5F;
}

tbody tr:nth-child(even) td {
    background-color: #F8FAFC;
}

tbody tr:nth-child(odd) td {
    background-color: #FFFFFF;
}

tbody tr td {
    padding: 0.15cm 0.22cm;
    border: 0.5pt solid #E2E8F0;
    vertical-align: top;
    line-height: 1.4;
}

td:first-child {
    font-weight: bold;
    color: #0E2C54;
}

/* ── CODE ── */
code {
    font-family: Courier, monospace;
    font-size: 9pt;
    background-color: #F3F4F6;
    color: #1F2937;
    padding: 0.05cm 0.12cm;
    border-radius: 2pt;
}

pre {
    background-color: #F3F4F6;
    padding: 0.3cm;
    border-left: 3pt solid #2563EB;
    font-size: 8.5pt;
    font-family: Courier, monospace;
    margin: 0.2cm 0;
    white-space: pre-wrap;
    overflow-wrap: break-word;
}

/* ── LETTERHEAD ── */
.letterhead {
    border-bottom: 2pt solid #0E2C54;
    padding-bottom: 0.3cm;
    margin-bottom: 0.4cm;
}

.letterhead-company {
    font-size: 16pt;
    font-weight: bold;
    color: #0E2C54;
}

.letterhead-meta {
    font-size: 9pt;
    color: #6B7280;
    margin-top: 0.1cm;
}

/* ── COVER LETTER SPECIFICS ── */
.address-block {
    font-size: 10pt;
    line-height: 1.6;
    margin: 0.4cm 0;
}

/* ── CALLOUT BOX ── */
.callout {
    background-color: #EFF6FF;
    border-left: 3pt solid #2563EB;
    padding: 0.25cm 0.4cm;
    margin: 0.3cm 0;
}
"""

# ─── MARKDOWN PREPROCESSING ──────────────────────────────────────────────────
UNICODE_MAP = {
    "✅": "&#10003;",
    "🔄": "&#9654;",
    "📋": "&#9642;",
    "▸": "&rsaquo;",
    "→": "&rarr;",
    "↑": "&#8593;",
    "✗": "&#215;",
    "·": "&middot;",
    "×": "&times;",
    "—": "&mdash;",
    "–": "&ndash;",
    "’": "&rsquo;",
    "‘": "&lsquo;",
    "“": "&ldquo;",
    "”": "&rdquo;",
}


def preprocess(text):
    for char, entity in UNICODE_MAP.items():
        text = text.replace(char, entity)
    # Remove document footer lines (owner/status/date)
    text = re.sub(r'\*Owner:.*?\*\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*Last updated:.*?\*\s*$', '', text, flags=re.MULTILINE)
    return text


def md_to_html(md_text, title):
    md_text = preprocess(md_text)
    md_ext = ['tables', 'fenced_code', 'attr_list', 'def_list']
    body_html = markdown.markdown(md_text, extensions=md_ext)

    letterhead = f"""
<table width="100%" style="border-bottom: 2pt solid #0E2C54; margin-bottom: 0.4cm; padding-bottom: 0.2cm;">
  <tr>
    <td style="font-size:14pt; font-weight:bold; color:#0E2C54; font-family:Helvetica,Arial,sans-serif;">
      DIS GROUP
    </td>
    <td align="right" style="font-size:8pt; color:#9CA3AF; font-family:Helvetica,Arial,sans-serif; vertical-align:bottom;">
      CONFIDENTIAL &nbsp;&nbsp;|&nbsp;&nbsp; July 2026
    </td>
  </tr>
</table>"""

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
{letterhead}
{body_html}
<p style="margin-top:1cm; border-top:0.5pt solid #E2E8F0; padding-top:0.15cm;
   font-size:7.5pt; color:#9CA3AF; font-family:Helvetica,Arial,sans-serif;
   text-align:center;">
DIS Group &times; Skyscanner &nbsp;|&nbsp; Confidential &mdash; For Partnership Discussion Only &nbsp;|&nbsp; July 2026
</p>
</body>
</html>"""
    return html


def convert(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    title = os.path.basename(md_path).replace('.md', '').replace('_', ' ')
    html = md_to_html(md_content, title)

    with open(pdf_path, 'wb') as f:
        result = pisa.CreatePDF(html, dest=f)

    if result.err:
        print(f"  ERROR: {result.err}")
        return False
    print(f"  OK: {os.path.basename(pdf_path)}")
    return True


# ─── MAIN ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    errors = 0
    for src_name, dst_name in DOCS:
        src = os.path.join(BASE, src_name)
        dst = os.path.join(OUT, dst_name)
        print(f"Converting {src_name} ...")
        if not convert(src, dst):
            errors += 1

    if errors == 0:
        print(f"\nAll PDFs generated in {OUT}")
    else:
        print(f"\n{errors} error(s) occurred.")
