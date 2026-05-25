import re

# ---- Update index.html awards grid to have images ----
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Find achievements section and inject images into each card
award_images = [
    ('assets/marwan_images/Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026/Winning 1st Place at the Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026.jpeg', 'EGYPES 2026'),
    ('assets/marwan_images/Huawei Developer Competition 2025 Northern Africa/Winning 2nd Place across North Africa at the Huawei Developer Competition 2025 Northern Africa.jpeg', 'Huawei'),
    ('assets/marwan_images/AI for Life Human- Centered Hackathon during Cairo ICT 2025/Winning 2nd Place at the AI for Life Human- Centered Hackathon during Cairo ICT 2025.jpeg', 'AI for Life'),
    ('assets/marwan_images/Accelerator Program at Flat6Labs/Selected for the Accelerator Program at Flat6Labs.jpeg', 'Flat6Labs Accelerator'),
    ('assets/marwan_images/NASA space Apps Cairo 2024/Global nominee and Local Winner at NASA space Apps Cairo 2024.jpeg', 'NASA Space Apps'),
    ('assets/marwan_images/Enpact Hackathon/Winning Team at Enpact Hackathon, Selected for the Pre-lncubation Phase.jpeg', 'enpact'),
    ("assets/marwan_images/CAE Green Contest 2023/Winning 2nd Place at Credit Agricole Egypt's CAE Green Contest 2023.jpeg", 'CAE ESG'),
]

# Replace the ach-card div structure to include images
old_grid_start = idx.find('<div class="achievements-grid">')
old_grid_end = idx.find('</div>\n    </section>', old_grid_start)

if old_grid_start != -1 and old_grid_end != -1:
    articles_map = ['article-riadi.html','article-huawei.html','article-aiforlife.html','article-riadi.html','article-nasa.html','article-judhur.html','article-unbounded.html']
    icons = ['🏆 1st Place','🥈 2nd Place','🥈 2nd Place','🚀 Accelerator','🌍 Global Nominee','🌿 Pre-Incubation','🥈 2nd Place']
    titles = ['Flat6Labs &amp; Shell Intilaaqah @ EGYPES 2026','Huawei Developer Competition — N. Africa','"AI for Life" Hackathon @ Cairo ICT 2025','Selected into Flat6Labs Accelerator','NASA Space Apps Cairo 2024','enpact Pre-Incubation Winner','Crédit Agricole Egypt Green ESG Contest']
    descs = ['Won 1st place with Riadi, securing accelerator backing. Feb 2026.','Led AI integration across 389 teams, 10+ countries (Dec 2025).','Human-centered AI solutions blending empathy and technology (Nov 2025).','Riadi selected into Flat6Labs accelerator program. Dec 2026.','Local Winner &amp; Global Nominee with Green Pulse (Oct 2024).','Judhur won from 100+ ideas — ETENA Tourism Marathon (Apr 2025).','Accessibility-first Flutter app connecting people with disabilities to jobs (2023).']
    colors = ['rgba(16,185,129,','rgba(59,130,246,','rgba(59,130,246,','rgba(255,255,255,','rgba(255,255,255,','rgba(16,185,129,','rgba(59,130,246,']
    
    cards_html = ''
    for i in range(7):
        img, alt = award_images[i]
        art = articles_map[i]
        color = colors[i]
        cards_html += f'''<a href="{art}" class="ach-card reveal" style="text-decoration:none;display:block;overflow:hidden;">
                <div style="height:160px;overflow:hidden;border-radius:.75rem .75rem 0 0;margin:-1.5rem -1.5rem 1rem -1.5rem;position:relative;">
                    <img src="{img}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;opacity:.8;transition:all .5s;">
                    <div style="position:absolute;inset:0;background:linear-gradient(to bottom,transparent 40%,rgba(5,5,7,.9));"></div>
                    <div class="ach-icon" style="position:absolute;bottom:.75rem;left:1rem;color:{color.replace('rgba','').replace('(','').split(',')[0] if 'green' in color else '#3b82f6'};font-size:.8rem;font-weight:800;">{icons[i]}</div>
                </div>
                <div class="ach-content"><h3 class="ach-title">{titles[i]}</h3><p class="ach-desc">{descs[i]}</p></div>
            </a>\n            '''
    
    new_grid = '<div class="achievements-grid">\n            ' + cards_html + '</div>'
    idx = idx[:old_grid_start] + new_grid + idx[old_grid_end+len('</div>'):]
    print("Awards grid updated with images")
else:
    print(f"Could not find grid. start={old_grid_start}, end={old_grid_end}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

# ---- Update about page nav labels ----
with open('about.html', 'r', encoding='utf-8') as f:
    about = f.read()
# Fix "Founder and CEO" text in about to use green color like hero section
about = about.replace(
    '>Founder &amp; CEO</span>',
    ' style="background:linear-gradient(135deg,#10b981,#34d399);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;">Founder &amp; CEO</span>'
)
about = about.replace(
    '>Founder & CEO</span>',
    ' style="background:linear-gradient(135deg,#10b981,#34d399);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;">Founder & CEO</span>'
)
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about)
print("About.html Founder & CEO color updated")

# ---- Update certifications: remove cert ID display, fix image preview ----
with open('certifications.html', 'r', encoding='utf-8') as f:
    certs = f.read()
# Remove cert-id div from cards (keep in modal only)
certs = re.sub(r'<div class="cert-id">ID: [^<]+</div>\n', '', certs)
# Fix modal-pdf to use object tag instead of iframe for better compatibility
certs = certs.replace(
    "document.getElementById('modal-pdf').innerHTML=`<iframe loading=\"lazy\" src=\"${c.pdf}#toolbar=0&navpanes=0&scrollbar=0&view=FitH\"></iframe>`;",
    "document.getElementById('modal-pdf').innerHTML=c.pdf?`<iframe loading=\"lazy\" src=\"${c.pdf}#toolbar=0&navpanes=0&view=FitH\" style=\"width:100%;height:100%;border:none;\"></iframe>`:'<div style=\"display:flex;align-items:center;justify-content:center;height:100%;color:#64748b;\">Preview not available</div>';"
)
with open('certifications.html', 'w', encoding='utf-8') as f:
    f.write(certs)
print("Certifications updated: removed cert IDs from cards, fixed preview")
