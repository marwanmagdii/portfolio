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
        
        .article-cover {{ width: 100%; height: 500px; border-radius: 1.5rem; overflow: hidden; margin: 4rem 0; border: 1px solid var(--color-border); }}
        .article-cover img {{ width: 100%; height: 100%; object-fit: cover; opacity: 0.9; }}
        
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

        <div class="article-cover">
            <img src="{cover_image}" alt="{title}">
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
        "filename": "article-riadi.html",
        "title": "Winning 1st Place at EGYPES 2026 with Riadi",
        "tag": "Entrepreneurship & Sports Tech",
        "date": "Feb 2026",
        "cover_image": "assets/marwan_images/Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026/Winning 1st Place at the Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026.jpeg",
        "body": """
        <p>I am incredibly proud to announce that <strong>Riadi</strong> has won 1st Place at the Flat6Labs and Shell Intilaaqah Competition during EGYPES 2026! This marks a major milestone for our team and our vision for the future of sports technology in the Arab world.</p>
        
        <h2>The Journey to EGYPES</h2>
        <p>Building Riadi has been a journey of extreme dedication. We noticed a massive gap in how sports venues, tournaments, and athletic performance are managed across the region. With Riadi, our goal is to build an ecosystem that digitizes every aspect of a sports facility's operations.</p>
        <p>Going into EGYPES 2026, we knew we had to refine our Lean Canvas and ensure our B2B strategy was flawless. The judges were looking for scalable, innovative solutions, and our rigorous preparation paid off.</p>
        
        <h2>What This Means for Riadi</h2>
        <p>Securing 1st place isn't just about the award—it's about the incredible backing we now have. With the support of Flat6Labs and Shell Intilaaqah, we are accelerating our go-to-market strategy and expanding our reach.</p>
        <ul>
            <li>Accelerated product iteration using Flutter & Firebase.</li>
            <li>Expanding our B2B sales and partnerships.</li>
            <li>Onboarding new sports facilities to digitize their management.</li>
        </ul>
        <p>This is just the beginning. I am deeply thankful to the entire team, our mentors, and the ecosystem for believing in us.</p>
        """
    },
    {
        "filename": "article-huawei.html",
        "title": "2nd Place Across Northern Africa at Huawei Developer Competition",
        "tag": "AI & Innovation",
        "date": "Dec 2025",
        "cover_image": "assets/marwan_images/Huawei Developer Competition 2025 Northern Africa/Winning 2nd Place across North Africa at the Huawei Developer Competition 2025 Northern Africa.jpeg",
        "body": """
        <p>Out of 389 teams, representing over 1,400 participants from more than 10 countries across Northern Africa, our team secured <strong>2nd Place</strong> at the prestigious Huawei Developer Competition 2025!</p>
        
        <h2>The Challenge</h2>
        <p>The competition was fierce, bringing together top talent from across the continent to build innovative solutions using Huawei Cloud. We focused on AI integration and architectural scalability. The pressure was immense, but our engineering instinct and strategic planning guided us through.</p>
        
        <div class="article-gallery">
            <img src="assets/marwan_images/Huawei Developer Competition 2025 Northern Africa/Huawei Developer Competition 2025.jpeg" alt="Huawei Dev Comp">
            <img src="assets/marwan_images/Huawei Developer Competition 2025 Northern Africa/Winning 2nd Place across North Africa at the Huawei Developer Competition 2025 Northern Africa.jpeg" alt="Huawei Dev Comp Win">
        </div>
        
        <h2>Execution and AI Integration</h2>
        <p>We built a product that demonstrated real commercial value and deep technical capability. Leading the AI integration from concept to competition-ready product required a lot of rapid prototyping, testing, and Vibe Coding. We ensured our system architecture was robust enough to impress the judges.</p>
        <p>I want to thank Huawei for hosting such a massive and inspiring platform. Competing on a regional scale has given us incredible insights and connections.</p>
        """
    },
    {
        "filename": "article-aiforlife.html",
        "title": "2nd Place at 'AI for Life' Human-Centered Hackathon",
        "tag": "Human-Centered AI",
        "date": "Nov 2025",
        "cover_image": "assets/marwan_images/AI for Life Human- Centered Hackathon during Cairo ICT 2025/Winning 2nd Place at the AI for Life Human- Centered Hackathon during Cairo ICT 2025.jpeg",
        "body": """
        <p>What an incredible experience at Cairo ICT 2025! My team and I won <strong>2nd Place</strong> at the "AI for Life" Human-Centered Hackathon.</p>
        
        <h2>Designing for Humanity</h2>
        <p>Our focus was on designing AI solutions that truly serve people. We believe that technology should blend empathy, creativity, and robust engineering to solve real human problems. We didn't just want to build something technically impressive; we wanted to build something that mattered.</p>
        
        <div class="article-gallery">
            <img src="assets/marwan_images/AI for Life Human- Centered Hackathon during Cairo ICT 2025/AI for Life Hackathon.jpg" alt="AI Hackathon">
            <img src="assets/marwan_images/AI for Life Human- Centered Hackathon during Cairo ICT 2025/Winning 2nd Place at the AI for Life Human- Centered Hackathon during Cairo ICT 2025.jpeg" alt="Cairo ICT">
        </div>
        
        <h2>The Pitch</h2>
        <p>Pitching our solution to the panel required us to articulate the human impact clearly while demonstrating the underlying ML/DL models. The intersection of tech and humanity is where real impact is made, and this hackathon proved that empathetic design combined with AI can create powerful results.</p>
        """
    },
    {
        "filename": "article-nasa.html",
        "title": "Global Nominee & Local Winner at NASA Space Apps 2024",
        "tag": "Sustainability & Tech",
        "date": "Oct 2024",
        "cover_image": "assets/marwan_images/NASA space Apps Cairo 2024/Global nominee and Local Winner at NASA space Apps Cairo 2024.jpeg",
        "body": """
        <p>Out of 500+ teams, my team, Green Pulse, won the <strong>NASA Space Apps Cairo 2024</strong> local competition and was officially chosen as a <strong>Global Nominee & Local Winner</strong>!</p>
        
        <h2>Tackling Climate Change</h2>
        <p>We developed a sustainability-focused tech solution leveraging NASA open datasets and geospatial tools. As the team leader, I am incredibly proud of my team, who worked tirelessly to address a planetary-scale challenge.</p>
        
        <div class="article-gallery">
            <img src="assets/marwan_images/NASA space Apps Cairo 2024/Global nominee and Local Winner at NASA space Apps Cairo 2024.jpeg" alt="NASA Team">
            <img src="assets/marwan_images/NASA space Apps Cairo 2024/NASA space Apps Cairo 2024.jpg" alt="NASA Event">
        </div>
        
        <h2>From Cairo to the Globe</h2>
        <p>Advancing from local winners to Global Nominees, representing Egypt on the world stage, is an honor. This hackathon tested our ability to ideate rapidly, process massive datasets, and frame a solution that could have a real-world impact on climate change.</p>
        """
    }
]

for article in articles:
    html = template.format(**article)
    with open(article["filename"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {article['filename']}")
