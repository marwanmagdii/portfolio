import re, json, os

BASE = r'D:\web\portfolio entrepreneur'

# 1. Fix Certifications
path_certs = os.path.join(BASE, 'certifications.html')
with open(path_certs, 'r', encoding='utf-8') as f:
    certs_html = f.read()

# Parse CERTS
match = re.search(r'const CERTS=(\[.*?\]);', certs_html, re.DOTALL)
if match:
    certs = json.loads(match.group(1))
    
    # Remove the 2 certs
    to_remove = ["6.Blockchain Eyouth.pdf", "10.1. ITIDA Gigs Certifications.jpg"]
    certs = [c for c in certs if not any(x in c.get('pdf','') for x in to_remove)]
    
    # Re-inject CERTS
    certs_html = certs_html.replace(match.group(1), json.dumps(certs, ensure_ascii=False))

# Fix the PDF card placeholder look (it was too dark)
# It used to be: <div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,rgba(...,.12),rgba(...,.03));font-size:2.5rem;">💼</div>
# Let's make it brighter, bigger icon, and a glowing effect.
def brighten_placeholder(match):
    full = match.group(0)
    # increase font size and background opacity
    full = full.replace('font-size:2.5rem', 'font-size:4rem;text-shadow:0 0 20px rgba(255,255,255,0.2)')
    full = re.sub(r',([a-z\(\d,]+)\.12\)', r',\1.25)', full)
    full = re.sub(r',([a-z\(\d,]+)\.03\)', r',\1.1)', full)
    return full

certs_html = re.sub(r'<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:linear-gradient[^>]*>.*?</div>', brighten_placeholder, certs_html)

with open(path_certs, 'w', encoding='utf-8') as f:
    f.write(certs_html)
print("1. Certifications fixed.")

# 2. Fix About Hero Dark Box
path_about = os.path.join(BASE, 'about.html')
with open(path_about, 'r', encoding='utf-8') as f:
    about_html = f.read()

# Find the gradient overlay at the bottom of Marwan's image and remove it
about_html = re.sub(r'<div style="position:absolute;inset:0;background:linear-gradient\(to top,var\(--bg\) 0%,transparent 40%\);"></div>', '', about_html)
# Also try without the semicolon
about_html = re.sub(r'<div style="position:absolute;inset:0;background:linear-gradient\(to top,var\(--bg\) 0%,transparent 40%\)"></div>', '', about_html)
# Try a broader regex for any dark gradient box over the image
about_html = re.sub(r'<div style="position:absolute;inset:0;background:linear-gradient\(to top,(?:rgba|var).*?transparent.*?\)[^>]*></div>', '', about_html)
about_html = re.sub(r'<div style="position:absolute;bottom:0;left:0;right:0;height:.*?background:linear-gradient.*?"></div>', '', about_html)

with open(path_about, 'w', encoding='utf-8') as f:
    f.write(about_html)
print("2. About dark box fixed.")

