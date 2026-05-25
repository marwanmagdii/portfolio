# Fix active state logic in nav — detect certifications.html and blog.html correctly
# Also remove Contact from nav (keep in home only)

with open('nav.html', 'r', encoding='utf-8') as f:
    nav = f.read()

# Remove contact nav item
nav = nav.replace(
    '            <li class="nav-item"><a href="contact.html" data-page="contact">Contact</a></li>\n',
    ''
)

# Fix active detection - handle article- pages pointing back to blog
old_js = '''        const currentPage = window.location.pathname.split('/').pop().replace('.html', '') || 'index';
        document.querySelectorAll('.nav-item a').forEach(link => {
            if (link.getAttribute('data-page') === currentPage) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });'''

new_js = '''        const rawPage = window.location.pathname.split('/').pop().replace('.html', '') || 'index';
        // Map article- pages back to blog
        const currentPage = rawPage.startsWith('article-') ? 'blog' : rawPage;
        document.querySelectorAll('.nav-item a').forEach(link => {
            const lp = link.getAttribute('data-page');
            const match = lp === currentPage;
            if (match) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });'''

nav = nav.replace(old_js, new_js)

with open('nav.html', 'w', encoding='utf-8') as f:
    f.write(nav)
print("nav.html updated")

# ---- FIX HERO PHOTO CARD VISIBILITY ----
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

old_card = '''                            <div class="hero-photo-card">
                                <h4>Marwan Magdy</h4>
                                <p>Founder & CEO · Riadi</p>
                            </div>'''

new_card = '''                            <div class="hero-photo-card" style="background:rgba(5,5,7,0.92);backdrop-filter:blur(16px);border:1px solid rgba(16,185,129,0.25);border-radius:0.875rem;padding:1rem 1.25rem;position:absolute;bottom:1.25rem;left:1.25rem;right:1.25rem;">
                                <h4 style="font-family:var(--font-body);font-size:1rem;font-weight:700;color:#f1f5f9;margin-bottom:.15rem;">Marwan Magdy</h4>
                                <p style="font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.1em;color:var(--color-brand-green);">Founder &amp; CEO &middot; Riadi</p>
                            </div>'''

if old_card in idx:
    idx = idx.replace(old_card, new_card)
    print("Hero photo card fixed")
else:
    print("Hero card pattern not found - trying alternate")
    idx = idx.replace(
        '<div class="hero-photo-card">',
        '<div class="hero-photo-card" style="background:rgba(5,5,7,0.92);backdrop-filter:blur(16px);border:1px solid rgba(16,185,129,0.25);border-radius:0.875rem;padding:1rem 1.25rem;">'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)
print("index.html saved")
