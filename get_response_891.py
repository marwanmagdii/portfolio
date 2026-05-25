import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Find the position of step_index: 891
idx = text.find('"step_index":891')
if idx != -1:
    print("Found step 891 at position:", idx)
    print(text[idx:idx+2000])
else:
    print("Step 891 not found")
