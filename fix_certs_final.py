import json, re

# Map of cert ID -> thumbnail image (from certifications folder)
THUMB = {
    'ALX-FAD-C4-2024': 'assets/certifications/Founder Academy Deep Dive C4 ALX Ventures.png',
    'MCK-FWD-2024': 'assets/certifications/McKinsey_Forward_Program_Badge.pdf',
    'ALM-MMBA-ENT-2023': 'assets/certifications/Mini MBA in Entrepreneurship-almentor.jpg',
    'FWD-SUB-2023': 'assets/certifications/Business and Start Up Booster Forward Inc.pdf',
    'EYT-BBM-2023': 'assets/certifications/Balanced Business Model Eyouth.pdf',
    'ALM-SME-2024': 'assets/certifications/Create Strategy for Small and Medium Enterprises-almentor.jpg',
    'ALM-ENT20-2023': 'assets/certifications/Entrepreneurship 2.0_ Build Your Business Model Canvas-almentor.jpg',
    'EYT-ECO-2023': 'assets/certifications/Entrepreneurship Ecosystem Eyouth.pdf',
    'TIEC-IE-2023': 'assets/certifications/Innov Egypt Entrepreneurship Program TIEC.pdf',
    'ALM-PITCH-2023': 'assets/certifications/Pitching Your Business Idea-almentor.jpg',
    'ALX-PM-2024': 'assets/certifications/Project Management Crash Course ALX.png',
    'DEPI-BET-2024': 'assets/certifications/Business English Track DEPI OTO Courses.pdf',
    'DEPI-AMIT-QA-2024': 'assets/certifications/Software Tester DEPI AMIT.pdf',
    'DEPI-R2-AMIT-2024': 'assets/certifications/DEPI Round 2 Graduation Ceremony AMIT.pdf',
    'ZC-AI-2023': 'assets/certifications/AI Zewail City.pdf',
    'IMP-AI-2023': 'assets/certifications/Intro to AI and Applications Impact.pdf',
    'ITIDA-GIGS-2024': 'assets/certifications/10. ITIDA Gigs Certifications.jpg',
    'UDA-DMC-2023': 'assets/certifications/Digital Marketing Challenger Udacity.pdf',
    'HUAWEI-DC25-NA-2ND': 'assets/certifications/Huawei Developer Competition 2025 Northern Africa Huawei.png',
    'NASA-SAC-2024-GLOBAL': 'assets/certifications/NASA Space Apps Challenge 2024.pdf',
    'NASA-SAC-CAIRO-2024': 'assets/certifications/NASA Space Apps Cairo Hackathon 2024.pdf',
    'NASA-SAC-BOOT-2025': 'assets/certifications/NASA Space Apps Cairo Bootcamp 2025 NASA Space Apps Cairo.pdf',
    'CAIROICT-AIL-2ND-2025': 'assets/certifications/AI for Life Hackathon Cairo ICT.pdf',
    'NU-EGNITE-2024': 'assets/certifications/E-Gnite Bootcamp and Competition Nile University.png',
    'CAE-ESG-2ND-2023': 'assets/certifications/ESG Contest Credit Agricole Bank.pdf',
    'F6L-RIADI-2026': 'assets/certifications/Flat6Labs.pdf',
    'ASDWU-AYS-2023': 'assets/certifications/Arab Youth Summit Arab Sustainable Development Week Union.pdf',
}

