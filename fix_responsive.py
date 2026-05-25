import os, re

BASE = r'D:\web\portfolio entrepreneur'

# --- 1. Fix nav.html ---
path_nav = os.path.join(BASE, 'nav.html')
with open(path_nav, 'r', encoding='utf-8') as f:
    nav = f.read()

# Make the nav horizontally scrollable on mobile instead of hiding it
nav = re.sub(
    r'@media\s*\(max-width:\s*1024px\)\s*\{\s*\.sliding-nav\s*\{\s*display:\s*none;\s*\}\s*\}',
    r'''@media (max-width: 1024px) {
        .sliding-nav-wrapper { width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; }
        .sliding-nav { display: flex; flex-wrap: nowrap; padding-bottom: 0.5rem; justify-content: flex-start !important; }
        .nav-item { flex: 0 0 auto; }
        .nav-brand { font-size: 1.5rem !important; }
        .navbar-global { flex-direction: column; gap: 1rem; align-items: flex-start; padding: 1.5rem !important; }
    }''',
    nav
)

with open(path_nav, 'w', encoding='utf-8') as f:
    f.write(nav)


# --- 2. Fix index.html inline grids ---
path_index = os.path.join(BASE, 'index.html')
with open(path_index, 'r', encoding='utf-8') as f:
    index = f.read()

# A. Replace inline styles with classes in the HTML
index = index.replace(
    'style="display:grid;grid-template-columns:1.4fr 1fr;gap:1.25rem;margin-bottom:1.25rem;align-items:stretch;"',
    'class="awards-row-1"'
)
index = index.replace(
    'style="display:grid;grid-template-rows:1fr 1fr;gap:1.25rem;height:100%;"',
    'class="awards-side-col"'
)
index = index.replace(
    'style="display:grid;grid-template-columns:repeat(4,1fr);gap:1.25rem;"',
    'class="awards-row-2"'
)
index = index.replace(
    'style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;"',
    'class="contact-grid-main"'
)

# B. Inject CSS for these classes in the <style> block
responsive_css = '''
        .awards-row-1 { display: grid; grid-template-columns: 1.4fr 1fr; gap: 1.25rem; margin-bottom: 1.25rem; align-items: stretch; }
        .awards-side-col { display: grid; grid-template-rows: 1fr 1fr; gap: 1.25rem; height: 100%; }
        .awards-row-2 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem; }
        .contact-grid-main { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }

        @media (max-width: 1024px) {
            .awards-row-1 { grid-template-columns: 1fr; }
            .awards-row-2 { grid-template-columns: repeat(2, 1fr); }
            .contact-grid-main { grid-template-columns: 1fr; gap: 2rem; }
        }
        @media (max-width: 768px) {
            .awards-row-2 { grid-template-columns: 1fr; }
            .awards-side-col { grid-template-rows: auto auto; height: auto; }
            .hero-title { font-size: 3rem !important; }
        }
'''

# Find the closing </style> and insert the CSS right before it
if '</style>' in index:
    # ensure we don't insert it multiple times if run again
    if '.awards-row-1' not in index:
        index = index.replace('</style>', responsive_css + '</style>', 1)

with open(path_index, 'w', encoding='utf-8') as f:
    f.write(index)


# --- 3. Fix footer.html padding/flex ---
path_footer = os.path.join(BASE, 'footer.html')
with open(path_footer, 'r', encoding='utf-8') as f:
    footer = f.read()

if '@media' not in footer:
    footer = footer.replace('</style>', '''
    @media (max-width: 768px) {
        .footer-wrapper { flex-direction: column; text-align: center; gap: 1.5rem; }
        .footer-links { flex-direction: column; gap: 1rem; }
        .global-footer { padding: 3rem 5% 2rem 5%; }
    }
</style>''')

with open(path_footer, 'w', encoding='utf-8') as f:
    f.write(footer)

print("Responsive fixes applied successfully.")
