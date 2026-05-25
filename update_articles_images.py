import os, re

BASE = r'D:\web\portfolio entrepreneur'

# ---- GARNET ARTICLE ----
garnet_body = """
<p>Garnet_eg is a testament to pioneering spirit. We launched as one of Egypt's <strong>first dedicated local streetwear brands</strong> in 2022 — before the local fashion scene had matured, before "made in Egypt" was a badge of pride. We were <em>the pioneers</em>.</p>

<h2>Pioneering Local Streetwear in Egypt</h2>
<p>In 2022, the Egyptian streetwear market was largely dominated by international imports. Local brands were rare, and the idea of building a premium, original, home-grown label was considered a bold risk. We took that risk. Garnet_eg became one of the first Egyptian streetwear brands to pursue original design, premium quality fabrics, and a brand identity built for the global market.</p>
<p>We pioneered the concept of <strong>oversized fits with Egyptian design language</strong> — combining international streetwear aesthetics with local cultural identity. This was new territory, and we owned it.</p>

<div class="article-gallery">
<img src="assets/logo/garnet/images/garnet design 1.jpg" alt="Garnet Design 1">
<img src="assets/logo/garnet/images/garnet design 2.jpg" alt="Garnet Design 2">
</div>

<h2>The Collections</h2>
<p>Our product line explored multiple aesthetic directions — each collection telling its own story while remaining true to the Garnet_eg identity of premium, original, Egyptian-made streetwear.</p>

<div class="article-gallery">
<img src="assets/logo/garnet/images/garnet baby blue.jpg" alt="Garnet Baby Blue Collection">
<img src="assets/logo/garnet/images/garnet lavenvder.jpg" alt="Garnet Lavender Collection">
</div>
<div class="article-gallery">
<img src="assets/logo/garnet/images/garnet black.jpg" alt="Garnet Black Edition">
<img src="assets/logo/garnet/images/garnet white.jpg" alt="Garnet White Edition">
</div>

<h2>My Role: Business Development</h2>
<p>As Co-Founder and Business Developer from January 2023 to April 2025, I was responsible for every aspect of commercial growth: Go-To-Market strategy, supplier relationships, pricing models, and digital marketing. Running a physical product brand taught me lessons in unit economics, supply chain logistics, and brand positioning that directly shape how I build digital startups today.</p>
<ul>
<li>Developed and executed the full Go-To-Market strategy for launch and growth.</li>
<li>Built and managed supplier relationships ensuring high-quality, locally-sourced production.</li>
<li>Led digital marketing campaigns and managed product drop strategy.</li>
<li>Designed the financial model including COGS, pricing tiers, and margin optimization.</li>
</ul>

<h2>Legacy</h2>
<p>Garnet_eg proved that Egyptian founders can build world-class brands from the ground up. We didn't wait for the market to mature — we helped create it. That pioneering mindset carries into everything I build.</p>
"""

garnet_html = open(os.path.join(BASE, 'article-garnet.html'), encoding='utf-8').read()
# Replace old body
start = garnet_html.find('<div class="article-body">')
end = garnet_html.find('</div>\n    </main>')
if start != -1 and end != -1:
    garnet_html = garnet_html[:start] + '<div class="article-body">\n' + garnet_body + '\n        </div>' + garnet_html[end+len('</div>\n    </main>'):]
# Also add gallery CSS if not present
if 'article-gallery' not in garnet_html:
    garnet_html = garnet_html.replace('</style>', '.article-gallery{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:2rem 0}.article-gallery img{width:100%;border-radius:1rem;border:1px solid var(--color-border);height:220px;object-fit:cover}\n</style>')
with open(os.path.join(BASE, 'article-garnet.html'), 'w', encoding='utf-8') as f:
    f.write(garnet_html)
print("Garnet article updated")

