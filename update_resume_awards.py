import re

with open('resume.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '                <!-- AWARDS -->'
end_marker = '                <!-- TOP CERTS -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    NEW_AWARDS = '''                <!-- AWARDS -->
                <div class="section">
                    <h2 class="section-title">&#127942; Awards</h2>
                    <hr class="section-line">
                    <div class="award-item">
                        <span class="award-icon">&#127942;</span>
                        <div><div class="award-title">1st Place &mdash; EGYPES 2026</div><div class="award-org">Flat6Labs + Shell Intilaaqah &middot; Riadi</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#129352;</span>
                        <div><div class="award-title">2nd Place &mdash; Huawei Dev. Comp.</div><div class="award-org">N. Africa 2025 &middot; 389 teams</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#129352;</span>
                        <div><div class="award-title">2nd Place &mdash; AI for Life</div><div class="award-org">Cairo ICT 2025</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#128640;</span>
                        <div><div class="award-title">Shell Intilaaqah Egypt</div><div class="award-org">Flat6Labs Partnership &middot; Sportiva</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#127757;</span>
                        <div><div class="award-title">Local Winner + Global Nominee</div><div class="award-org">NASA Space Apps Cairo 2024</div></div>
                    </div>
                    <div class="award-item">
                        <span class="award-icon">&#129352;</span>
                        <div><div class="award-title">2nd Place &mdash; CAE ESG Contest</div><div class="award-org">Credit Agricole Egypt 2023</div></div>
                    </div>
                </div>

'''
    new_content = content[:start_idx] + NEW_AWARDS + content[end_idx:]
    with open('resume.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Awards section updated.")
else:
    print("Could not find Awards tags in resume.html")

