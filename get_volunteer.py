import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for "VOLUNTEER" in the log and print lines around it to find the HTML chunk
# that was viewed or replaced.
matches = [m.start() for m in re.finditer(r'volunteer', text, re.IGNORECASE)]
print(f"Found {len(matches)} occurrences of volunteer:")
for idx in matches:
    # print context of 300 chars before and after
    print("--- CONTEXT ---")
    print(text[idx-200:idx+400])
    print("----------------")
