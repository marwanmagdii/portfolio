import os, glob, re

BASE = r'D:\web\portfolio entrepreneur'

# 1. Global Em Dash removal and "backed by" to "accelerator"
html_files = glob.glob(os.path.join(BASE, '*.html'))
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove em dash
    content = content.replace(" — ", ", ")
    content = content.replace("—", "-")
    
    # Replace "backed by"
    content = re.sub(r'backed by Flat6Labs', 'accelerated by Flat6Labs', content, flags=re.IGNORECASE)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Fix Index CSS Hero background gradient
path_index = os.path.join(BASE, 'index.html')
with open(path_index, 'r', encoding='utf-8') as f:
    index = f.read()

index = re.sub(r'\.hero-photo-wrap::after\s*\{[^\}]+\}', '', index)
with open(path_index, 'w', encoding='utf-8') as f:
    f.write(index)

# 3. Blog Cards hero image fix
path_blog = os.path.join(BASE, 'blog.html')
with open(path_blog, 'r', encoding='utf-8') as f:
    blog = f.read()

# Fix Unbounded card image
blocks = blog.split('<a href="article-')
for i, b in enumerate(blocks):
    if 'article-unbounded.html' in b or 'Unbounded:' in b:
        blocks[i] = re.sub(
            r'<div class="card-img\s*.*?">\s*<img src="[^"]+" alt="Unbounded[^"]+">',
            r'<div class="card-img">\n        <img src="assets/logo/unbounded/unbounded logo.jpg" alt="Unbounded" style="object-fit:cover;">',
            b, flags=re.DOTALL|re.IGNORECASE
        )
    if 'article-garnet.html' in b or 'Scaling Garnet_eg' in b:
        # Check if Garnet card exists in blog. It might not! 
        # Wait, Garnet is not in blog.html? No, Garnet wasn't in blog, it was in ventures.html.
        # But if it is, fix it:
        blocks[i] = re.sub(
            r'<div class="card-img\s*.*?">\s*<img src="[^"]+" alt="Scaling Garnet_eg[^"]+">',
            r'<div class="card-img">\n        <img src="assets/logo/garnet/garnet.png" alt="Garnet" style="object-fit:contain;background:#fff;padding:1.5rem;">',
            b, flags=re.DOTALL|re.IGNORECASE
        )

blog = '<a href="article-'.join(blocks)
with open(path_blog, 'w', encoding='utf-8') as f:
    f.write(blog)

# 4. Certifications Modal Fix (Use <embed> for PDFs instead of iframe)
path_certs = os.path.join(BASE, 'certifications.html')
with open(path_certs, 'r', encoding='utf-8') as f:
    certs = f.read()

certs = re.sub(
    r'el\.innerHTML=`<iframe src="\$\{c\.pdf\}"[^>]+></iframe>`;',
    r'el.innerHTML=`<embed src="${c.pdf}" type="application/pdf" style="width:100%;height:100%;border:none;">`;',
    certs
)
with open(path_certs, 'w', encoding='utf-8') as f:
    f.write(certs)

# 5. Index Awards Swap (Make Large block for Flat6Labs Accelerator / Riadi)
with open(path_index, 'r', encoding='utf-8') as f:
    index = f.read()

# Replace EGYPES details with Flat6Labs Accelerator details in the large block
old_large = r"""<img src="assets/marwan_images/Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026/marwan magdy holding the prize.png" alt="1st Place EGYPES" style="width:100%;height:100%;object-fit:cover;opacity:.75;transition:all .5s;display:block;">
            <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.4) 50%,transparent 100%);"></div>
            <div style="position:absolute;bottom:0;left:0;right:0;padding:1.75rem;">
              <div style="display:inline-flex;align-items:center;gap:.4rem;background:rgba(16,185,129,.9);color:#000;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;padding:.3rem .75rem;border-radius:50px;margin-bottom:.75rem;">&#127942; 1st Place</div>
              <h3 style="font-family:'Playfair Display',serif;font-size:1.3rem;color:#fff;line-height:1.2;margin-bottom:.35rem;">Flat6Labs &amp; Shell Intilaaqah @ EGYPES 2026</h3>
              <p style="color:#94a3b8;font-size:.82rem;">Won 1st place with Riadi · Feb 2026</p>
            </div>"""

new_large = r"""<img src="assets/marwan_images/Accelerator Program at Flat6Labs/Selected for the Accelerator Program at Flat6Labs.jpeg" alt="Flat6Labs Accelerator" style="width:100%;height:100%;object-fit:cover;opacity:.75;transition:all .5s;display:block;">
            <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.4) 50%,transparent 100%);"></div>
            <div style="position:absolute;bottom:0;left:0;right:0;padding:1.75rem;">
              <div style="display:inline-flex;align-items:center;gap:.4rem;background:rgba(16,185,129,.9);color:#000;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;padding:.3rem .75rem;border-radius:50px;margin-bottom:.75rem;">&#128640; Accelerator</div>
              <h3 style="font-family:'Playfair Display',serif;font-size:1.3rem;color:#fff;line-height:1.2;margin-bottom:.35rem;">Flat6Labs Accelerator Program</h3>
              <p style="color:#94a3b8;font-size:.82rem;">Selected with Riadi · Dec 2026</p>
            </div>"""

# Replace Accelerator details with EGYPES details in the small block
old_small = r"""<img src="assets/marwan_images/Accelerator Program at Flat6Labs/Selected for the Accelerator Program at Flat6Labs.jpeg" alt="Flat6Labs Accelerator" style="width:100%;height:100%;object-fit:cover;opacity:.7;display:block;">
            <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.3) 60%,transparent 100%);"></div>
            <div style="position:absolute;bottom:0;left:0;right:0;padding:1rem;">
              <div style="display:inline-flex;background:rgba(255,255,255,.15);backdrop-filter:blur(8px);color:#fff;font-size:.63rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;padding:.22rem .6rem;border-radius:50px;margin-bottom:.4rem;">&#128640; Accelerator</div>
              <h3 style="font-size:.88rem;color:#fff;line-height:1.25;font-weight:600;">Flat6Labs Accelerator</h3>
            </div>"""

new_small = r"""<img src="assets/marwan_images/Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026/marwan magdy holding the prize.png" alt="EGYPES 2026" style="width:100%;height:100%;object-fit:cover;opacity:.7;display:block;">
            <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.3) 60%,transparent 100%);"></div>
            <div style="position:absolute;bottom:0;left:0;right:0;padding:1rem;">
              <div style="display:inline-flex;background:rgba(16,185,129,.8);color:#000;font-size:.63rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;padding:.22rem .6rem;border-radius:50px;margin-bottom:.4rem;">&#127942; 1st Place</div>
              <h3 style="font-size:.88rem;color:#fff;line-height:1.25;font-weight:600;">Shell Intilaaqah @ EGYPES</h3>
            </div>"""

# Be careful replacing, use literal replace
if old_large in index and old_small in index:
    index = index.replace(old_large, new_large)
    index = index.replace(old_small, new_small)
else:
    print("WARNING: Could not find blocks to swap. Check the strings.")

with open(path_index, 'w', encoding='utf-8') as f:
    f.write(index)

print("Done part 4 fixes.")
