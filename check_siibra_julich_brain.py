#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "siibra",
# ]
# ///

# Synchon Mandal, 2026
# Naive checking of Julich-Brain via siibra, no tricks

import re
import sys
from pathlib import Path

import siibra as s

pattern = re.compile(r"V[\d_]+\d+$")
a = s.atlases.get("human")
ps = set([re.search(pattern, p).group(0) for p in a.parcellations.keys if p.startswith("JULICH")])
base_dir = Path("./parcellations/Julich-Brain")
vs = set([re.search(pattern, v_dir.name).group(0) for v_dir in base_dir.glob("V*")])
if ps != vs:
    print(f"New version available: {ps - vs}")
    sys.exit(1)
else:
    print("Versions up-to-date")
    sys.exit(0)