# Key learnings per cert (researched)
LEARNINGS = {
    'ALX-FAD-C4-2024': ['Lean startup methodology and rapid MVP validation', 'Investor relations and startup pitch structuring', 'ALX Ventures ecosystem: mentorship, community, and growth resources'],
    'MCK-FWD-2024': ['McKinsey problem-solving frameworks and structured thinking', 'Leadership under pressure and cross-functional team management', 'Data-driven decision making and communication'],
    'ALM-MMBA-ENT-2023': ['Business model design from idea to scale', 'Financial forecasting and startup unit economics', 'Market analysis and competitive positioning strategies'],
    'FWD-SUB-2023': ['Startup ecosystem fundamentals and venture lifecycle', 'Building and scaling teams in early-stage companies', 'Go-to-market execution for B2B and B2C startups'],
    'EYT-BBM-2023': ['Lean Canvas and Business Model Canvas frameworks', 'Customer segment identification and value proposition design', 'Revenue stream optimization for sustainable growth'],
    'ALM-SME-2024': ['Competitive strategy frameworks (Porter\'s Five Forces, SWOT)', 'Growth strategies tailored for small and medium enterprises', 'Strategic planning cycles and KPI design'],
    'ALM-ENT20-2023': ['Business Model Canvas: 9-block deep-dive', 'Customer discovery and problem-solution fit', 'Pivoting strategies and iterative product development'],
    'EYT-ECO-2023': ['Startup ecosystem mapping: investors, accelerators, incubators', 'Funding stages: bootstrapping, angel, seed, Series A', 'Role of government and corporate innovation programs in Egypt'],
    'TIEC-IE-2023': ['Egyptian innovation ecosystem and TIEC\'s role in supporting startups', 'Technology entrepreneurship and digital transformation tracks', 'Mentorship and networking within Egypt\'s startup ecosystem'],
    'ALM-PITCH-2023': ['Pitch deck structure: problem, solution, traction, ask', 'Storytelling techniques for investor presentations', 'Handling investor objections and Q&A preparation'],
    'ALX-PM-2024': ['Agile and Scrum project management fundamentals', 'Task prioritization using Kanban and sprint planning', 'Risk management and stakeholder communication'],
    'DEPI-BET-2024': ['Business English communication: writing, speaking, presentations', 'Professional email and report writing standards', 'Cross-cultural business communication skills'],
    'DEPI-AMIT-QA-2024': ['Software testing lifecycle: unit, integration, system, UAT', 'Manual and automated testing techniques', 'Bug tracking, test case design, and QA reporting'],
    'DEPI-R2-AMIT-2024': ['Graduation from DEPI Round 2 — government digital skills program', 'Advanced software development practices and professional delivery', 'Digital Egypt Pioneers Initiative certification'],
    'ZC-AI-2023': ['Introduction to artificial intelligence and machine learning', 'AI applications in industry: healthcare, finance, logistics', 'Zewail City AI curriculum: neural networks and deep learning basics'],
    'IMP-AI-2023': ['AI fundamentals: supervised, unsupervised, and reinforcement learning', 'Real-world AI use cases and ethical considerations', 'Hands-on AI tools and frameworks introduction'],
    'ITIDA-GIGS-2024': ['Freelancing and digital gig economy certification by ITIDA', 'Egyptian digital economy initiative for tech professionals', 'International freelancing platforms and project management'],
    'UDA-DMC-2023': ['Digital marketing fundamentals: SEO, SEM, social media', 'Content marketing and audience targeting strategies', 'Analytics and conversion optimization basics'],
    'HUAWEI-DC25-NA-2ND': ['2nd Place — Huawei Developer Competition 2025 Northern Africa', '389 teams, 10+ countries, 1,400+ participants', 'AI architecture integration with Huawei Cloud services'],
    'NASA-SAC-2024-GLOBAL': ['Global Nominee — NASA Space Apps Challenge 2024', 'Built Green Pulse: climate-tech solution addressing Kiribati\'s sea-level crisis', 'NASA open data integration and space technology application'],
    'NASA-SAC-CAIRO-2024': ['Local Winner — NASA Space Apps Cairo 2024', 'Team Green Pulse: storytelling-driven climate science', 'Translated complex NASA data into human-centered narratives'],
    'NASA-SAC-BOOT-2025': ['NASA Space Apps Cairo Bootcamp 2025: ideation to prototype', 'Collaboration with space professionals and NASA challenge mentors', 'Rapid prototyping and pitching for space technology challenges'],
    'CAIROICT-AIL-2ND-2025': ['2nd Place — AI for Life Human-Centered Hackathon, Cairo ICT 2025', 'Designed empathy-first AI solutions for real-world social impact', 'Blending human-centered design with advanced AI technology'],
    'NU-EGNITE-2024': ['E-Gnite Bootcamp: entrepreneurship and innovation at Nile University', 'Ideation workshops, prototyping, and competitive pitching', 'Startup competition experience in Egyptian university ecosystem'],
    'CAE-ESG-2ND-2023': ['2nd Place — Crédit Agricole Egypt Green ESG Contest 2023', 'Built Unbounded: accessibility-first Flutter app for job seekers with disabilities', 'ESG principles: Environmental, Social, and Governance in product design'],
    'F6L-RIADI-2026': ['Selected into Flat6Labs Accelerator Program — Dec 2026', 'Riadi: sports-tech platform digitizing the Arab world\'s athletic ecosystem', 'Flat6Labs acceleration: investor access, mentorship, and market validation'],
    'ASDWU-AYS-2023': ['Arab Youth Summit — Arab Sustainable Development Week Union', 'Regional youth leadership and sustainable development goals (SDGs)', 'Networking with Arab youth leaders and policy makers'],
}

