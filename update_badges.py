import re

with open('ventures.html', 'r', encoding='utf-8') as f:
    content = f.read()

badge_css = '''
    <style>
    .store-badge {
      display: inline-flex;
      align-items: center;
      background-color: rgba(255, 255, 255, 0.05);
      color: #ffffff;
      border: 1px solid rgba(255,255,255,0.2);
      border-radius: 7px;
      padding: 6px 14px 6px 12px;
      text-decoration: none;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      transition: background-color 0.2s ease, border-color 0.2s ease, transform 0.2s;
      height: 42px;
      box-sizing: border-box;
      min-width: 145px;
    }

    .store-badge:hover {
      background-color: rgba(16,185,129,0.1);
      border-color: rgba(16,185,129,0.5);
      transform: translateY(-2px);
    }

    .badge-icon {
      width: 24px;
      height: 24px;
      margin-right: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .badge-icon svg {
      width: 100%;
      height: 100%;
      fill: currentColor;
    }

    .badge-text {
      display: flex;
      flex-direction: column;
      justify-content: center;
      text-align: left;
    }

    .badge-sub {
      font-size: 9px;
      line-height: 1;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 2px;
      color: #a6a6a6;
    }

    .badge-title {
      font-size: 16px;
      font-weight: 500;
      line-height: 1.1;
      letter-spacing: -0.3px;
    }
    </style>
'''

if '.store-badge {' not in content:
    content = content.replace('</head>', badge_css + '</head>')

# Riadi links replacement
# The original links for Riadi
riadi_web = r'<a href="https://riadiapp\.com/" target="_blank" style="transition: transform 0\.2s;">\s*<div[^>]*>\s*<img src="assets/logo/social/internet\.png"[^>]*>\s*</div>\s*</a>'
riadi_new_web = '''<a href="https://riadiapp.com/" target="_blank" class="store-badge">
    <div class="badge-icon">
      <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
      </svg>
    </div>
    <div class="badge-text">
      <span class="badge-sub">VISIT OUR</span>
      <span class="badge-title">Website</span>
    </div>
</a>'''
content = re.sub(riadi_web, riadi_new_web, content)

riadi_email = r'<a href="mailto:Contact@riadiapp\.com" style="transition: transform 0\.2s;">\s*<img src="assets/logo/social/email\.png"[^>]*>\s*</a>'
riadi_new_email = '''<a href="mailto:Contact@riadiapp.com" class="store-badge">
    <div class="badge-icon">
      <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
      </svg>
    </div>
    <div class="badge-text">
      <span class="badge-sub">CONTACT US</span>
      <span class="badge-title">Email</span>
    </div>
</a>'''
content = re.sub(riadi_email, riadi_new_email, content)

# Juzur links replacement
juzur_web = r'<a href="#" target="_blank" style="transition: transform 0\.2s;">\s*<div[^>]*>\s*<img src="assets/logo/social/internet\.png"[^>]*>\s*</div>\s*</a>'
juzur_new_web = riadi_new_web.replace('https://riadiapp.com/', '#')
content = re.sub(juzur_web, juzur_new_web, content)

juzur_email = r'<a href="#" style="transition: transform 0\.2s;">\s*<img src="assets/logo/social/email\.png"[^>]*>\s*</a>'
juzur_new_email = riadi_new_email.replace('Contact@riadiapp.com', '#')
content = re.sub(juzur_email, juzur_new_email, content)

with open('ventures.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated ventures.html')
