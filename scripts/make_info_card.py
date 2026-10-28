"""
Build a neofetch-style info card SVG for the whoami section of the profile
README: colored key/value rows for role and stack. Deliberately no focus /
passion / highlights rows and no GitHub stats -- the contribution graph right
above it already covers activity.

Static content, hand-authored below. Lines fade/slide in on a short stagger so
it feels like the panel is printing. STATIC=1 emits the frozen state.
"""
import html
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")
STATIC = bool(os.environ.get("STATIC"))

W = 480
PAD = 20
TITLEBAR_H = 30
KEY_X = PAD
VAL_X = PAD + 92
LINE_H = 20.5
TOP_PAD = 30
BOTTOM_PAD = 24

BG = "#0a0e0c"
BG2 = "#101614"
FRAME = "#2b3a32"
MUTED = "#7d8590"
INK = "#e6edf3"
KEY = "#3fb950"      # green keys
SECTION = "#7ee787"  # brighter green section headers
HOST = "asimali@github"

# content model: tuples describing each row
# ("host",)                    -> "asimali@github" + rule
# ("kv", key, value)           -> green key + light value
# ("sec", title)               -> bright green "-- title --" rule
# ("gap",)                     -> vertical space
ROWS = [
    ("host",),
    ("kv", "Role", "Backend Engineer / PHP & Laravel"),
    ("gap",),
    ("sec", "Stack"),
    ("kv", "Languages", "PHP, Python, TypeScript"),
    ("kv", "Backend", "Laravel, FastAPI, REST APIs"),
    ("kv", "Data", "MySQL 8, Redis, Pinecone"),
    ("kv", "Auth", "OAuth 2.0, PKCE, JWT (RS256)"),
    ("kv", "Frontend", "React, Inertia.js, Tailwind"),
    ("kv", "Ops", "GitHub Actions, Horizon, Linux"),
]


def esc(s):
    return html.escape(s)


def rise(inner, i):
    """fade + slight upward slide, staggered by row index; freezes visible."""
    if STATIC:
        return f"<g>{inner}</g>"
    delay = 0.15 + i * 0.06
    return (f'<g opacity="0" transform="translate(0,5)">{inner}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.4s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" '
            f'begin="{delay:.2f}s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/></g>')


def canvas_height():
    y = TITLEBAR_H + TOP_PAD
    for row in ROWS:
        y += LINE_H * 0.5 if row[0] == "gap" else LINE_H
    return int(math.ceil(y + BOTTOM_PAD))


H = canvas_height()

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    '<defs>'
    f'<linearGradient id="ibg" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>',
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#ibg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]
for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')
parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" '
             f'text-anchor="middle">asimali@github: ~$ neofetch</text>')

y = TITLEBAR_H + TOP_PAD
for i, row in enumerate(ROWS):
    kind = row[0]
    if kind == "gap":
        y += LINE_H * 0.5
        continue
    if kind == "host":
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" font-size="14" font-weight="700">'
                 f'<tspan fill="{SECTION}">asimali</tspan><tspan fill="{MUTED}">@</tspan>'
                 f'<tspan fill="{KEY}">github</tspan></text>'
                 f'<line x1="{KEY_X + len(HOST) * 8.4 + 10:.1f}" y1="{y-4:.1f}" x2="{W-PAD}" y2="{y-4:.1f}" '
                 f'stroke="{FRAME}" stroke-opacity="0.8"/>')
    elif kind == "sec":
        title = esc(row[1])
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" fill="{SECTION}" font-size="12.5" font-weight="700">'
                 f'&#8212; {title}</text>'
                 f'<line x1="{KEY_X + 12 + len(row[1])*8}" y1="{y-4:.1f}" x2="{W-PAD}" y2="{y-4:.1f}" '
                 f'stroke="{FRAME}" stroke-opacity="0.8"/>')
    elif kind == "kv":
        key, val = esc(row[1]), esc(row[2])
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" fill="{KEY}" font-size="12.5" font-weight="700">{key}</text>'
                 f'<text x="{VAL_X}" y="{y:.1f}" fill="{INK}" font-size="12.5">{val}</text>')
    else:
        continue
    parts.append(rise(inner, i))
    y += LINE_H

parts.append("</svg>")
svg = "".join(parts)
with open(OUT, "w") as f:
    f.write(svg)
print("wrote", OUT, len(svg), "bytes;", W, "x", H, "content_bottom", round(y))
