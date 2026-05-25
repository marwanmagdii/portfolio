with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Sequentially replace each blog.html Learn More link with specific article links
articles = [
    'article-riadi.html',
    'article-alx.html',
    'article-garnet.html',
    'article-judhur.html',
    'article-greenpulse.html',
    'article-cae.html',
    'article-unbounded.html',
]

old = 'href="blog.html" class="btn-preview">Learn More'
count_before = content.count(old)
print(f"Found {count_before} occurrences of old link")

for art in articles:
    new = f'href="{art}" class="btn-preview">Learn More'
    content = content.replace(old, new, 1)

count_after = content.count(old)
print(f"Remaining unpatched: {count_after}")

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done patching about.html article links")
