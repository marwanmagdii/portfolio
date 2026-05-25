import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- CASE STUDIES PREVIEW -->'

# Find where the achievements section starts by searching backward from CASE STUDIES
achievements_title = content.rfind('<h2 class="section-title">Achievements & Awards</h2>', 0, content.find(start_marker))
if achievements_title == -1:
    achievements_title = content.rfind('Awards', 0, content.find(start_marker))

print(f"Found achievements around index: {achievements_title}")

if achievements_title != -1:
    start_grid = content.find('<div class="cs-grid">', achievements_title)
    end_grid = content.find('</section>', start_grid)
    
    if start_grid != -1 and end_grid != -1:
        NEW_GRID = '''<div class="cs-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem;padding:2rem 0;">
            
            <div class="cs-card reveal">
                <div class="cs-image"><img src="assets/marwan_images/Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026/Winning 1st Place at the Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026.jpeg" alt="EGYPES"></div>
                <div class="cs-content">
                    <div class="cs-meta"><span>🏆 1st Place</span><span>Feb 2026</span></div>
                    <h3 class="cs-title">Flat6Labs & Shell Intilaaqah @ EGYPES 2026</h3>
                    <p style="color:var(--color-text-secondary);font-size:0.95rem;">Won 1st place with Riadi, securing accelerator backing to redefine the future of sports.</p>
                </div>
            </div>

            <div class="cs-card reveal delay-1">
                <div class="cs-image"><img src="assets/marwan_images/Huawei Developer Competition 2025 Northern Africa/Winning 2nd Place across North Africa at the Huawei Developer Competition 2025 Northern Africa.jpeg" alt="Huawei"></div>
                <div class="cs-content">
                    <div class="cs-meta"><span>🥈 2nd Place</span><span>Dec 2025</span></div>
                    <h3 class="cs-title">Huawei Developer Competition Northern Africa</h3>
                    <p style="color:var(--color-text-secondary);font-size:0.95rem;">Led AI integration for a product competing across 10+ countries and 1,400+ participants.</p>
                </div>
            </div>

            <div class="cs-card reveal delay-2">
                <div class="cs-image"><img src="assets/marwan_images/AI for Life Human- Centered Hackathon during Cairo ICT 2025/Winning 2nd Place at the AI for Life Human- Centered Hackathon during Cairo ICT 2025.jpeg" alt="AI for Life"></div>
                <div class="cs-content">
                    <div class="cs-meta"><span>🥈 2nd Place</span><span>Nov 2025</span></div>
                    <h3 class="cs-title">"AI for Life" Hackathon @ Cairo ICT 2025</h3>
                    <p style="color:var(--color-text-secondary);font-size:0.95rem;">Designed human-centered AI solutions blending empathy, creativity, and technology.</p>
                </div>
            </div>

            <div class="cs-card reveal">
                <div class="cs-image" style="background:#fff;padding:2rem;display:flex;align-items:center;justify-content:center;">
                    <img src="assets/logo/Shell Intilaaqah/Shell Intilaaqah.jpg" alt="Shell Intilaaqah" style="max-height:100px;object-fit:contain;">
                </div>
                <div class="cs-content">
                    <div class="cs-meta"><span>🚀 Incubated</span><span>2024</span></div>
                    <h3 class="cs-title">Shell Intilaaqah Egypt Partnership</h3>
                    <p style="color:var(--color-text-secondary);font-size:0.95rem;">Joined the Shell Intilaaqah Egypt program in partnership with Flat6Labs to build Sportiva.</p>
                </div>
            </div>

            <div class="cs-card reveal delay-1">
                <div class="cs-image"><img src="assets/marwan_images/NASA space Apps Cairo 2024/Global nominee and Local Winner at NASA space Apps Cairo 2024.jpeg" alt="NASA"></div>
                <div class="cs-content">
                    <div class="cs-meta"><span>🌍 Global Nominee</span><span>2024</span></div>
                    <h3 class="cs-title">NASA Space Apps Cairo 2024</h3>
                    <p style="color:var(--color-text-secondary);font-size:0.95rem;">Won Local Winner and Global Nominee with Green Pulse, tackling climate change challenges.</p>
                </div>
            </div>

            <div class="cs-card reveal delay-2">
                <div class="cs-image" style="background:#fff;padding:2rem;display:flex;align-items:center;justify-content:center;">
                    <img src="assets/logo/cae/cae main logo.jpg" alt="CAE" style="max-height:100px;object-fit:contain;">
                </div>
                <div class="cs-content">
                    <div class="cs-meta"><span>🥈 2nd Place</span><span>2023</span></div>
                    <h3 class="cs-title">Crédit Agricole Egypt Green ESG Contest</h3>
                    <p style="color:var(--color-text-secondary);font-size:0.95rem;">Built an accessibility-first Flutter + Firebase app connecting people with disabilities to jobs.</p>
                </div>
            </div>

        </div>
        '''
        new_content = content[:start_grid] + NEW_GRID + content[end_grid:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Index achievements grid updated!")
    else:
        print("Could not find the grid boundaries.")
else:
    print("Could not find achievements title.")
