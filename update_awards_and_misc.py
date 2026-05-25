# ---- 1. UPDATE ACHIEVEMENTS IN ALL FILES ----
# 7 awards:
# 1. 1st Place - EGYPES 2026 (Flat6Labs & Shell Intilaaqah) - Feb 2026
# 2. 2nd Place - Huawei Dev Competition - Dec 2025
# 3. 2nd Place - AI for Life - Nov 2025
# 4. Selected into Flat6Labs Accelerator - Dec 2026 (replaces Shell Intilaaqah incubation)
# 5. NASA Space Apps Cairo - Local Winner & Global Nominee - Oct 2024
# 6. 2nd Place - CAE ESG Contest - 2023
# 7. enpact Pre-Incubation (Judhur) - Apr 2025

import re

# ---- 2. Update about.html: add AIX under ALX, update unbounded logo, fix achievements ----
with open('about.html', 'r', encoding='utf-8') as f:
    about = f.read()

# Fix unbounded timeline logo (update the UNB text badge to use actual image)
about = about.replace(
    '<div class="timeline-logo" style="background: var(--color-surface); font-size:0.75rem; font-weight:800; color:var(--color-brand-green); letter-spacing:-0.03em;">UNB</div>',
    '<div class="timeline-logo" style="background:#fff;padding:4px;"><img src="assets/logo/unbounded/unbounded logo.jpg" alt="Unbounded" style="width:100%;height:100%;object-fit:contain;border-radius:50%;"></div>'
)

# Add AIX experience after ALX section
alx_section_end = about.find('<!-- 3. Garnet -->')
if alx_section_end != -1:
    aix_html = '''                <!-- 2b. AIX (Huawei Competition) -->
                <div class="timeline-item reveal">
                    <div class="timeline-logo" style="background:#fff; padding:4px;">
                        <img src="assets/logo/huawei/huawei.png" alt="Huawei" style="width:100%;height:100%;object-fit:contain;" onerror="this.parentElement.innerHTML='<span style=font-size:.75rem;font-weight:800;color:#cf0a2c>AIX</span>'">
                    </div>
                    <div class="timeline-content">
                        <div class="tl-header">
                            <h3 class="tl-title">AI Technical Lead</h3>
                            <div class="tl-company">AIX &mdash; Huawei Developer Competition 2025</div>
                            <span class="tl-date">May 2025 &middot; Competition</span>
                        </div>
                        <div class="tl-desc">
                            <p style="margin-bottom: 1rem;">Led the AI integration for the Huawei Developer Competition 2025, competing across Northern Africa with 389 teams, 1,400+ participants, and 10+ countries. Secured <strong>2nd Place</strong> regionally.</p>
                            <ul>
                                <li>Led AI architecture from concept to competition-ready product.</li>
                                <li>Integrated Huawei Cloud AI services into a scalable system design.</li>
                            </ul>
                            <div style="margin-top: 1.5rem; display: flex; gap: 1rem; flex-wrap: wrap;">
                                <a href="article-huawei.html" class="btn-preview">Learn More ↗</a>
                            </div>
                        </div>
                    </div>
                </div>

                '''
    about = about[:alx_section_end] + aix_html + about[alx_section_end:]

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about)
print("about.html updated")

# ---- 3. Update resume.html achievements section to 7 awards ----
with open('resume.html', 'r', encoding='utf-8') as f:
    resume = f.read()

start = resume.find('<!-- AWARDS -->')
end = resume.find('<!-- TOP CERTS -->')
if start != -1 and end != -1:
    new_awards = '''<!-- AWARDS -->
                <div class="section">
                    <h2 class="section-title">&#127942; Achievement Summary</h2>
                    <hr class="section-line">
                    <div class="award-item">
                        <span class="award-icon">&#127942;</span>
                        <div><div class="award-title">1st Place &mdash; EGYPES 2026</div><div class="award-org">Flat6Labs + Shell Intilaaqah &middot; Riadi &middot; Feb 2026</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#129352;</span>
                        <div><div class="award-title">2nd Place &mdash; Huawei Dev. Competition</div><div class="award-org">Northern Africa 2025 &middot; 389 teams &middot; Dec 2025</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#129352;</span>
                        <div><div class="award-title">2nd Place &mdash; AI for Life Hackathon</div><div class="award-org">Cairo ICT 2025 &middot; Nov 2025</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#128640;</span>
                        <div><div class="award-title">Selected into Flat6Labs Accelerator</div><div class="award-org">Riadi &middot; Dec 2026</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#127757;</span>
                        <div><div class="award-title">Local Winner + Global Nominee</div><div class="award-org">NASA Space Apps Cairo 2024 &middot; Oct 2024</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#127808;</span>
                        <div><div class="award-title">enpact Pre-Incubation Winner</div><div class="award-org">Judhur &middot; ETENA Tourism Marathon &middot; Apr 2025</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#129352;</span>
                        <div><div class="award-title">2nd Place &mdash; CAE Green ESG Contest</div><div class="award-org">Cr&eacute;dit Agricole Egypt 2023</div></div>
                    </div>
                </div>

                '''
    resume = resume[:start] + new_awards + resume[end:]
    with open('resume.html', 'w', encoding='utf-8') as f:
        f.write(resume)
    print("resume.html awards updated (7 awards)")
