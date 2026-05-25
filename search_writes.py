import re

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for any tool calls that wrote to about.html
# e.g., write_to_file, replace_file_content, multi_replace_file_content
# and print their step index, name, and size if possible.
for m in re.finditer(r'\{[^\}]*"step_index"\s*:\s*(\d+)[^\}]*"name"\s*:\s*"[^"]*file"[^\}]*\}', text):
    line = m.group(0)
    if 'about.html' in line:
        print(f"Step {m.group(1)}: {line[:200]}")
