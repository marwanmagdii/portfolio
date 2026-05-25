import os, re

BASE = r'D:\web\portfolio entrepreneur'

# 1. Fix nav.html mobile layout
path_nav = os.path.join(BASE, 'nav.html')
with open(path_nav, 'r', encoding='utf-8') as f:
    nav = f.read()

# Replace the media query block
new_media = '''    @media (max-width: 1024px) {
        .navbar-global { 
            height: auto !important; 
            padding: 1rem 5% !important; 
            flex-direction: column; 
            align-items: center; 
            gap: 1rem; 
        }
        .sliding-nav-wrapper { 
            position: relative; 
            transform: none; 
            left: auto; 
            width: 100%; 
            overflow-x: auto; 
            -webkit-overflow-scrolling: touch; 
        }
        .sliding-nav { 
            display: flex; 
            flex-wrap: nowrap; 
            justify-content: flex-start;
            padding-bottom: 0.5rem; 
        }
        .nav-item { flex: 0 0 auto; }
        .nav-brand { font-size: 1.5rem !important; }
    }'''

nav = re.sub(r'@media\s*\(max-width:\s*1024px\)\s*\{.*?\}', new_media, nav, flags=re.DOTALL)

with open(path_nav, 'w', encoding='utf-8') as f:
    f.write(nav)

# 2. Fix certifications freezing issue in rebuild_certs.py
path_rebuild = os.path.join(BASE, 'rebuild_certs.py')
with open(path_rebuild, 'r', encoding='utf-8') as f:
    rebuild = f.read()

# Replace the iframe logic with a nice download/view button
old_iframe = r"""else if(c.pdf&&c.pdf.endsWith('.pdf'))el.innerHTML=`<iframe src="${{c.pdf}}" sandbox="allow-scripts allow-same-origin"></iframe>`;"""
new_btn = r"""else if(c.pdf&&c.pdf.endsWith('.pdf'))el.innerHTML=`<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;background:#111;text-align:center;"><div style="font-size:3rem;margin-bottom:1rem;">📄</div><a href="${{c.pdf}}" target="_blank" style="background:#10b981;color:#000;padding:0.75rem 1.5rem;border-radius:50px;text-decoration:none;font-weight:700;font-size:0.9rem;transition:transform 0.3s;">View Certificate PDF</a></div>`;"""

rebuild = rebuild.replace(old_iframe, new_btn)

with open(path_rebuild, 'w', encoding='utf-8') as f:
    f.write(rebuild)

print("Running rebuild_certs.py to regenerate certifications.html...")
import subprocess
subprocess.run(['python', 'rebuild_certs.py'], cwd=BASE)

print("Fixes applied.")