else:
    print("Could not find awards section in resume.html")

# ---- 4. Update index.html: remove "Cairo, Egypt", fix achievements grid to 7 ----
with open('index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# Remove Cairo Egypt
index = index.replace('Cairo, Egypt &mdash; ', '').replace('Cairo, Egypt — ', '').replace('>Cairo, Egypt<', '><')
index = index.replace('cairo-egypt', '').replace('Cairo, Egypt', '')

# Fix achievements - replace the 6-card grid with 7 cards
start_ach = index.find('<!-- 🏆 ACHIEVEMENTS 🏆 -->')
end_ach = index.find('<!-- ── CTA ──', start_ach) if index.find('<!-- ── CTA ──', start_ach) != -1 else index.find('<!-- CTA', start_ach)
if end_ach == -1:
    end_ach = index.find('<section class="cta-section', start_ach)
    if end_ach == -1:
        end_ach = index.find('<!-- 🎯', start_ach)

if start_ach != -1 and end_ach != -1:
    new_ach = '''<!-- 🏆 ACHIEVEMENTS 🏆 -->
    <section class="container reveal" style="padding: 6rem 0;">
        <div style="text-align:center;margin-bottom:3rem;">
            <span style="font-size:.8rem;text-transform:uppercase;letter-spacing:.2em;color:var(--color-brand-green);font-weight:600;display:block;margin-bottom:.8rem;">7 Milestones &amp; Recognition</span>
            <h2 style="font-family:var(--font-heading);font-size:clamp(2rem,4vw,3rem);letter-spacing:-.02em;">Awards &amp; <span style="background:linear-gradient(135deg,#10b981,#3b82f6);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;">Achievements</span></h2>
        </div>
        <div class="achievements-grid">
            <div class="ach-card reveal"><div class="ach-icon">&#127942; 1st Place</div><div class="ach-content"><h3 class="ach-title">Flat6Labs &amp; Shell Intilaaqah @ EGYPES 2026</h3><p class="ach-desc">Won 1st place with Riadi, securing accelerator backing. Feb 2026.</p></div></div>
            <div class="ach-card reveal d1"><div class="ach-icon" style="color:var(--color-brand-blue);border-color:rgba(59,130,246,.3);background:rgba(59,130,246,.05);">&#129352; 2nd Place</div><div class="ach-content"><h3 class="ach-title">Huawei Developer Competition — N. Africa</h3><p class="ach-desc">Led AI integration across 389 teams, 10+ countries (Dec 2025).</p></div></div>
            <div class="ach-card reveal d2"><div class="ach-icon" style="color:var(--color-brand-blue);border-color:rgba(59,130,246,.3);background:rgba(59,130,246,.05);">&#129352; 2nd Place</div><div class="ach-content"><h3 class="ach-title">"AI for Life" Hackathon @ Cairo ICT 2025</h3><p class="ach-desc">Human-centered AI solutions blending empathy and technology (Nov 2025).</p></div></div>
            <div class="ach-card reveal"><div class="ach-icon" style="color:#fff;border-color:rgba(255,255,255,.3);background:rgba(255,255,255,.05);">&#128640; Accelerator</div><div class="ach-content"><h3 class="ach-title">Selected into Flat6Labs Accelerator</h3><p class="ach-desc">Riadi selected into Flat6Labs accelerator program. Dec 2026.</p></div></div>
            <div class="ach-card reveal d1"><div class="ach-icon" style="color:#fff;border-color:rgba(255,255,255,.3);background:rgba(255,255,255,.05);">&#127757; Global Nominee</div><div class="ach-content"><h3 class="ach-title">NASA Space Apps Cairo 2024</h3><p class="ach-desc">Local Winner &amp; Global Nominee with Green Pulse (Oct 2024).</p></div></div>
            <div class="ach-card reveal d2"><div class="ach-icon" style="color:#10b981;border-color:rgba(16,185,129,.3);background:rgba(16,185,129,.05);">&#127808; Pre-Incubation</div><div class="ach-content"><h3 class="ach-title">enpact Pre-Incubation Winner</h3><p class="ach-desc">Judhur won from 100+ ideas — ETENA Tourism Marathon (Apr 2025).</p></div></div>
            <div class="ach-card reveal" style="grid-column:span 1;"><div class="ach-icon" style="color:var(--color-brand-blue);border-color:rgba(59,130,246,.3);background:rgba(59,130,246,.05);">&#129352; 2nd Place</div><div class="ach-content"><h3 class="ach-title">Crédit Agricole Egypt Green ESG Contest</h3><p class="ach-desc">Accessibility-first Flutter app connecting people with disabilities to jobs (2023).</p></div></div>
        </div>
    </section>

    '''
    index = index[:start_ach] + new_ach + index[end_ach:]
    print("index.html achievements updated with 7 awards")
else:
    print(f"Could not find achievement section. start={start_ach}, end={end_ach}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index)
print("index.html saved")
