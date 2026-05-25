import re

# Known cert IDs and corrected dates  
# Format: title_keyword -> (date, cert_id)
CERT_FIXES = {
    "Founder Academy Deep Dive":            ("Oct 2024",   "ALX-FAD-C4-2024"),
    "McKinsey Forward Program":             ("Sep 2024",   "MCK-FWD-2024"),
    "Mini MBA in Entrepreneurship":         ("2023",       "ALM-MMBA-ENT-2023"),
    "Business & Start Up Booster":          ("Oct 2023",   "FWD-SUB-2023"),
    "Balanced Business Model":              ("Aug 2023",   "EYT-BBM-2023"),
    "Strategy for SMEs":                    ("Jan 2024",   "ALM-SME-2024"),
    "Entrepreneurship 2.0":                 ("2023",       "ALM-ENT20-2023"),
    "Entrepreneurship Ecosystem":           ("Nov 2023",   "EYT-ECO-2023"),
    "Innov Egypt":                          ("2023",       "TIEC-IE-2023"),
    "Pitching Your Business Idea":          ("2023",       "ALM-PITCH-2023"),
    "Project Management Crash Course":      ("2024",       "ALX-PM-2024"),
    "Business English Track":              ("2024",       "DEPI-BET-2024"),
    "Software Tester":                      ("2024",       "DEPI-AMIT-QA-2024"),
    "DEPI Round 2 Graduation":              ("Apr 2024",   "DEPI-R2-AMIT-2024"),
    "Mobile Development":                   ("2023",       "ITI-FLUTTER-2023"),
    "AI Introduction":                      ("2023",       "ZC-AI-2023"),
    "Intro to AI and Applications":         ("2023",       "IMP-AI-2023"),
    "ITIDA Gigs Certification":             ("2024",       "ITIDA-GIGS-2024"),
    "ITIDA Gigs Certification (Advanced)":  ("2024",       "ITIDA-GIGS-ADV-2024"),
    "Blockchain (Part 1)":                  ("2023",       "EYT-BC1-2023"),
    "Blockchain (Part 2)":                  ("2023",       "EYT-BC2-2023"),
    "Digital Marketing Challenger":         ("2023",       "UDA-DMC-2023"),
    "Huawei Developer Competition":         ("May 2025",   "HUAWEI-DC25-NA-2ND"),
    "NASA Space Apps Challenge":            ("Oct 2024",   "NASA-SAC-2024-GLOBAL"),
    "NASA Space Apps Cairo 2024":           ("Oct 2024",   "NASA-SAC-CAIRO-2024"),
    "NASA Space Apps Cairo Bootcamp 2025":  ("2025",       "NASA-SAC-BOOT-2025"),
    "AI for Life Hackathon":               ("Dec 2025",   "CAIROICT-AIL-2ND-2025"),
    "E-Gnite":                              ("2024",       "NU-EGNITE-2024"),
    "ESG Contest":                          ("2023",       "CAE-ESG-2ND-2023"),
    "Accelerator Backing":                  ("Mar 2026",   "F6L-RIADI-2026"),
    "Arab Youth Summit":                    ("2023",       "ASDWU-AYS-2023"),
}

with open('certifications.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find every openModal call and update date + add cert_id as 6th argument
def fix_modal(match):
    btn_str = match.group(0)
    
    # Extract current args
    title_m = re.search(r"openModal\('([^']+)'", btn_str)
    issuer_m = re.search(r"openModal\('[^']+',\s*'([^']+)'", btn_str)
    learnings_m = re.search(r",\s*'(\[[^\]]*\](?:[^']*)?)'", btn_str)
    file_m = re.search(r",\s*'(assets/certifications/[^']+)'\)", btn_str)
    
    if not title_m:
        return btn_str
    
    title = title_m.group(1)
    issuer = issuer_m.group(1) if issuer_m else ''
    learnings = learnings_m.group(1) if learnings_m else '[]'
    file_src = file_m.group(1) if file_m else ''
    
    # Find matching fix
    date = '2023 - 2024'
    cert_id = ''
    for key, (d, cid) in CERT_FIXES.items():
        if key.lower() in title.lower() or title.lower() in key.lower():
            date = d
            cert_id = cid
            break
    
    # Build new onclick - add cert_id as 6th arg
    if file_src:
        new_onclick = f"openModal('{title}', '{issuer}', '{date}', '{learnings}', '{file_src}', '{cert_id}')"
    else:
        new_onclick = f"openModal('{title}', '{issuer}', '{date}', '{learnings}', '', '{cert_id}')"
    
    return f'<button class="cert-modal-btn" onclick="{new_onclick}">More</button>'

pattern = re.compile(r'<button class="cert-modal-btn" onclick="[^"]*">More</button>')
content = pattern.sub(fix_modal, content)

# Now update the openModal JS function to accept and display certId
old_fn = '''function openModal(title, issuer, date, learningsStr, fileSrc) {'''
new_fn = '''function openModal(title, issuer, date, learningsStr, fileSrc, certId) {'''
content = content.replace(old_fn, new_fn)

# Update the modal date display to also show cert ID
old_date_line = '''document.getElementById('modalDate').innerText = date;'''
new_date_line = '''document.getElementById('modalDate').innerText = date;
            if (certId) {
                let idEl = document.getElementById('modalCertId');
                if (!idEl) {
                    idEl = document.createElement('span');
                    idEl.id = 'modalCertId';
                    idEl.style.cssText = 'display:inline-block;margin-left:0.8rem;padding:3px 8px;background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);border-radius:4px;font-size:0.7rem;color:#3b82f6;font-family:monospace;letter-spacing:0.05em;';
                    document.getElementById('modalDate').parentNode.appendChild(idEl);
                }
                idEl.innerText = 'ID: ' + certId;
            }'''
content = content.replace(old_date_line, new_date_line)

# Fix McKinsey - the iframe PDF needs toolbar=0 in correct format
content = content.replace(
    "src=\"assets/certifications/McKinsey_Forward_Program_Badge.pdf#toolbar=0&navpanes=0&scrollbar=0&view=FitH\"",
    "src=\"assets/certifications/McKinsey_Forward_Program_Badge.pdf#toolbar=0&navpanes=0&scrollbar=0\""
)

with open('certifications.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed dates, added cert IDs, fixed McKinsey iframe.')
