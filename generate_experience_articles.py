import os

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Marwan Magdy Blog</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --color-bg: #030305;
            --color-surface: rgba(15, 15, 20, 0.6);
            --color-text-primary: #f8fafc;
            --color-text-secondary: #94a3b8;
            --color-border: rgba(255, 255, 255, 0.2);
            --color-brand-green: #10b981;
            --color-brand-blue: #3b82f6;
            --font-heading: 'Playfair Display', serif;
            --font-body: 'Outfit', sans-serif;
            --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background-color: var(--color-bg); color: var(--color-text-primary); font-family: var(--font-body); line-height: 1.6; overflow-x: hidden; }}
        
        .bg-glow {{ position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: -1; }}
        .bg-glow::before {{ content: ''; position: absolute; border-radius: 50%; filter: blur(120px); opacity: 0.1; width: 600px; height: 600px; background: var(--color-brand-green); top: -100px; right: -100px; }}
        
        .container {{ max-width: 900px; margin: 0 auto; padding: 0 5%; }}
        
        .article-header {{ text-align: center; padding: 10rem 0 4rem 0; border-bottom: 1px solid var(--color-border); }}
        .article-tag {{ display: inline-block; padding: 0.5rem 1.2rem; border-radius: 50px; border: 1px solid rgba(16,185,129,0.3); color: var(--color-brand-green); font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; background: rgba(16,185,129,0.05); margin-bottom: 1.5rem; }}
        .article-title {{ font-family: var(--font-heading); font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 1.5rem; line-height: 1.1; }}
        .article-meta {{ display: flex; align-items: center; justify-content: center; gap: 1rem; color: var(--color-text-secondary); font-size: 0.95rem; }}
        .article-author-img {{ width: 40px; height: 40px; border-radius: 50%; object-fit: cover; border: 1px solid var(--color-brand-green); }}
        
        .article-cover {{ width: 100%; height: 500px; border-radius: 1.5rem; overflow: hidden; margin: 4rem 0; border: 1px solid var(--color-border); display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.5); }}
        .article-cover img {{ width: 100%; height: 100%; object-fit: contain; opacity: 0.9; }}
        
        .article-body {{ font-size: 1.15rem; line-height: 1.8; color: #cbd5e1; padding-bottom: 6rem; }}
        .article-body h2 {{ font-family: var(--font-heading); font-size: 2rem; color: #fff; margin: 3rem 0 1.5rem 0; }}
        .article-body p {{ margin-bottom: 1.5rem; }}
        .article-body ul {{ margin-bottom: 1.5rem; padding-left: 1.5rem; }}
        .article-body li {{ margin-bottom: 0.5rem; }}
        
        .article-gallery {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 3rem 0; }}
        .article-gallery img {{ width: 100%; border-radius: 1rem; border: 1px solid var(--color-border); }}
        
        .back-link {{ display: inline-flex; align-items: center; gap: 0.5rem; color: var(--color-text-secondary); text-decoration: none; font-weight: 500; margin-bottom: 2rem; transition: color 0.3s; }}
        .back-link:hover {{ color: var(--color-brand-green); }}
        .back-link svg {{ width: 18px; height: 18px; }}

        @media (max-width: 768px) {{
            .article-cover {{ height: 300px; }}
            .article-gallery {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="bg-glow"></div>
    <div id="nav-placeholder"></div>

    <main class="container">
        <header class="article-header">
            <a href="blog.html" class="back-link">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                Back to Articles
            </a>
            <div>
                <span class="article-tag">{tag}</span>
                <h1 class="article-title">{title}</h1>
                <div class="article-meta">
                    <img src="assets/marwan_images/personal/main image.png" alt="Marwan" class="article-author-img">
                    <span>By Marwan Magdy</span>
                    <span>&bull;</span>
                    <span>{date}</span>
                </div>
            </div>
        </header>

        <div class="article-cover" style="background: {cover_bg}">
            <img src="{cover_image}" alt="{title}" style="object-fit: {object_fit}; padding: {img_padding};">
        </div>

        <div class="article-body">
            {body}
        </div>
    </main>

    <div id="footer-placeholder"></div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            fetch('nav.html').then(r => r.text()).then(data => {{
                const temp = document.createElement('div'); temp.innerHTML = data;
                const ph = document.getElementById('nav-placeholder');
                while (temp.firstChild) {{
                    const child = temp.firstChild;
                    if (child.tagName === 'SCRIPT') {{
                        const s = document.createElement('script');
                        s.textContent = child.textContent;
                        document.body.appendChild(s);
                        temp.removeChild(child);
                    }} else {{ ph.appendChild(child); }}
                }}
            }});
            fetch('footer.html').then(r => r.text()).then(d => document.getElementById('footer-placeholder').innerHTML = d);
        }});
    </script>
</body>
</html>"""

articles = [
    {
        "filename": "article-alx.html",
        "title": "Mentoring the Next Generation of Tech Leaders at ALX",
        "tag": "Leadership & Mentoring",
        "date": "Apr 2026 - Present",
        "cover_image": "assets/logo/alx/alx.svg",
        "cover_bg": "#fff",
        "object_fit": "contain",
        "img_padding": "4rem",
        "body": """
        <p>Mentoring aspiring tech professionals within the ALX pan-African ecosystem has been an incredibly rewarding experience. Guiding young engineers through the complexities of software development and career navigation allows me to give back to the community.</p>
        
        <h2>Fostering Growth</h2>
        <p>At ALX, I focus on instilling agile methodologies, robust engineering principles, and a strong problem-solving mindset. Our sessions cover deep dives into system architecture, product thinking, and how to effectively transition from a junior developer into a leadership role.</p>
        <ul>
            <li>Providing 1:1 coaching for technical and career growth.</li>
            <li>Leading group sessions on modern frameworks and state management.</li>
            <li>Guiding students through real-world portfolio projects and startup ideation.</li>
        </ul>
        <p>Watching these aspiring professionals grow into confident software engineers is the true highlight of this role.</p>
        """
    },
    {
        "filename": "article-garnet.html",
        "title": "Scaling Garnet_eg: A Premium Streetwear Brand",
        "tag": "Business Development",
        "date": "Jan 2023 - Apr 2025",
        "cover_image": "assets/marwan_images/personal/main image.png",
        "cover_bg": "#111",
        "object_fit": "cover",
        "img_padding": "0",
        "body": """
        <p>Co-founding Garnet_eg was my first deep dive into physical product development and e-commerce. As the Business Developer, I was responsible for taking a premium streetwear concept and turning it into a recognizable brand in the competitive Egyptian market.</p>
        
        <h2>Building a Brand from Scratch</h2>
        <p>From day one, the focus was on the <strong>business model</strong> and <strong>growth strategy</strong>. We had to understand our customer demographic, negotiate with suppliers, and ensure our supply chain was solid. The local streetwear scene is fast-paced, so establishing strong partnerships was critical.</p>
        <ul>
            <li>Designed and executed the Go-To-Market (GTM) strategy.</li>
            <li>Built and managed supplier relationships for high-quality production.</li>
            <li>Executed digital marketing campaigns and managed product drops.</li>
        </ul>
        <p>The lessons learned from scaling a physical product brand directly translated into how I now architect digital startups: agility, quality, and strong unit economics are paramount.</p>
        """
    },
    {
        "filename": "article-judhur.html",
        "title": "Judhur: Connecting Tourists with Rural Egyptian Heritage",
        "tag": "Sustainable Tourism",
        "date": "2024",
        "cover_image": "assets/logo/enpact/enpact logo.png",
        "cover_bg": "#fff",
        "object_fit": "contain",
        "img_padding": "4rem",
        "body": """
        <p>Judhur (Juzur) was born out of a desire to promote sustainable tourism while empowering local Egyptian communities. The idea was simple but powerful: connect international and local tourists directly with rural communities for immersive experiences.</p>
        
        <h2>The ETENA Idea Marathon</h2>
        <p>Out of over 100 applications, Judhur was selected to join the ETENA Tourism Idea Marathon powered by the TUI Care Foundation and enpact. We competed against 25 teams and were chosen as one of the 12 winning startups to advance into the pre-incubation phase.</p>
        <ul>
            <li>Turned a concept into a working prototype and Minimum Viable Product (MVP).</li>
            <li>Developed robust financial modeling and a clear go-to-market strategy.</li>
            <li>Learned the legalities of operating a digital tourism startup in Egypt.</li>
        </ul>
        <p>The journey with Judhur highlighted the immense potential of tech to preserve heritage, create jobs, and offer tourists authentic, unforgettable experiences.</p>
        """
    },
    {
        "filename": "article-greenpulse.html",
        "title": "Green Pulse: Gamifying Recycling in Egypt",
        "tag": "Green Tech Startup",
        "date": "2024",
        "cover_image": "assets/marwan_images/NASA space Apps Cairo 2024/Global nominee and Local Winner at NASA space Apps Cairo 2024.jpeg",
        "cover_bg": "#111",
        "object_fit": "cover",
        "img_padding": "0",
        "body": """
        <p>Green Pulse is a green tech mobile application that I co-founded and lead-developed. Our mission is to solve the waste management challenge in Egypt by making recycling accessible, habitual, and rewarding.</p>
        
        <h2>Architecting the Solution</h2>
        <p>As the Lead Developer, I took the app from initial wireframes to a fully functional mobile product. The core mechanism connects households with nearby recycling collection services. We implemented a gamified reward system to encourage users to recycle consistently.</p>
        <ul>
            <li>Full-stack mobile development using Flutter and Firebase.</li>
            <li>Accessibility-first UI and UX design.</li>
            <li>Integration of geospatial tracking for waste collection routing.</li>
        </ul>
        <p>Interestingly, Green Pulse was also the name we used for our team at NASA Space Apps Cairo 2024, where we won Local Winner and Global Nominee for a separate climate tech solution. Green Pulse represents a persistent drive towards sustainability.</p>
        """
    },
    {
        "filename": "article-cae.html",
        "title": "Ensuring Flawless Banking Experiences at Crédit Agricole Egypt",
        "tag": "Quality Assurance",
        "date": "Jan - Feb 2024",
        "cover_image": "assets/logo/cae/cae main logo.jpg",
        "cover_bg": "#fff",
        "object_fit": "contain",
        "img_padding": "4rem",
        "body": """
        <p>Working on-site as a Software Quality Assurance Tester for Crédit Agricole Egypt (CAE) was a masterclass in enterprise-grade security and reliability. I was responsible for ensuring that the bank's digital products functioned flawlessly for hundreds of thousands of users.</p>
        
        <h2>Testing High-Stakes Financial Products</h2>
        <p>My core responsibilities revolved around testing three primary products: the Banki Mobile application, the Banki Wallet, and the main banking website platform.</p>
        <ul>
            <li><strong>Banki Wallet:</strong> Validated payment gateways and seamless transaction flows.</li>
            <li><strong>Banki Mobile:</strong> Conducted extensive manual testing focusing on UI responsiveness, security, and functional reliability.</li>
            <li><strong>Web Platform:</strong> Ensured cross-browser compatibility and a flawless customer experience.</li>
        </ul>
        <p>This experience solidified my understanding of how critical rigorous QA is, especially when dealing with financial data and large-scale enterprise deployments.</p>
        """
    },
    {
        "filename": "article-unbounded.html",
        "title": "Unbounded: Empowering Individuals with Disabilities",
        "tag": "Accessibility App",
        "date": "Aug - Nov 2023",
        "cover_image": "assets/marwan_images/personal/main image.png",
        "cover_bg": "#111",
        "object_fit": "cover",
        "img_padding": "0",
        "body": """
        <p>Unbounded was an incredibly fulfilling project where I served as the Lead Developer and Team Leader. We built a Flutter and Firebase mobile application designed to connect individuals with disabilities to equal job opportunities.</p>
        
        <h2>Winning the CAE Green ESG Contest</h2>
        <p>The app was designed with an accessibility-first mindset. We incorporated color-blindness themes, high-contrast typography, and voice-assisted navigation to ensure the app was usable by everyone.</p>
        <p>Our hard work culminated in winning <strong>2nd Place</strong> at the Crédit Agricole Egypt Green ESG Contest 2023. Pitching the product to the panel of judges and demonstrating the real-world impact of the app was an unforgettable moment in my early career.</p>
        <ul>
            <li>Led the full development lifecycle from Figma to production.</li>
            <li>Engineered custom accessibility features directly into the Flutter UI.</li>
            <li>Successfully pitched the ESG-focused startup concept to banking executives.</li>
        </ul>
        """
    }
]

for article in articles:
    html = template.format(**article)
    with open(article["filename"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {article['filename']}")
