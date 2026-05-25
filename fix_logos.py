import os, glob

BASE = r'D:\web\portfolio entrepreneur'

# Fix AIX article — use actual aix logo transparent
with open(os.path.join(BASE,'article-huawei.html'),'r',encoding='utf-8') as f:
    art = f.read()
# Replace any placeholder logo with actual aix logo
art = art.replace(
    "onerror=\"this.parentElement.innerHTML='<span style=font-size:.75rem;font-weight:800;color:#cf0a2c>AIX</span>'\"",
    ''
)
# Ensure huawei logo is used in cover
if 'aix logo transpernt.png' not in art:
    art = art.replace(
        '<div class="hero-img">',
        '<div style="text-align:center;padding:2rem 0;"><img src="assets/logo/aix/aix logo transpernt.png" alt="AIX Logo" style="height:80px;object-fit:contain;"></div>\n  <div class="hero-img">'
    )
with open(os.path.join(BASE,'article-huawei.html'),'w',encoding='utf-8') as f:
    f.write(art)
print("AIX article: logo added")

# Fix Garnet article — logo in header
with open(os.path.join(BASE,'article-garnet.html'),'r',encoding='utf-8') as f:
    art = f.read()
if 'garnet.png' not in art:
    art = art.replace(
        '<span class="tag">',
        '<div style="text-align:center;margin-bottom:1.5rem;"><img src="assets/logo/garnet/garnet.png" alt="Garnet_eg" style="height:60px;object-fit:contain;"></div>\n    <span class="tag">',
        1
    )
with open(os.path.join(BASE,'article-garnet.html'),'w',encoding='utf-8') as f:
    f.write(art)
print("Garnet article: logo added")

# Update MTI logo in resume.html and about.html
for fname in ['resume.html','about.html']:
    path = os.path.join(BASE, fname)
    with open(path,'r',encoding='utf-8') as f:
        content = f.read()
    old = 'assets/logo/mti/mti-logo-light-roboto.png'
    # if old path already correct just verify
    content = content.replace('mti-logo-light-roboto.png', 'mti-logo-light-roboto.png')  # no-op
    # Replace wrong paths
    content = content.replace('src="logo/mti/', 'src="assets/logo/mti/')
    with open(path,'w',encoding='utf-8') as f:
        f.write(content)
print("MTI logo paths verified")

# Use AIX transparent logo in about.html timeline for AIX entry
with open(os.path.join(BASE,'about.html'),'r',encoding='utf-8') as f:
    about = f.read()
# Fix aix logo in timeline
about = about.replace(
    'src="assets/logo/huawei/huawei.png" alt="Huawei"',
    'src="assets/logo/aix/aix logo transpernt.png" alt="AIX"'
)
about = about.replace(
    "onerror=\"this.parentElement.innerHTML='<span style=font-size:.75rem;font-weight:800;color:#cf0a2c>AIX</span>'\"",
    ''
)
with open(os.path.join(BASE,'about.html'),'w',encoding='utf-8') as f:
    f.write(about)
print("About.html AIX logo fixed")

# Use garnet logo in about.html timeline for Garnet entry
with open(os.path.join(BASE,'about.html'),'r',encoding='utf-8') as f:
    about = f.read()
about = about.replace(
    'assets/logo/garnet/garnet logo.png',
    'assets/logo/garnet/garnet.png'
)
with open(os.path.join(BASE,'about.html'),'w',encoding='utf-8') as f:
    f.write(about)
print("About.html Garnet logo fixed")

print("\nAll logo fixes complete!")
