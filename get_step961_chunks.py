import re
import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for "step_index":961 or "step_index": 961 and grab the whole line
for m in re.finditer(r'\{[^\}]*"step_index"\s*:\s*961[^\}]*\}', text):
    line = m.group(0)
    print("Found step 961 log line.")
    # Write to a file since it's very long
    with open('step961_raw.json', 'w', encoding='utf-8') as out:
        out.write(line)
    print("Wrote to step961_raw.json")
