import os, re

BASE = r'D:\web\portfolio entrepreneur'
path_nav = os.path.join(BASE, 'nav.html')

with open(path_nav, 'r', encoding='utf-8') as f:
    nav = f.read()

# Replace the previous media query with a highly optimized single-row layout
new_media = '''    @media (max-width: 1024px) {
        .navbar-global { 
            height: 70px !important; 
            padding: 0 1rem !important; 
            flex-direction: row; 
            justify-content: space-between;
            align-items: center; 
            gap: 1rem;
        }
        .nav-brand { font-size: 1.25rem !important; white-space: nowrap; }
        .sliding-nav-wrapper { 
            position: relative; 
            transform: none; 
            left: auto; 
            width: auto; 
            flex-grow: 1;
            overflow-x: auto; 
            -webkit-overflow-scrolling: touch; 
            scrollbar-width: none; /* Firefox */
        }
        .sliding-nav-wrapper::-webkit-scrollbar { display: none; } /* Chrome/Safari */
        .sliding-nav { 
            display: flex; 
            flex-wrap: nowrap; 
            justify-content: flex-start;
            padding-bottom: 0; 
            border: none;
            background: transparent;
        }
        .nav-item { flex: 0 0 auto; }
        .nav-item a { padding: 0.4rem 1rem; font-size: 0.7rem; }
    }'''

nav = re.sub(r'@media\s*\(max-width:\s*1024px\)\s*\{.*?\}', new_media, nav, flags=re.DOTALL)

with open(path_nav, 'w', encoding='utf-8') as f:
    f.write(nav)

print("Nav mobile layout fixed to single-row 70px.")
