with open('step961_raw.json', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

print("File size:", len(text))
# Let's search for "ReplacementContent" ignoring backslashes
import re
matches = [m.start() for m in re.finditer('ReplacementContent', text)]
print("ReplacementContent count:", len(matches))
for idx in matches:
    print("Match at:", idx)
    print(text[idx:idx+150])
