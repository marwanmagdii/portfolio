import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- \U0001f3c6 ACHIEVEMENTS \U0001f3c6 -->'
end_marker = '<!-- \u2500\u2500 CTA \u2500\u2500 -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    NEW_GRID = '''<!-- \U0001f3c6 ACHIEVEMENTS \U0001f3c6 -->
    <section class="container reveal" style="padding: 6rem 0;">
        <div class="section-header" style="text-align: center; margin-bottom: 4rem;">
            <span style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.2em; color: var(--color-brand-green); font-weight: 600; display: block; margin-bottom: 0.8rem;">Milestones & Recognition</span>
            <h2 style="font-family: var(--font-heading); font-size: clamp(2rem, 4vw, 3rem); letter-spacing: -0.02em;">Awards & <span class="gradient-text">Achievements</span></h2>
        </div>

        <div class="achievements-grid">

            <div class="ach-card reveal">
                <div class="ach-icon">\U0001f3c6 1st Place</div>
                <div class="ach-content">
                    <h3 class="ach-title">Flat6Labs & Shell Intilaaqah @ EGYPES 2026</h3>
                    <p class="ach-desc">Won 1st place with Riadi, securing accelerator backing to redefine the future of sports.</p>
                </div>
            </div>

            <div class="ach-card reveal delay-1">
                <div class="ach-icon" style="color: var(--color-brand-blue); border-color: rgba(59, 130, 246, 0.3); background: rgba(59, 130, 246, 0.05);">\U0001f948 2nd Place</div>
                <div class="ach-content">
                    <h3 class="ach-title">Huawei Developer Competition Northern Africa</h3>
                    <p class="ach-desc">Led AI integration for a product competing across 10+ countries and 1,400+ participants (Dec 2025).</p>
                </div>
            </div>

            <div class="ach-card reveal delay-2">
                <div class="ach-icon" style="color: var(--color-brand-blue); border-color: rgba(59, 130, 246, 0.3); background: rgba(59, 130, 246, 0.05);">\U0001f948 2nd Place</div>
                <div class="ach-content">
                    <h3 class="ach-title">"AI for Life" Hackathon @ Cairo ICT 2025</h3>
                    <p class="ach-desc">Designed human-centered AI solutions blending empathy, creativity, and technology (Nov 2025).</p>
                </div>
            </div>

            <div class="ach-card reveal">
                <div class="ach-icon" style="color: #fff; border-color: rgba(255, 255, 255, 0.3); background: rgba(255, 255, 255, 0.05);">\U0001f680 Incubated</div>
                <div class="ach-content">
                    <h3 class="ach-title">Shell Intilaaqah Egypt Partnership</h3>
                    <p class="ach-desc">Joined the Shell Intilaaqah Egypt program in partnership with Flat6Labs to build Sportiva (2024).</p>
                </div>
            </div>

            <div class="ach-card reveal delay-1">
                <div class="ach-icon" style="color: #fff; border-color: rgba(255, 255, 255, 0.3); background: rgba(255, 255, 255, 0.05);">\U0001f30d Global Nominee</div>
                <div class="ach-content">
                    <h3 class="ach-title">NASA Space Apps Cairo 2024</h3>
                    <p class="ach-desc">Won Local Winner and Global Nominee with Green Pulse, tackling climate change challenges.</p>
                </div>
            </div>

            <div class="ach-card reveal delay-2">
                <div class="ach-icon" style="color: var(--color-brand-blue); border-color: rgba(59, 130, 246, 0.3); background: rgba(59, 130, 246, 0.05);">\U0001f948 2nd Place</div>
                <div class="ach-content">
                    <h3 class="ach-title">Crédit Agricole Egypt Green ESG Contest</h3>
                    <p class="ach-desc">Built an accessibility-first Flutter + Firebase app connecting people with disabilities to jobs (2023).</p>
                </div>
            </div>

        </div>
    </section>

    '''
    
    new_content = content[:start_idx] + NEW_GRID + content[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Index achievements grid updated!")
else:
    print(f"Could not find the grid boundaries. start: {start_idx}, end: {end_idx}")