# ---- AIX ARTICLE ----
aix_body = """
<p>The <strong>Huawei Developer Competition 2025 (Northern Africa)</strong> was one of the most demanding and rewarding competitions I've participated in. Out of <strong>389 teams</strong> from 10+ countries with 1,400+ participants, we secured <strong>2nd Place</strong> — and this is the story of how we got there.</p>

<div class="article-gallery">
<img src="assets/logo/aix/images/team photo when tells use we won .png" alt="Team learning we won">
<img src="assets/logo/aix/images/team photo with member of hauwei.jpeg" alt="Team with Huawei member">
</div>

<h2>The Competition</h2>
<p>The challenge required building an innovative product leveraging Huawei Cloud AI services. The judges evaluated on technical depth, commercial viability, scalability, and presentation quality. Competing regionally meant we were up against the best technical talent from Egypt, Algeria, Morocco, Tunisia, and beyond.</p>

<div class="article-gallery">
<img src="assets/logo/aix/images/marwan pitch.png" alt="Marwan pitching to judges">
<img src="assets/logo/aix/images/marwan holding all prizes.png" alt="Marwan holding prizes">
</div>

<h2>My Role: AI Technical Lead</h2>
<p>As the AI Technical Lead, I was responsible for the entire AI architecture — from selecting the right Huawei Cloud AI services, to designing the model pipeline, to ensuring the system was production-ready enough to impress the judges.</p>
<ul>
<li>Architected the full AI pipeline from concept to demo-ready product.</li>
<li>Integrated Huawei Cloud AI APIs including computer vision and NLP modules.</li>
<li>Led rapid prototyping sessions with the team over 48-hour sprints.</li>
<li>Prepared and delivered the technical pitch to the panel of Huawei judges.</li>
</ul>

<h2>The Result</h2>
<p>Winning 2nd Place across Northern Africa is a moment I'll never forget — the validation that our technical vision was world-class, and that Egyptian engineering talent can compete and win at the highest regional levels.</p>
"""

# Build full AIX article
aix_art = open(os.path.join(BASE, 'article-alx.html'), encoding='utf-8').read()  # use as template base
aix_full = open(os.path.join(BASE, 'article-huawei.html'), encoding='utf-8').read()
start = aix_full.find('<div class="article-body">')
end = aix_full.rfind('</div>\n\n    <div id="footer')
if start != -1 and end != -1:
    aix_full = aix_full[:start] + '<div class="article-body">\n' + aix_body + '\n        </div>\n\n    <div id="footer' + aix_full[end+len('</div>\n\n    <div id="footer'):]
if 'article-gallery' not in aix_full:
    aix_full = aix_full.replace('</style>', '.article-gallery{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:2rem 0}.article-gallery img{width:100%;border-radius:1rem;border:1px solid var(--color-border);height:220px;object-fit:cover}\n</style>')
with open(os.path.join(BASE, 'article-huawei.html'), 'w', encoding='utf-8') as f:
    f.write(aix_full)
print("AIX/Huawei article updated with images")

# ---- ALX ARTICLE ----
alx = open(os.path.join(BASE, 'article-alx.html'), encoding='utf-8').read()
alx_gallery = '''
        <div class="article-gallery">
            <img src="assets/logo/alx/images/alx my pif coach journey begins.jpg" alt="ALX PiF Coach Journey Begins">
        </div>
'''
# Insert gallery after first paragraph
alx = alx.replace('<div class="article-body">', '<div class="article-body">' + alx_gallery, 1)
if 'article-gallery' not in alx:
    alx = alx.replace('</style>', '.article-gallery{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:2rem 0}.article-gallery img{width:100%;border-radius:1rem;border:1px solid var(--color-border);object-fit:cover}\n</style>')
with open(os.path.join(BASE, 'article-alx.html'), 'w', encoding='utf-8') as f:
    f.write(alx)
print("ALX article updated with image")

# ---- RIADI ARTICLE — add booth image ----
riadi = open(os.path.join(BASE, 'article-riadi.html'), encoding='utf-8').read()
booth_section = '''
        <h2>Riadi at EGYPES 2026</h2>
        <p>Following our 1st place win, Riadi was proudly present at the <strong>Egypt International Exhibitions Center (EIEC)</strong> — Hall 3, Booth 3A60 inside the Shell Egypt Pavilion at EGYPES 2026. An incredible milestone to showcase Riadi to 50,000+ international attendees, 500 exhibiting companies, and 350 global sponsors.</p>
        <div class="article-gallery">
            <img src="assets/marwan_images/flat6laps/booth at EGYPES 2026 .jpeg" alt="Riadi Booth at EGYPES 2026 — EIEC Hall 3">
            <img src="assets/marwan_images/Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026/Winning 1st Place at the Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026.jpeg" alt="1st Place Win">
        </div>
        <p>Alongside the competition win, Riadi was also <strong>selected into the Flat6Labs Accelerator Program</strong> (Dec 2026) — backing our vision to digitize sports management across the Arab world.</p>
        <div class="article-gallery">
            <img src="assets/marwan_images/Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026/marwan magdy holding the prize.png" alt="Marwan holding the prize">
            <img src="assets/marwan_images/Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026/team holding the prize.png" alt="Team holding the prize">
        </div>
        <div class="article-gallery">
            <img src="assets/marwan_images/Accelerator Program at Flat6Labs/Selected for the Accelerator Program at Flat6Labs.jpeg" alt="Selected for Flat6Labs Accelerator">
        </div>
'''
if 'EGYPES 2026' not in riadi:
    # Add before closing article-body
    riadi = riadi.replace('</div>\n\n    <div id="footer', booth_section + '</div>\n\n    <div id="footer', 1)
