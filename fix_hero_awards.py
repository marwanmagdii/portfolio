import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# 1. Fix hero proof badges — remove McKinsey, change "Backed by" to "Flat6Labs Accelerator"
idx = idx.replace('<span class="proof-badge white">McKinsey Forward Graduate</span>', '')
idx = idx.replace('<span class="proof-badge white">Backed by Flat6Labs</span>',
                  '<span class="proof-badge white">Flat6Labs Accelerator &#128640;</span>')

# 2. Add Contact button to hero CTAs
idx = idx.replace(
    '<a href="about.html" class="btn-secondary">My Story</a>',
    '<a href="about.html" class="btn-secondary">My Story</a>\n                            <a href="#contact-section" class="btn-secondary" style="border-color:rgba(16,185,129,.4);color:#10b981;">Contact Me &#9993;</a>'
)

# 3. Remove old "Connect" quick contact section from index (we keep it but rename anchor)
idx = idx.replace('id="footer-placeholder"', 'id="footer-placeholder"')  # no-op placeholder

# 4. Add id to contact section for anchor
idx = idx.replace(
    '    <!-- ── CONNECT ── -->',
    '    <!-- ── CONNECT ── -->\n    <div id="contact-section"></div>'
)

# 5. Redesign Awards section — clean modern editorial layout with real images
old_start = idx.find('    <!-- 🏆 ACHIEVEMENTS 🏆 -->')
old_end = idx.find('\n\n    <!-- ── CONNECT ──', old_start)

