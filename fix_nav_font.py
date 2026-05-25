# Fix 1: Nav bar - consistent font + fix active state for ALL pages
nav_content = r"""<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
    .navbar-global { 
        position: fixed; top: 0; left: 0; width: 100%; height: var(--nav-height, 80px); 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 0 5%; background: rgba(3, 3, 5, 0.85); backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(255,255,255,0.05); 
        z-index: 1000; transition: transform 0.4s cubic-bezier(0.25, 1, 0.2, 1);
        font-family: 'Outfit', sans-serif;
    }
    .nav-brand { 
        font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; 
        letter-spacing: 0.05em; color: #f8fafc; text-decoration: none;
    }
    .nav-brand span { color: #10b981; }
    .sliding-nav-wrapper { position: absolute; left: 50%; transform: translateX(-50%); }
    .sliding-nav { 
        display: flex; align-items: center; list-style: none; gap: 0.4rem;
        background: rgba(255,255,255,0.02); border-radius: 50px; padding: 0.35rem; 
        border: 1px solid rgba(255,255,255,0.12); 
    }
    .nav-item a { 
        display: flex; align-items: center; justify-content: center;
        padding: 0.6rem 1.4rem; font-size: 0.75rem; text-transform: uppercase; 
        font-weight: 600; letter-spacing: 0.1em; color: #94a3b8;
        border-radius: 50px; transition: all 0.3s cubic-bezier(0.25, 1, 0.2, 1);
        text-decoration: none; font-family: 'Outfit', sans-serif;
    }
    .nav-item a:hover { color: #f8fafc; background: rgba(255,255,255,0.06); }
    .nav-item a.active { 
        background-color: #10b981; 
        color: #000000; font-weight: 700;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
    }
    @media (max-width: 1024px) { .sliding-nav { display: none; } }
</style>

<header class="navbar-global" id="navbar">
    <a href="index.html" class="nav-brand">Marwan Magdy<span>.</span></a>
    <nav class="sliding-nav-wrapper">
        <ul class="sliding-nav" id="main-nav">
            <li class="nav-item"><a href="index.html" data-page="index">Home</a></li>
            <li class="nav-item"><a href="about.html" data-page="about">About</a></li>
            <li class="nav-item"><a href="ventures.html" data-page="ventures">Ventures</a></li>
            <li class="nav-item"><a href="certifications.html" data-page="certifications">Certifications</a></li>
            <li class="nav-item"><a href="blog.html" data-page="blog">Blog</a></li>
        </ul>
    </nav>
</header>

<script>
    (function initNav() {
        const navbar = document.getElementById('navbar');
        let lastScrollTop = 0;
        const rawPage = window.location.pathname.split('/').pop().replace('.html','') || 'index';
        const currentPage = rawPage.startsWith('article-') ? 'blog' : rawPage;
        document.querySelectorAll('.nav-item a').forEach(link => {
            if (link.getAttribute('data-page') === currentPage) {
                link.classList.add('active');
            }
        });
        window.addEventListener('scroll', () => {
            let scrollY = window.pageYOffset;
            if (scrollY > lastScrollTop && scrollY > 150) {
                navbar.style.transform = 'translateY(-100%)';
            } else {
                navbar.style.transform = 'translateY(0)';
            }
            lastScrollTop = scrollY <= 0 ? 0 : scrollY;
        });
    })();
</script>
"""
with open('nav.html', 'w', encoding='utf-8') as f:
    f.write(nav_content)
print("nav.html rewritten with consistent font + correct active state")
