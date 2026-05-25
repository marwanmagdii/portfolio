import re

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Search for "VIEW_FILE" and "about.html" and find the lines shown
for m in re.finditer(r'\{[^\}]*"step_index"\s*:\s*(\d+)[^\}]*"VIEW_FILE"[^\}]*\}', text):
    line = m.group(0)
    if 'about.html' in line:
        # extract showing lines or size
        lines_match = re.search(r'Showing lines \d+ to \d+', line)
        total_lines_match = re.search(r'Total Lines: \d+', line)
        print(f"Step {m.group(1)}: {lines_match.group(0) if lines_match else 'no lines info'}, {total_lines_match.group(0) if total_lines_match else 'no total lines'}")
