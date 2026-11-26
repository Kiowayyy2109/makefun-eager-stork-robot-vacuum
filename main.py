import os

LINE = "I didn't miss that spot. I was saving it for later, like you save everything else for later."

LIMIT = 120
if len(LINE) != 92 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 92 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# The excuse only works if the vacuum sounds a little proud of it.
