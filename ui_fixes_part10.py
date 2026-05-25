import os

BASE = r'D:\web\portfolio entrepreneur'
path_nav = os.path.join(BASE, 'nav.html')

clean_nav = """<style>
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
        letter-spacing: 0.05em; color: #f8fafc; text-decoration: none; position: relative; z-index: 2000;
    }
    .nav-brand span { color: #10b981; }
    
    .hamburger {
        display: none; flex-direction: column; gap: 6px; cursor: pointer; z-index: 2000; padding: 10px;
    }
    .hamburger span {
        width: 28px; height: 2px; background: #fff; transition: all 0.3s cubic-bezier(0.25, 1, 0.2, 1); border-radius: 2px;
    }

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

    @media (max-width: 1024px) {
        .hamburger { display: flex; }
        .hamburger.active span:nth-child(1) { transform: translateY(8px) rotate(45deg); background: #10b981; }
        .hamburger.active span:nth-child(2) { opacity: 0; }
        .hamburger.active span:nth-child(3) { transform: translateY(-8px) rotate(-45deg); background: #10b981; }
        
        .sliding-nav-wrapper { 
            position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
            background: rgba(3,3,5,0.98); backdrop-filter: blur(20px);
            display: flex; flex-direction: column; justify-content: center; align-items: center;
            transform: translateX(100%); transition: transform 0.4s cubic-bezier(0.25, 1, 0.2, 1);
        }
        .sliding-nav-wrapper.open { transform: translateX(0); }
        .sliding-nav { 
            flex-direction: column; gap: 1.5rem; background: transparent; border: none; padding: 0; 
        }
        .nav-item a { font-size: 1.2rem; padding: 1rem 2rem; background: transparent !important; }
        .nav-item a.active { background: transparent !important; color: #10b981; box-shadow: none; text-shadow: 0 0 10px rgba(16,185,129,0.5); }
    }
</style>

<header class="navbar-global" id="navbar">
    <a href="index.html" class="nav-brand">Marwan Magdy<span>.</span></a>
    
    <div class="hamburger" id="hamburger">
        <span></span><span></span><span></span>
    </div>

    <nav class="sliding-nav-wrapper" id="nav-wrapper">
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
        const hamburger = document.getElementById('hamburger');
        const navWrapper = document.getElementById('nav-wrapper');
        
        // Active page logic
        const rawPage = window.location.pathname.split('/').pop().replace('.html','') || 'index';
        const currentPage = rawPage.startsWith('article-') ? 'blog' : rawPage;
        document.querySelectorAll('.nav-item a').forEach(link => {
            if (link.getAttribute('data-page') === currentPage) {
                link.classList.add('active');
            }
        });

        // Hamburger Menu Toggle
        if(hamburger) {
            hamburger.addEventListener('click', () => {
                hamburger.classList.toggle('active');
                navWrapper.classList.toggle('open');
                if(navWrapper.classList.contains('open')) {
                    document.body.style.overflow = 'hidden';
                } else {
                    document.body.style.overflow = '';
                }
            });
        }

        // Hide nav on scroll down
        let lastScrollTop = 0;
        window.addEventListener('scroll', () => {
            let scrollY = window.pageYOffset;
            if (scrollY > lastScrollTop && scrollY > 150 && (!navWrapper.classList.contains('open'))) {
                navbar.style.transform = 'translateY(-100%)';
            } else {
                navbar.style.transform = 'translateY(0)';
            }
            lastScrollTop = scrollY <= 0 ? 0 : scrollY;
        });
    })();
</script>
"""

with open(path_nav, 'w', encoding='utf-8') as f:
    f.write(clean_nav)

print("Nav bar hamburger menu successfully implemented.")