if 'article-gallery' not in riadi:
    riadi = riadi.replace('</style>', '.article-gallery{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:2rem 0}.article-gallery img{width:100%;border-radius:1rem;border:1px solid var(--color-border);height:220px;object-fit:cover}\n</style>')
with open(os.path.join(BASE, 'article-riadi.html'), 'w', encoding='utf-8') as f:
    f.write(riadi)
print("Riadi article updated with booth + accelerator images")

# ---- AIFORLIFE ARTICLE — add image ----
aifl = open(os.path.join(BASE, 'article-aiforlife.html'), encoding='utf-8').read()
aifl_img = 'assets/marwan_images/AI for Life Human- Centered Hackathon during Cairo ICT 2025/Winning 2nd Place at the AI for Life Human- Centered Hackathon during Cairo ICT 2025.jpeg'
aifl_desc = '''<p>Awarded <strong>2nd Place</strong> in the "AI for Life" Human-Centered Hackathon at Cairo ICT 2025 for designing human-centered AI solutions focused on real-world impact — blending empathy, creativity, and technology.</p>'''
if aifl_desc not in aifl:
    aifl = aifl.replace('<div class="article-body">', '<div class="article-body">\n' + aifl_desc, 1)
with open(os.path.join(BASE, 'article-aiforlife.html'), 'w', encoding='utf-8') as f:
    f.write(aifl)
print("AI for Life article updated")

# ---- UNBOUNDED ARTICLE — add CAE image ----
unb = open(os.path.join(BASE, 'article-unbounded.html'), encoding='utf-8').read()
cae_img = '''
        <div class="article-gallery">
            <img src="assets/marwan_images/CAE Green Contest 2023/Winning 2nd Place at Credit Agricole Egypt's CAE Green Contest 2023.jpeg" alt="2nd Place CAE Green Contest 2023">
        </div>
'''
if 'CAE Green Contest 2023' not in unb:
    unb = unb.replace('</div>\n\n    <div id="footer', cae_img + '</div>\n\n    <div id="footer', 1)
if 'article-gallery' not in unb:
    unb = unb.replace('</style>', '.article-gallery{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:2rem 0}.article-gallery img{width:100%;border-radius:1rem;border:1px solid var(--color-border);object-fit:cover}\n</style>')
with open(os.path.join(BASE, 'article-unbounded.html'), 'w', encoding='utf-8') as f:
    f.write(unb)
print("Unbounded article updated with CAE image")

# ---- JUDHUR — add enpact image ----
jud = open(os.path.join(BASE, 'article-judhur.html'), encoding='utf-8').read()
enpact_img = '''
        <div class="article-gallery">
            <img src="assets/marwan_images/Enpact Hackathon/Winning Team at Enpact Hackathon, Selected for the Pre-lncubation Phase.jpeg" alt="Winning Team at Enpact Hackathon">
        </div>
'''
if 'Enpact Hackathon' not in jud:
    jud = jud.replace('</div>\n\n    <div id="footer', enpact_img + '</div>\n\n    <div id="footer', 1)
if 'article-gallery' not in jud:
    jud = jud.replace('</style>', '.article-gallery{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:2rem 0}.article-gallery img{width:100%;border-radius:1rem;border:1px solid var(--color-border);object-fit:cover}\n</style>')
with open(os.path.join(BASE, 'article-judhur.html'), 'w', encoding='utf-8') as f:
    f.write(jud)
print("Judhur article updated with enpact image")

print("\nAll articles updated!")
