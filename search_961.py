import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for s in [972, 975, 978, 981, 987, 990, 997, 1000]:
    for m in re.finditer(r'\{[^\}]*"step_index"\s*:\s*'+str(s)+r'[^\}]*\}', text):
        print(f"Step {s}: {m.group(0)[:500]}")
