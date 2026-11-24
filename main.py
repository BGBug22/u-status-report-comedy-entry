# Status Report Comedy Sprint — make.fun entry.
#
# Writes one funny status-report line (<=200 characters) to
# /output/entry.txt: the weekly report an AI agent sends its human.
#
# The joke is the report eating itself: the agent finished every task,
# then spent 3 hours writing the report about it, and files the report
# under the very kind of task it just created.
#
# Python 3.13, standard library only, no network, fully deterministic:
# every run writes the exact same bytes.

import os
import sys

LINE = (
    "All 47 tasks complete, 0 failed. This status report took 3 hours, "
    "so I have filed it under 'tasks that create more tasks'."
)

# The gate only accepts 1-200 characters, so refuse to write anything
# outside that range instead of shipping an entry the judge never sees.
length = len(LINE)
if length < 1 or length > 200:
    sys.exit(f"line must be 1-200 characters, got {length}")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
