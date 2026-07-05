#!/usr/bin/env python3
"""
DIS Group — Team Profile PDF Generator
Converts TEAM_PROFILE.md to a professional PDF using xhtml2pdf.
"""

import os
import re
import markdown
from xhtml2pdf import pisa

BASE = "/Users/user1/Desktop/DIS-Foundation/partners"
SRC  = os.path.join(BASE, "TEAM_PROFILE.md")
OUT  = os.path.join(BASE, "TEAM_PROFILE.pdf")

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

blockquote {
    border-left: 3pt solid #2563EB;
    margin: 0.3cm 0 0.3cm 0;
    padding: 0.2cm 0.4cm;
    background-color: #F0F6FF;
    color: #1E3A5F;
    font-style: italic;
    font-size: 10pt;
}

hr {
    border: none;
    border-top: 1pt solid #E2E8F0;
    margin: 0.4cm 0;
}

ul, ol {
    margin: 0.1cm 0 0.25cm 0.5cm;
    padding-left: 0.4cm;
}

li {
    margin-bottom: 0.12cm;
    line-height: 1.45;
}

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

code {
    font-family: Courier, monospace;
    font-size: 9pt;
    background-color: #F3F4F6;
    color: #1F2937;
    padding: 0.05cm 0.12cm;
}
"""

UNICODE_MAP = {
    "—": "&mdash;",
    "–": "&ndash;",
    "’": "&rsquo;",
    "‘": "&lsquo;",
    "“": "&ldquo;",
    "”": "&rdquo;",
    "→": "&rarr;",
    "↓": "&#8595;",
    "×": "&times;",
    "·": "&middot;",
}


def preprocess(text):
    for char, entity in UNICODE_MAP.items():
        text = text.replace(char, entity)
    text = re.sub(r'\*Owner:.*?\*\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*Last updated:.*?\*\s*$', '', text, flags=re.MULTILINE)
    return text


def build_html(md_text):
    md_text = preprocess(md_text)
    body_html = markdown.markdown(
        md_text,
        extensions=['tables', 'fenced_code', 'attr_list', 'def_list']
    )

    letterhead = """
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

    footer = """
<p style="margin-top:1cm; border-top:0.5pt solid #E2E8F0; padding-top:0.15cm;
   font-size:7.5pt; color:#9CA3AF; font-family:Helvetica,Arial,sans-serif;
   text-align:center;">
DIS Group &nbsp;|&nbsp; Confidential &mdash; Enterprise Partnership Briefing &nbsp;|&nbsp; July 2026
</p>"""

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>DIS Group — Leadership and Company Profile</title>
<style>{CSS}</style>
</head>
<body>
{letterhead}
{body_html}
{footer}
</body>
</html>"""


def main():
    with open(SRC, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html = build_html(md_content)

    with open(OUT, 'wb') as f:
        result = pisa.CreatePDF(html, dest=f)

    if result.err:
        print(f"ERROR: {result.err}")
        return False

    size_kb = os.path.getsize(OUT) // 1024
    print(f"OK: TEAM_PROFILE.pdf ({size_kb} KB) → {OUT}")
    return True


if __name__ == "__main__":
    main()
