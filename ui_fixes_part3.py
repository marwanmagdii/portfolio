import re, os

BASE = r'D:\web\portfolio entrepreneur'

# 1. Fix Index Hero: Dark box, em dashes, "backed by"
path_index = os.path.join(BASE, 'index.html')
with open(path_index, 'r', encoding='utf-8') as f:
    index = f.read()

# Remove dark box from hero image
index = re.sub(
    r'<div style="position:absolute;inset:0;background:linear-gradient\(to top,rgba\(5,5,7,1\) 0%,transparent 40%\);"></div>',
    '', index
)
index = re.sub(
    r'<div style="position:absolute;inset:0;background:linear-gradient\(to top,var\(--bg\) 0%,transparent 40%\)[^>]*></div>',
    '', index
)
# If it's a different gradient at the bottom of the hero image
index = re.sub(r'<div style="position:absolute;bottom:0;left:0;right:0;height:40%;background:linear-gradient.*?"></div>', '', index)

# Replace em dashes and "backed by"
index = index.replace(
    "Founder & CEO of Riadi — backed by Flat6Labs — I'm digitizing",
    "Founder & CEO of Riadi, an accelerated company by Flat6Labs, I'm digitizing"
)
index = index.replace(
    "— backed by Flat6Labs —",
    ", accelerated by Flat6Labs,"
)
index = index.replace(" — ", ", ")

# 2. Fix Awards Grid Spacing
# The right column currently has flex:1 on the a tags, but maybe the images inside are not height:100%
# Let's ensure the image tags inside have height:100% and the a tags fill the flex container.
# Instead of flex, let's use CSS grid for the right column: grid-template-rows: 1fr 1fr
index = index.replace(
    'style="display:flex;flex-direction:column;gap:1.25rem;"',
    'style="display:grid;grid-template-rows:1fr 1fr;gap:1.25rem;height:100%;"'
)
index = index.replace(
    'style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;border:1px solid rgba(255,255,255,.1);background:#0a0a12;flex:1;"',
    'style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;border:1px solid rgba(255,255,255,.1);background:#0a0a12;height:100%;"'
)

with open(path_index, 'w', encoding='utf-8') as f:
    f.write(index)
print("Index fixes applied.")

# 3. Fix Ventures: Hero images in Garnet and Unbounded cards
path_ventures = os.path.join(BASE, 'ventures.html')
with open(path_ventures, 'r', encoding='utf-8') as f:
    ventures = f.read()

# The card image is <div class="v-img"><img src="..."></div>
# Garnet image: currently might be Marwan's image
# Replace Garnet's card image
blocks = ventures.split('<div class="v-card reveal"')
for i, b in enumerate(blocks):
    if 'Scaling Garnet_eg' in b:
        # replace the image
        blocks[i] = re.sub(
            r'<div class="v-img">.*?<img src="[^"]+".*?>',
            r'<div class="v-img">\n        <img src="assets/logo/garnet/garnet.png" alt="Garnet" style="object-fit:contain;background:#fff;padding:2rem;">',
            b, flags=re.DOTALL
        )
    if 'Unbounded:' in b or 'unbounded.html' in b:
        blocks[i] = re.sub(
            r'<div class="v-img">.*?<img src="[^"]+".*?>',
            r'<div class="v-img">\n        <img src="assets/logo/unbounded/unbounded logo.jpg" alt="Unbounded" style="object-fit:cover;">',
            b, flags=re.DOTALL
        )

ventures = '<div class="v-card reveal"'.join(blocks)
with open(path_ventures, 'w', encoding='utf-8') as f:
    f.write(ventures)
print("Ventures card images fixed.")

# 4. Certifications: Fix ALX entrepreneurship missing / PDF modal broken
# The modal fails to load PDFs cleanly sometimes. Let's make sure the PDF iframe has full height and no borders.
path_certs = os.path.join(BASE, 'certifications.html')
with open(path_certs, 'r', encoding='utf-8') as f:
    certs = f.read()

# Fix broken pdf modal logic if any
certs = certs.replace(
    'el.innerHTML=`<iframe src="${c.pdf}" sandbox="allow-scripts allow-same-origin"></iframe>`;',
    'el.innerHTML=`<iframe src="${c.pdf}" style="width:100%;height:100%;border:none;" sandbox="allow-scripts allow-same-origin"></iframe>`;'
)

with open(path_certs, 'w', encoding='utf-8') as f:
    f.write(certs)
print("Certs modal iframe styled.")

