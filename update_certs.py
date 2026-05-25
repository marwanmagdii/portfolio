import re

with open('certifications.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    href = match.group(1)
    target = match.group(2)
    classes = match.group(3)
    data_cat = match.group(4)
    inner = match.group(5)
    
    parts = inner.split('</div>\n            </a>')
    
    inner_mod = re.sub(r'(<div class="cert-content">.*?)</div>', 
    r'\1\n' + 
    r'                <div class="cert-details" style="display: none; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);">\n' +
    r'                    <p style="font-size: 0.85rem; color: #cbd5e1; margin-bottom: 1rem;">Placeholder: Add your key learnings here.</p>\n' +
    f'                    <a href="{href}" target="_blank" style="display: inline-block; padding: 0.4rem 1rem; background: var(--color-brand-green); color: #fff; text-decoration: none; border-radius: 4px; font-size: 0.8rem; font-weight: 600;">View Certificate</a>\n' +
    r'                </div>\n' +
    r'                <button class="cert-toggle-btn" style="margin-top: 1rem; background: none; border: 1px solid var(--color-brand-green); color: var(--color-brand-green); padding: 0.4rem; border-radius: 4px; cursor: pointer; font-size: 0.8rem; font-family: inherit; transition: all 0.2s;" onclick="const d = this.previousElementSibling; if(d.style.display === \'none\') { d.style.display = \'block\'; this.innerText = \'Hide Details\'; } else { d.style.display = \'none\'; this.innerText = \'What I Learned\'; }">What I Learned</button>\n' +
    r'            </div>', inner, flags=re.DOTALL)

    return f'<div class="{classes}" {data_cat}>\n            {inner_mod}\n            </div>'

pattern = re.compile(r'<a href="([^"]+)" target="([^"]+)" class="([^"]+)" (data-category="[^"]+")>\n(.*?)</a>', re.DOTALL)
new_content = pattern.sub(replacer, content)

with open('certifications.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
