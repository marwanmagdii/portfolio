import os, glob, re

BASE = r'D:\web\portfolio entrepreneur'

# 1. Rename EGYPES competition in index.html
path_index = os.path.join(BASE, 'index.html')
with open(path_index, 'r', encoding='utf-8') as f:
    index = f.read()

index = index.replace(
    'Shell Intilaaqah @ EGYPES',
    'Flat6Labs and Shell Intilaaqah Competition during EGYPES 2026'
)

with open(path_index, 'w', encoding='utf-8') as f:
    f.write(index)


# 2. Rename EGYPES competition in blog.html and remove "By Marwan Magdy" in the blog cards if it exists there
path_blog = os.path.join(BASE, 'blog.html')
with open(path_blog, 'r', encoding='utf-8') as f:
    blog = f.read()

# Replace the title in blog.html featured card
blog = blog.replace(
    'Winning 1st Place at EGYPES 2026 with Riadi',
    'Winning 1st Place at Flat6Labs and Shell Intilaaqah Competition during EGYPES 2026'
)

with open(path_blog, 'w', encoding='utf-8') as f:
    f.write(blog)


# 3. Redesign headers in all article-*.html
article_files = glob.glob(os.path.join(BASE, 'article-*.html'))

for file in article_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Also rename the title if it's the riadi article
    html = html.replace(
        'Winning 1st Place at EGYPES 2026 with Riadi',
        'Winning 1st Place at Flat6Labs and Shell Intilaaqah Competition during EGYPES 2026'
    )

    # We need to find the <header class="article-header"> section
    # Current structure:
    # <div>
    #     <span class="article-tag">...</span>
    #     <h1 class="article-title">...</h1>
    #     <div class="article-meta">
    #         <img ...>
    #         <span>By Marwan Magdy</span>
    #         <span>&bull;</span>
    #         <span>...</span>
    #     </div>
    # </div>
    
    # We want: h1 first, then tag, then meta (without By Marwan Magdy)
    
    match = re.search(r'(<span class="article-tag">.*?</span>)\s*(<h1 class="article-title">.*?</h1>)', html, re.DOTALL)
    if match:
        tag = match.group(1)
        title = match.group(2)
        # Swap them
        html = html.replace(tag, '', 1)
        # Add a little margin to the title bottom and tag bottom so it looks nice
        tag_styled = tag.replace('class="article-tag"', 'class="article-tag" style="margin-top:1rem;margin-bottom:1.5rem;"')
        html = html.replace(title, f"{title}\n                {tag_styled}", 1)

    # Remove "By Marwan Magdy" and the bullet point from article-meta
    html = re.sub(r'<span>By Marwan Magdy</span>\s*<span>&bull;</span>', '', html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Article redesign applied to all.")
