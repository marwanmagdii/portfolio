import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for "view_file" and "about.html" and find the args and response size
for m in re.finditer(r'\{[^\}]*"step_index"\s*:\s*(\d+)[^\}]*"view_file"[^\}]*\}', text):
    line = m.group(0)
    if 'about.html' in line:
        print(f"Step {m.group(1)}: {line[:300]}")
