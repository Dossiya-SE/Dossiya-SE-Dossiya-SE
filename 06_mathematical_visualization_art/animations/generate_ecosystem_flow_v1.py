#!/usr/bin/env python3
"""Generate deterministic structural-reveal GIF for the 12-module mathematics ecosystem.

tau_ui is presentation/reveal time only. It is not physical time and does not
encode importance, learning speed, difficulty, causal strength, or evidence.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
FRAMES = 48
DURATION_MS = 100

BG = "#07111F"
PANEL = "#0E1D31"
INK = "#EAF1F8"
MUTED = "#94A3B8"
LINE = "#355A7B"
ACCENT = "#87CEFA"
ACCENT_STRONG = "#2D8FD6"
VIOLET = "#7E22CE"

MODULES = [
    ("01", "Foundations"),
    ("02", "Models"),
    ("03", "Examples"),
    ("04", "Reproductions"),
    ("05", "Skills"),
    ("06", "Visualization"),
    ("07", "Computing"),
    ("08", "Verification"),
    ("09", "Math Physics"),
    ("10", "Engineering"),
    ("11", "Literature Atlas"),
    ("12", "Research Lab"),
]

def font(size: int, bold: bool = False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

F_TITLE = font(31, True)
F_SUB = font(18)
F_NODE = font(18, True)
F_SMALL = font(14)

def positions():
    xs = [170, 440, 710, 980]
    ys = [210, 360, 510]
    pts = []
    for row, y in enumerate(ys):
        row_xs = xs if row % 2 == 0 else list(reversed(xs))
        pts.extend((x, y) for x in row_xs)
    return pts

PTS = positions()

def center_text(draw, xy, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    w = box[2] - box[0]
    h = box[3] - box[1]
    draw.text((xy[0]-w/2, xy[1]-h/2), text, font=fnt, fill=fill)

def draw_frame(frame: int) -> Image.Image:
    tau = frame / (FRAMES - 1)
    progress = tau * (len(MODULES) - 1)
    complete = int(progress)
    frac = progress - complete

    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((45, 40, W-45, H-40), radius=28, fill=PANEL, outline=LINE, width=2)
    d.text((85, 75), "Mathematics Research Ecosystem", font=F_TITLE, fill=INK)
    d.text((85, 118), "Governed 12-module structural reveal", font=F_SUB, fill=ACCENT)
    d.text((780, 82), "τ_ui = presentation order", font=F_SUB, fill=ACCENT)
    d.text((780, 112), "not physical time", font=F_SMALL, fill=MUTED)

    # Base sequence and progressive active segment.
    for i in range(len(PTS)-1):
        p, q = PTS[i], PTS[i+1]
        d.line((p[0], p[1], q[0], q[1]), fill=LINE, width=4)
        if i < complete:
            d.line((p[0], p[1], q[0], q[1]), fill=ACCENT_STRONG, width=5)
        elif i == complete:
            ex = p[0] + frac * (q[0]-p[0])
            ey = p[1] + frac * (q[1]-p[1])
            d.line((p[0], p[1], ex, ey), fill=ACCENT, width=6)

    for i, ((num, label), (x, y)) in enumerate(zip(MODULES, PTS)):
        revealed = i <= complete
        active = i == complete and frame < FRAMES-1
        r = 52 if not active else 58
        fill = "#122941" if not revealed else "#10283F"
        outline = LINE if not revealed else ACCENT
        if active:
            outline = ACCENT
        d.ellipse((x-r, y-r, x+r, y+r), fill=fill, outline=outline, width=4 if revealed else 2)
        center_text(d, (x, y-12), num, F_NODE, ACCENT if revealed else MUTED)
        center_text(d, (x, y+17), label, F_SMALL, INK if revealed else MUTED)

    d.text((85, 602), "Static authority: assets/mathematics-ecosystem-v4.svg", font=F_SMALL, fill=MUTED)
    d.text((760, 602), "No importance / speed / causality encoded", font=F_SMALL, fill=MUTED)
    return im

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="assets/animations/mathematics-ecosystem-flow-v1.gif")
    args = parser.parse_args()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    frames = [draw_frame(i) for i in range(FRAMES)]
    frames[0].save(
        out,
        save_all=True,
        append_images=frames[1:],
        duration=DURATION_MS,
        loop=0,
        optimize=False,
        disposal=2,
    )
    print(f"wrote {out} frames={FRAMES} size={W}x{H} duration_ms={DURATION_MS}")

if __name__ == "__main__":
    main()
