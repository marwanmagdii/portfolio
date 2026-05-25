import re, json, os

BASE = r'D:\web\portfolio entrepreneur'

# 4. Fix Ventures logos (Garnet & Unbounded)
path_ventures = os.path.join(BASE, 'ventures.html')
with open(path_ventures, 'r', encoding='utf-8') as f:
    ventures_html = f.read()

# Replace the avatar with Garnet logo using simple string replace for safety
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

# Also fix any remaining Marwan avatars for Garnet
ventures_html = re.sub(
    r'<img src="[^"]+" alt="Marwan" class="v-avatar">\s*<span class="v-auth">Marwan</span>',
    r'<img src="assets/logo/garnet/garnet.png" alt="Garnet" class="v-avatar" style="border-radius:0;background:transparent;"> <span class="v-auth">Garnet_eg</span>',
    ventures_html
)

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
