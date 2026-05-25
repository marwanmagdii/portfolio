import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for "page-title" or "page-header" or "about.html" and print nearby content
matches = [m.start() for m in re.finditer(r'page-title|page-header', text)]
print(f"Found {len(matches)} occurrences:")
for idx in matches[:10]:
    print("--- CONTEXT ---")
    print(text[idx-200:idx+400])
    print("----------------")