with open('certifications.html', 'r', encoding='utf-8') as f:
    certs = f.read()

# 1. Update CERTS JS array with real learnings and thumbnails
pattern = r'const CERTS=(\[.*?\]);'
match = re.search(pattern, certs, re.DOTALL)
if match:
    data = json.loads(match.group(1))
    for c in data:
        cid = c.get('cid','')
        if cid in LEARNINGS:
            c['learnings'] = LEARNINGS[cid]
        if cid in THUMB:
            c['thumb'] = THUMB[cid]
        else:
            c['thumb'] = c.get('pdf','')
    new_js = 'const CERTS=' + json.dumps(data, ensure_ascii=False) + ';'
    certs = certs.replace(match.group(0), new_js)
    print(f"Updated {len(data)} certs with learnings and thumbnails")

# 2. Add thumbnail image to each card (shown on card top, not just in modal)
# Replace the cert-top div to show a thumbnail image
old_card_top = '''.cert-top{padding:1.5rem 1.5rem 1rem;display:flex;justify-content:space-between;align-items:flex-start;gap:1rem}'''
new_card_top = '''.cert-top{padding:0;position:relative;height:150px;overflow:hidden;background:#0a0a12}
.cert-top-img{width:100%;height:100%;object-fit:cover;opacity:.85;transition:transform .5s,opacity .4s}
.cert-card:hover .cert-top-img{transform:scale(1.05);opacity:1}
.cert-top-overlay{position:absolute;inset:0;background:linear-gradient(to bottom,transparent 40%,rgba(5,5,7,.95))}
.cert-top-meta{position:absolute;bottom:.75rem;left:1rem;right:1rem;display:flex;align-items:center;justify-content:space-between}
.cert-icon-sm{font-size:1.2rem}
'''
certs = certs.replace(old_card_top, new_card_top)

# 3. Update openDetail to show thumbnail + make pdf scrollable
old_pdf_style = '''.modal-pdf{width:100%;height:280px;background:#000;border-bottom:1px solid var(--border)}
.modal-pdf iframe{width:100%;height:100%;border:none}'''
new_pdf_style = '''.modal-pdf{width:100%;height:340px;background:#000;border-bottom:1px solid var(--border);position:relative;overflow:hidden}
.modal-pdf iframe{width:100%;height:100%;border:none;overflow:auto}
.modal-pdf img{width:100%;height:100%;object-fit:contain;background:#fff}'''
certs = certs.replace(old_pdf_style, new_pdf_style)

# 4. Update modal to show scrollable PDF and image fallback
old_modal_set = "document.getElementById('modal-pdf').innerHTML=c.pdf?`<iframe loading=\"lazy\" src=\"${c.pdf}#toolbar=0&navpanes=0&view=FitH\" style=\"width:100%;height:100%;border:none;\"></iframe>`:'<div style=\"display:flex;align-items:center;justify-content:center;height:100%;color:#64748b;\">Preview not available</div>';"
new_modal_set = """const pdfSrc=c.pdf;
  const thumbSrc=c.thumb||pdfSrc;
  let pdfHtml='<div style="display:flex;align-items:center;justify-content:center;height:100%;color:#64748b;font-size:.9rem;">No preview available</div>';
  if(pdfSrc&&pdfSrc.endsWith('.pdf')){
    pdfHtml=`<iframe loading="lazy" src="${pdfSrc}" style="width:100%;height:100%;border:none;" sandbox="allow-scripts allow-same-origin"></iframe>`;
  } else if(thumbSrc&&(thumbSrc.endsWith('.jpg')||thumbSrc.endsWith('.png')||thumbSrc.endsWith('.jpeg'))){
    pdfHtml=`<img src="${thumbSrc}" alt="${c.title}" style="width:100%;height:100%;object-fit:contain;background:#fff;">`;
  }
  document.getElementById('modal-pdf').innerHTML=pdfHtml;"""
certs = certs.replace(old_modal_set, new_modal_set)

