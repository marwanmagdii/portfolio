import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for "VOLUNTEER" in a case-insensitive manner
matches = [m.start() for m in re.finditer(r'volunteer', text, re.IGNORECASE)]
print(f"Found {len(matches)} matches.")
for idx in matches:
    # Print the next 500 characters
    chunk = text[idx:idx+800]
    if 'section' in chunk or 'class=' in chunk or 'Red Crescent' in chunk:
        print("--- MATCH AT INDEX", idx)
        print(chunk)
        print("====================================")
