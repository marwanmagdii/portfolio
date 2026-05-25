import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for "Showing lines" and print 100 characters around it to see what it is
matches = [m.start() for m in re.finditer(r'Showing lines', text)]
print(f"Found {len(matches)} occurrences of Showing lines")
for idx in matches:
    print(text[idx:idx+150])