# 5. Remove download button from modal
certs = certs.replace(
    '<a id="modal-dl" class="btn-dl" download>⬇ Download Certificate</a>',
    ''
)
# Also remove download from the card footer
certs = re.sub(r'<a href="[^"]*" download onclick="event\.stopPropagation\(\)" class="cert-dl"[^>]*>⬇</a>', '', certs)

# 6. Update make_card calls to use thumbnail img in cert-top
# Rebuild the card HTML to show image in top section
# Cards are pre-generated in the HTML - we need to update the card generation to show thumbnail
# Since cards are static HTML, we update the JS openDetail to inject image on card hover (complex)
# Instead, update each card's cert-top to show an img tag based on the cert index
# This requires regenerating cards - let's update the CSS to make static cards work

# Add img to each cert-top in the static cards
def replace_cert_tops(html_content, data):
    """Replace each .cert-top div with one containing a thumbnail image"""
    result = html_content
    for i, c in enumerate(data):
        thumb = c.get('thumb', c.get('pdf',''))
        icon = {'business':'💼','tech':'💻','hackathon':'🏆'}.get(c.get('cat','tech'),'📜')
        cat_label = {'business':'Business','tech':'Technology','hackathon':'Hackathon'}.get(c.get('cat','tech'),'Other')
        cat = c.get('cat','tech')
        colors = {'business':('#10b981','rgba(16,185,129,'),'tech':('#3b82f6','rgba(59,130,246,'),'hackathon':('#8b5cf6','rgba(139,92,246,')}
        accent, rgba = colors.get(cat, colors['tech'])
        
        is_img = any(thumb.endswith(x) for x in ['.jpg','.png','.jpeg'])
        if is_img:
            inner = f'<img class="cert-top-img" src="{thumb}" alt="{c["title"]}" loading="lazy"><div class="cert-top-overlay"></div>'
        else:
            inner = f'<div style="display:flex;align-items:center;justify-content:center;height:100%;background:linear-gradient(135deg,{rgba}0.12),{rgba}0.04));">{icon}</div>'
        
        old_top = f'''<div class="cert-top" style="background:linear-gradient(135deg,{rgba}0.12) 0%,{rgba}0.04) 100%);">
                <div class="cert-icon">{icon}</div>
                <div class="cert-cat-badge" style="color:{accent};border-color:{rgba}0.3);background:{rgba}0.08);">{cat_label}</div>
            </div>'''
        new_top = f'''<div class="cert-top">
                {inner}
                <div class="cert-top-meta">
                  <span class="cert-cat-badge" style="color:{accent};border-color:{rgba}0.3);background:{rgba}0.12);backdrop-filter:blur(8px);font-size:.65rem;">{icon} {cat_label}</span>
                </div>
            </div>'''
        if old_top in result:
            result = result.replace(old_top, new_top, 1)
    return result

certs = replace_cert_tops(certs, data)

with open('certifications.html', 'w', encoding='utf-8') as f:
    f.write(certs)
print("certifications.html fully updated")

# Fix ventures.html — Riadi card: use Riadi LOGO not competition image
with open('ventures.html', 'r', encoding='utf-8') as f:
    ven = f.read()

# Fix featured Riadi visual — use riadi logo on white bg, not competition photo
old_feat_img = 'assets/marwan_images/Flat6Labs &amp; Shell Intilaaqah Competition at EGYPES 2026/Winning 1st Place at the Flat6Labs &amp; Shell Intilaaqah Competition at EGYPES 2026.jpeg'
new_feat_content = '''    <img src="assets/marwan_images/personal/main image.png" alt="Marwan Magdy — Riadi" style="width:100%;height:100%;object-fit:cover;opacity:.85;transition:transform .7s,opacity .4s;">
      <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:180px;height:80px;background:#fff;border-radius:1rem;display:flex;align-items:center;justify-content:center;padding:1rem;box-shadow:0 20px 60px rgba(0,0,0,.5);">
        <img src="assets/logo/riadi/logo-transparent.png" alt="Riadi Logo" style="max-width:100%;max-height:100%;object-fit:contain;">
      </div>'''

# Replace the entire feat-visual img line
ven = ven.replace(
    f'<img src="{old_feat_img}"',
    '<img src="assets/marwan_images/flat6laps/booth at EGYPES 2026 .jpeg"'
)
with open('ventures.html', 'w', encoding='utf-8') as f:
    f.write(ven)
print("ventures.html Riadi image fixed to booth photo")
