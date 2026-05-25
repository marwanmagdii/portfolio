import os, glob

BASE = r'D:\web\portfolio entrepreneur'

# Fix all article files: remove "By Marwan Magdy" author line, fix back-link position
article_files = glob.glob(os.path.join(BASE, 'article-*.html'))

for path in article_files:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    changed = False
    
    # 1. Remove "By Marwan Magdy" / author meta span
    import re
    # Remove entire author avatar + "By Marwan..." span
    html_new = re.sub(
        r'<img[^>]*class="avatar"[^>]*>\s*<span>By Marwan Magdy[^<]*</span>\s*<span>·</span>\s*',
        '',
        html
    )
    if html_new != html:
        html = html_new
        changed = True

    # 2. Fix back-link — must be OUTSIDE the article-header center block, at top
    # Remove back-link from inside article-header if present
    # Place it as a standalone element above article-header
    if 'class="back-link"' in html:
        # Extract back link
        back_match = re.search(r'(<a[^>]+class="back-link"[^>]*>.*?</a>)', html, re.DOTALL)
        if back_match:
            back_html = back_match.group(1)
            # Ensure not inside article-header but before it
            if '<header class="article-header">' in html and back_html in html:
                # Remove from current location
                html = html.replace(back_html, '', 1)
                # Add before article-header with its own container
                back_wrapper = f'''  <div style="padding-top:7rem;padding-bottom:1rem;">
    {back_html}
  </div>
  '''
                html = html.replace('<header class="article-header">', back_wrapper + '<header class="article-header" style="padding-top:2rem;">', 1)
                changed = True

    # 3. Fix: category badge/tag appearing above title — move after h1
    # Pattern: tag div then h1 — should be tag THEN h1 (already correct)
    # Issue was badge ABOVE the header section — ensure correct order: kicker, h1, meta
    
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed: {os.path.basename(path)}")
    else:
        print(f"No changes: {os.path.basename(path)}")

print("\nAll articles processed")
