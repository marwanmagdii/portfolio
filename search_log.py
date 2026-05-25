import re

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's find all instances of write_to_file or replace_file_content or multi_replace_file_content targeting about.html
matches = re.finditer(r'("TargetFile"|"TargetContent"|"CodeContent"|"ReplacementContent"|"about.html")', text)
# Let's print occurrences around step_index
for m in re.finditer(r'\{[^\}]*"step_index"\s*:\s*(\d+)[^\}]*\}', text):
    line = m.group(0)
    if 'about.html' in line:
        print(f"Step {m.group(1)}: {line[:150]}")