awards_section = '''    <!-- 🏆 ACHIEVEMENTS 🏆 -->
    <section style="padding:6rem 0;border-top:1px solid rgba(255,255,255,0.07);">
      <div class="container">
        <div style="max-width:600px;margin-bottom:3.5rem;">
          <span style="font-size:.75rem;text-transform:uppercase;letter-spacing:.18em;color:#10b981;font-weight:700;display:block;margin-bottom:.75rem;">7 Awards &amp; Recognitions</span>
          <h2 style="font-family:'Playfair Display',serif;font-size:clamp(2rem,4vw,3.2rem);letter-spacing:-.02em;line-height:1.1;">Awards &amp; <em style="font-style:italic;background:linear-gradient(135deg,#10b981,#3b82f6);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;">Achievements</em></h2>
        </div>

        <!-- ROW 1: Featured large + 2 side -->
        <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:1.25rem;margin-bottom:1.25rem;">
          <!-- FEATURED: 1st Place EGYPES -->
          <a href="article-riadi.html" style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;height:320px;border:1px solid rgba(255,255,255,.1);background:#0a0a12;group">
            <img src="assets/marwan_images/Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026/marwan magdy holding the prize.png" alt="1st Place EGYPES" style="width:100%;height:100%;object-fit:cover;opacity:.75;transition:all .5s;display:block;">
            <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.4) 50%,transparent 100%);"></div>
            <div style="position:absolute;bottom:0;left:0;right:0;padding:1.75rem;">
              <div style="display:inline-flex;align-items:center;gap:.4rem;background:rgba(16,185,129,.9);color:#000;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;padding:.3rem .75rem;border-radius:50px;margin-bottom:.75rem;">&#127942; 1st Place</div>
              <h3 style="font-family:'Playfair Display',serif;font-size:1.3rem;color:#fff;line-height:1.2;margin-bottom:.35rem;">Flat6Labs &amp; Shell Intilaaqah @ EGYPES 2026</h3>
              <p style="color:#94a3b8;font-size:.82rem;">Won 1st place with Riadi · Feb 2026</p>
            </div>
          </a>
          <!-- RIGHT COLUMN: 2 stacked -->
          <div style="display:grid;grid-template-rows:1fr 1fr;gap:1.25rem;">
            <a href="article-huawei.html" style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;border:1px solid rgba(255,255,255,.1);background:#0a0a12;">
              <img src="assets/marwan_images/Huawei Developer Competition 2025 Northern Africa/Winning 2nd Place across North Africa at the Huawei Developer Competition 2025 Northern Africa.jpeg" alt="Huawei" style="width:100%;height:100%;object-fit:cover;opacity:.7;display:block;">
              <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.3) 60%,transparent 100%);"></div>
              <div style="position:absolute;bottom:0;left:0;right:0;padding:1.25rem;">
                <div style="display:inline-flex;background:rgba(59,130,246,.9);color:#fff;font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;padding:.25rem .65rem;border-radius:50px;margin-bottom:.5rem;">&#129352; 2nd Place</div>
                <h3 style="font-size:1rem;color:#fff;line-height:1.25;font-weight:600;">Huawei Developer Competition — N. Africa</h3>
              </div>
            </a>
            <a href="article-aiforlife.html" style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;border:1px solid rgba(255,255,255,.1);background:#0a0a12;">
              <img src="assets/marwan_images/AI for Life Human- Centered Hackathon during Cairo ICT 2025/Winning 2nd Place at the AI for Life Human- Centered Hackathon during Cairo ICT 2025.jpeg" alt="AI for Life" style="width:100%;height:100%;object-fit:cover;opacity:.7;display:block;">
              <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.3) 60%,transparent 100%);"></div>
              <div style="position:absolute;bottom:0;left:0;right:0;padding:1.25rem;">
                <div style="display:inline-flex;background:rgba(59,130,246,.9);color:#fff;font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;padding:.25rem .65rem;border-radius:50px;margin-bottom:.5rem;">&#129352; 2nd Place</div>
                <h3 style="font-size:1rem;color:#fff;line-height:1.25;font-weight:600;">"AI for Life" Hackathon @ Cairo ICT 2025</h3>
              </div>
            </a>
          </div>
        </div>

        <!-- ROW 2: 4 equal cards -->
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1.25rem;">
          <a href="article-riadi.html" style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;height:200px;border:1px solid rgba(255,255,255,.1);background:#0a0a12;">
            <img src="assets/marwan_images/Accelerator Program at Flat6Labs/Selected for the Accelerator Program at Flat6Labs.jpeg" alt="Flat6Labs Accelerator" style="width:100%;height:100%;object-fit:cover;opacity:.7;display:block;">
            <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.3) 60%,transparent 100%);"></div>
            <div style="position:absolute;bottom:0;left:0;right:0;padding:1rem;">
              <div style="display:inline-flex;background:rgba(255,255,255,.15);backdrop-filter:blur(8px);color:#fff;font-size:.63rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;padding:.22rem .6rem;border-radius:50px;margin-bottom:.4rem;">&#128640; Accelerator</div>
              <h3 style="font-size:.88rem;color:#fff;line-height:1.25;font-weight:600;">Flat6Labs Accelerator</h3>
            </div>
          </a>
          <a href="article-nasa.html" style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;height:200px;border:1px solid rgba(255,255,255,.1);background:#0a0a12;">
            <img src="assets/marwan_images/NASA space Apps Cairo 2024/Global nominee and Local Winner at NASA space Apps Cairo 2024.jpeg" alt="NASA" style="width:100%;height:100%;object-fit:cover;opacity:.7;display:block;">
            <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.3) 60%,transparent 100%);"></div>
            <div style="position:absolute;bottom:0;left:0;right:0;padding:1rem;">
              <div style="display:inline-flex;background:rgba(255,255,255,.15);backdrop-filter:blur(8px);color:#fff;font-size:.63rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;padding:.22rem .6rem;border-radius:50px;margin-bottom:.4rem;">&#127757; Global Nominee</div>
              <h3 style="font-size:.88rem;color:#fff;line-height:1.25;font-weight:600;">NASA Space Apps Cairo 2024</h3>
            </div>
          </a>
          <a href="article-judhur.html" style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;height:200px;border:1px solid rgba(255,255,255,.1);background:#0a0a12;">
            <img src="assets/marwan_images/Enpact Hackathon/Winning Team at Enpact Hackathon, Selected for the Pre-lncubation Phase.jpeg" alt="enpact" style="width:100%;height:100%;object-fit:cover;opacity:.7;display:block;">
            <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.3) 60%,transparent 100%);"></div>
            <div style="position:absolute;bottom:0;left:0;right:0;padding:1rem;">
              <div style="display:inline-flex;background:rgba(16,185,129,.8);color:#000;font-size:.63rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;padding:.22rem .6rem;border-radius:50px;margin-bottom:.4rem;">&#127808; Pre-Incubation</div>
              <h3 style="font-size:.88rem;color:#fff;line-height:1.25;font-weight:600;">enpact Pre-Incubation Winner</h3>
            </div>
          </a>
          <a href="article-unbounded.html" style="text-decoration:none;display:block;position:relative;border-radius:1.25rem;overflow:hidden;height:200px;border:1px solid rgba(255,255,255,.1);background:#0a0a12;">
            <img src="assets/marwan_images/CAE Green Contest 2023/Winning 2nd Place at Credit Agricole Egypt's CAE Green Contest 2023.jpeg" alt="CAE" style="width:100%;height:100%;object-fit:cover;opacity:.7;display:block;">
            <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(5,5,7,.95) 0%,rgba(5,5,7,.3) 60%,transparent 100%);"></div>
            <div style="position:absolute;bottom:0;left:0;right:0;padding:1rem;">
              <div style="display:inline-flex;background:rgba(59,130,246,.85);color:#fff;font-size:.63rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;padding:.22rem .6rem;border-radius:50px;margin-bottom:.4rem;">&#129352; 2nd Place</div>
              <h3 style="font-size:.88rem;color:#fff;line-height:1.25;font-weight:600;">CAE Green ESG Contest 2023</h3>
            </div>
          </a>
        </div>

      </div>
    </section>

'''

if old_start != -1 and old_end != -1:
    idx = idx[:old_start] + awards_section + idx[old_end:]
    print("Awards section redesigned with editorial photo layout")
else:
    print(f"Could not find awards section. start={old_start}, end={old_end}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)
print("index.html saved")
