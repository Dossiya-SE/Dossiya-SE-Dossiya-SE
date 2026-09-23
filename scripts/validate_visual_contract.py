#!/usr/bin/env python3
"""Fail-closed local visual contract validator."""

from __future__ import annotations

import colorsys
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_WORDS = re.compile(r"\b(gold|golden|goldenrod|darkgoldenrod|amber|ochre|yellow-gold)\b", re.I)
TEXT_SUFFIX = {".md",".svg",".py",".json",".yml",".yaml",".css",".js",".mjs",".html"}
SCAN_ROOTS = [ROOT/"README.md", ROOT/"assets", ROOT/"05_mathematical_skills_development", ROOT/"06_mathematical_visualization_art", ROOT/"docs"/"visual-system"]
SELF = Path(__file__).resolve()

def warm(hex_value: str) -> bool:
    h = hex_value.lstrip("#")
    if len(h) != 6:
        return False
    r,g,b = [int(h[i:i+2],16)/255 for i in (0,2,4)]
    hue, light, sat = colorsys.rgb_to_hls(r,g,b)
    deg = hue*360
    return 32 <= deg <= 72 and sat >= .45 and .18 <= light <= .90

def files():
    for root in SCAN_ROOTS:
        if root.is_file():
            yield root
        elif root.exists():
            yield from (p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in TEXT_SUFFIX)

fail=[]
for p in files():
    if p.resolve()==SELF:
        continue
    s=p.read_text(encoding="utf-8")
    for pattern in VISUAL_NAME_PATTERNS:
        if pattern.search(s):
            fail.append(f"{p.relative_to(ROOT)}: forbidden warm/gold visual identifier")
    for token in set(re.findall(r"#[0-9A-Fa-f]{6}\b",s)):
        if warm(token):
            fail.append(f"{p.relative_to(ROOT)}: unauthorized warm hue {token}")

for p in ROOT.rglob("*.svg"):
    try:
        s=p.read_text(encoding="utf-8")
        root=ET.fromstring(s)
    except Exception as exc:
        fail.append(f"{p.relative_to(ROOT)}: SVG parse failed {exc}")
        continue
    if not root.attrib.get("viewBox"):
        fail.append(f"{p.relative_to(ROOT)}: missing viewBox")
    if root.attrib.get("role")!="img":
        fail.append(f"{p.relative_to(ROOT)}: missing role=img")
    title=next((e for e in root.iter() if e.tag.endswith("title")),None)
    desc=next((e for e in root.iter() if e.tag.endswith("desc")),None)
    if title is None or not "".join(title.itertext()).strip():
        fail.append(f"{p.relative_to(ROOT)}: missing title")
    if desc is None or not "".join(desc.itertext()).strip():
        fail.append(f"{p.relative_to(ROOT)}: missing desc")

manifest_path=ROOT/"06_mathematical_visualization_art/animations/ecosystem_flow_v1.motion.json"
gif_path=ROOT/"assets/animations/mathematics-ecosystem-flow-v1.gif"
generator=ROOT/"06_mathematical_visualization_art/animations/generate_ecosystem_flow_v1.py"
if not manifest_path.exists():
    fail.append("motion manifest missing")
else:
    m=json.loads(manifest_path.read_text(encoding="utf-8"))
    if m.get("motion_variable",{}).get("symbol")!="tau_ui":
        fail.append("motion variable must be tau_ui")
    if m.get("motion_variable",{}).get("physical_time") is not False:
        fail.append("tau_ui must be explicitly non-physical")
if not gif_path.exists():
    fail.append("generated ecosystem GIF missing")
elif gif_path.stat().st_size < 10_000:
    fail.append("generated ecosystem GIF unexpectedly small")
else:
    with tempfile.TemporaryDirectory() as td:
        regen=Path(td)/"regen.gif"
        subprocess.run([sys.executable,str(generator),"--output",str(regen)],check=True)
        a=hashlib.sha256(gif_path.read_bytes()).hexdigest()
        b=hashlib.sha256(regen.read_bytes()).hexdigest()
        if a!=b:
            fail.append(f"GIF deterministic regeneration mismatch committed={a} regenerated={b}")

if fail:
    print("VISUAL CONTRACT: FAIL", file=sys.stderr)
    for item in fail:
        print(" -",item,file=sys.stderr)
    raise SystemExit(1)

print("VISUAL CONTRACT: PASS — palette, SVG accessibility, motion provenance and deterministic GIF verified.")
