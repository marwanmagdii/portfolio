import re

# Read existing certifications.html to extract all cert data
with open('certifications.html', 'r', encoding='utf-8') as f:
    old = f.read()

# Extract all openModal calls to get cert data
pattern = r"openModal\('([^']+)',\s*'([^']+)',\s*'([^']+)',\s*'(\[[^\]]+\])',\s*'([^']+)',\s*'([^']+)'\)"
certs = re.findall(pattern, old)

# Get data-category for each cert card
cat_pattern = r'<div class="cert-card[^"]*" data-category="([^"]+)"[^>]*>.*?openModal\(([^)]+)\)'
cats_raw = re.findall(r'data-category="([^"]+)"', old)

print(f"Found {len(certs)} certs, {len(cats_raw)} categories")
for i,(title,issuer,date,learnings,pdf,cid) in enumerate(certs):
    cat = cats_raw[i] if i < len(cats_raw) else 'unknown'
    print(f"  [{cat}] {title} | {issuer} | {date} | ID:{cid}")
