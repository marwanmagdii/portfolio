html = open('index.html', encoding='utf-8').read()

# Find what sections exist
import re
sections = re.findall(r'<!--[^>]{1,60}-->', html)
for i, s in enumerate(sections[:40]):
    print(f"{i}: {s.strip()}")
print("\nTotal lines:", len(html.splitlines()))