# 3. Fix Index (Awards grid & Contact logos)
path_index = os.path.join(BASE, 'index.html')
with open(path_index, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Awards grid: change the 2 stacked cards container to display:flex;flex-direction:column to stretch
index_html = index_html.replace(
    'style="display:grid;grid-template-rows:1fr 1fr;gap:1.25rem;"',
    'style="display:flex;flex-direction:column;gap:1.25rem;"'
)
# Make the inner a tags flex:1
index_html = index_html.replace(
    'style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;border:1px solid rgba(255,255,255,.1);background:#0a0a12;"',
    'style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;border:1px solid rgba(255,255,255,.1);background:#0a0a12;flex:1;"'
)

# Contact logos
# We have: <div class="ci-icon">✉</div>, <div class="ci-icon">in</div>, <div class="ci-icon">🌐</div>
# Or similar in index.html
contact_html = '''        <div style="display:flex;flex-direction:column;gap:2rem;">
          <a href="mailto:marwan@riadiapp.com" class="contact-item" style="display:flex;align-items:center;gap:1.5rem;text-decoration:none;color:var(--sub);font-size:1.1rem;transition:all .3s;">
            <img src="assets/logo/social/email.png" alt="Email" style="width:36px;height:36px;object-fit:contain;opacity:0.8;">
            <span style="font-weight:500;">marwan@riadiapp.com</span>
          </a>
          <a href="#" class="contact-item" style="display:flex;align-items:center;gap:1.5rem;text-decoration:none;color:var(--sub);font-size:1.1rem;transition:all .3s;">
            <img src="assets/logo/social/linkedin.png" alt="LinkedIn" style="width:36px;height:36px;object-fit:contain;opacity:0.8;">
            <span style="font-weight:500;">LinkedIn</span>
          </a>
          <a href="https://riadiapp.com" class="contact-item" style="display:flex;align-items:center;gap:1.5rem;text-decoration:none;color:var(--sub);font-size:1.1rem;transition:all .3s;">
            <img src="assets/logo/social/internet.png" alt="Website" style="width:36px;height:36px;object-fit:contain;opacity:0.8;">
            <span style="font-weight:500;">riadiapp.com</span>
          </a>
        </div>'''
# Replace the contact column
index_html = re.sub(
    r'<div style="display:flex;flex-direction:column;gap:2rem;">.*?</div>\s*</div>\s*</div>\s*</section>',
    contact_html + '\n        </div>\n      </div>\n    </section>',
    index_html,
    flags=re.DOTALL
)

with open(path_index, 'w', encoding='utf-8') as f:
    f.write(index_html)
print("3. Index fixed (Awards spacing + Contact logos).")

# 4. Fix Ventures logos (Garnet & Unbounded)
path_ventures = os.path.join(BASE, 'ventures.html')
with open(path_ventures, 'r', encoding='utf-8') as f:
    ventures_html = f.read()

# Find Garnet card. It has an avatar: <img src="assets/marwan_images/personal/2.jpeg" alt="Marwan" class="v-avatar">
# Let's replace the avatar with Garnet logo
ventures_html = re.sub(
    r'<img src="[^"]+" alt="Marwan" class="v-avatar">\s*<span class="v-auth">Marwan</span>',
    r'<img src="assets/logo/garnet/garnet.png" alt="Garnet" class="v-avatar" style="border-radius:0;background:transparent;">\s*<span class="v-auth">Garnet_eg</span>',
    ventures_html,
    count=1 # Make sure it's Garnet
)

# Wait, the avatar replacement regex might fail if the HTML format differs.
# A safer way: find the card by its title "Scaling Garnet_eg" and replace inside it
blocks = ventures_html.split('<a href="article-')
for i, b in enumerate(blocks):
    if 'Scaling Garnet_eg' in b:
        # Replace the avatar div content
        blocks[i] = re.sub(
            r'<div class="v-foot-left">.*?</div>',
            r'<div class="v-foot-left"><img src="assets/logo/garnet/garnet.png" alt="Garnet" style="height:24px;object-fit:contain;"></div>',
            b, flags=re.DOTALL
        )
    if 'Unbounded:' in b or 'unbounded.html' in b:
        blocks[i] = re.sub(
            r'<div class="v-foot-left">.*?</div>',
            r'<div class="v-foot-left"><img src="assets/logo/unbounded/unbounded logo.jpg" alt="Unbounded" style="height:24px;border-radius:4px;object-fit:contain;"></div>',
            b, flags=re.DOTALL
        )

ventures_html = '<a href="article-'.join(blocks)
with open(path_ventures, 'w', encoding='utf-8') as f:
    f.write(ventures_html)
print("4. Ventures logos fixed.")

# 5. Fix Article Riadi Social Links
path_riadi = os.path.join(BASE, 'article-riadi.html')
with open(path_riadi, 'r', encoding='utf-8') as f:
    riadi_html = f.read()

social_html = '''
    <div style="display:flex;justify-content:center;gap:1.5rem;margin-top:1.5rem;margin-bottom:2rem;">
      <a href="#" target="_blank" style="transition:transform .2s;"><img src="assets/logo/social/facebook.png" alt="Facebook" style="width:28px;height:28px;opacity:0.8;"></a>
      <a href="mailto:marwan@riadiapp.com" style="transition:transform .2s;"><img src="assets/logo/social/email.png" alt="Email" style="width:28px;height:28px;opacity:0.8;"></a>
      <a href="https://riadiapp.com" target="_blank" style="transition:transform .2s;"><img src="assets/logo/social/internet.png" alt="Website" style="width:28px;height:28px;opacity:0.8;"></a>
    </div>
'''

if 'assets/logo/social/facebook.png' not in riadi_html:
    # Insert it right after the hero meta tags
    riadi_html = riadi_html.replace(
        '<div class="hero-meta">',
        social_html + '<div class="hero-meta">'
    )
    with open(path_riadi, 'w', encoding='utf-8') as f:
        f.write(riadi_html)
print("5. Riadi article social links added.")

# 6. Ensure Unbounded & Garnet articles have logos
path_garnet = os.path.join(BASE, 'article-garnet.html')
with open(path_garnet, 'r', encoding='utf-8') as f:
    garnet_html = f.read()
if 'assets/logo/garnet/garnet.png' not in garnet_html:
    garnet_html = garnet_html.replace(
        '<header class="article-header" style="padding-top:2rem;">',
        '<header class="article-header" style="padding-top:2rem;">\n<div style="text-align:center;margin-bottom:1.5rem;"><img src="assets/logo/garnet/garnet.png" alt="Garnet" style="height:60px;object-fit:contain;"></div>'
    )
    with open(path_garnet, 'w', encoding='utf-8') as f:
        f.write(garnet_html)

path_unb = os.path.join(BASE, 'article-unbounded.html')
with open(path_unb, 'r', encoding='utf-8') as f:
    unb_html = f.read()
if 'assets/logo/unbounded/unbounded logo.jpg' not in unb_html:
    unb_html = unb_html.replace(
        '<header class="article-header" style="padding-top:2rem;">',
        '<header class="article-header" style="padding-top:2rem;">\n<div style="text-align:center;margin-bottom:1.5rem;"><img src="assets/logo/unbounded/unbounded logo.jpg" alt="Unbounded" style="height:60px;border-radius:8px;object-fit:contain;"></div>'
    )
    with open(path_unb, 'w', encoding='utf-8') as f:
        f.write(unb_html)
print("6. Article logos verified.")

