# Add contact section to index.html between achievements and CTA
# Also add AIX to resume.html experience

with open('index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# Insert a "Connect" quick contact section before CTA
cta_marker = '    <!-- ── CTA ── -->'
contact_section = '''    <!-- ── CONNECT ── -->
    <section class="container reveal" style="padding:5rem 0;border-top:1px solid rgba(255,255,255,0.08);">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;">
            <div>
                <span style="font-size:.8rem;text-transform:uppercase;letter-spacing:.2em;color:var(--color-brand-green);font-weight:600;display:block;margin-bottom:1rem;">Get in Touch</span>
                <h2 style="font-family:var(--font-heading);font-size:clamp(2rem,4vw,3rem);letter-spacing:-.02em;margin-bottom:1.5rem;">Let's <em style="font-style:italic;background:linear-gradient(135deg,#10b981,#3b82f6);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;">Build</em> Together</h2>
                <p style="color:var(--color-text-secondary);font-size:1.1rem;line-height:1.8;margin-bottom:2.5rem;">Whether you're an investor, partner, fellow founder, or just want to connect — I'd love to hear from you.</p>
                <div style="display:flex;flex-direction:column;gap:1rem;">
                    <a href="mailto:marwan@riadiapp.com" style="display:inline-flex;align-items:center;gap:.8rem;color:var(--color-text-secondary);font-size:1rem;transition:color .3s;text-decoration:none;" onmouseover="this.style.color='#10b981'" onmouseout="this.style.color='#94a3b8'">
                        <span style="width:36px;height:36px;border-radius:50%;border:1px solid rgba(255,255,255,.1);display:flex;align-items:center;justify-content:center;font-size:.9rem;">✉</span>
                        marwan@riadiapp.com
                    </a>
                    <a href="https://linkedin.com/in/marwanmagdy" target="_blank" style="display:inline-flex;align-items:center;gap:.8rem;color:var(--color-text-secondary);font-size:1rem;transition:color .3s;text-decoration:none;" onmouseover="this.style.color='#10b981'" onmouseout="this.style.color='#94a3b8'">
                        <span style="width:36px;height:36px;border-radius:50%;border:1px solid rgba(255,255,255,.1);display:flex;align-items:center;justify-content:center;font-size:.9rem;">in</span>
                        LinkedIn
                    </a>
                    <a href="https://riadiapp.com" target="_blank" style="display:inline-flex;align-items:center;gap:.8rem;color:var(--color-text-secondary);font-size:1rem;transition:color .3s;text-decoration:none;" onmouseover="this.style.color='#10b981'" onmouseout="this.style.color='#94a3b8'">
                        <span style="width:36px;height:36px;border-radius:50%;border:1px solid rgba(255,255,255,.1);display:flex;align-items:center;justify-content:center;font-size:.9rem;">🌐</span>
                        riadiapp.com
                    </a>
                </div>
            </div>
            <div style="background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.08);border-radius:1.5rem;padding:2.5rem;">
                <h3 style="font-size:1.1rem;font-weight:600;margin-bottom:1.5rem;">Quick Message</h3>
                <form onsubmit="sendQuickMsg(event)" style="display:flex;flex-direction:column;gap:1rem;">
                    <input id="qName" type="text" placeholder="Your name" required style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);color:#f1f5f9;font-family:var(--font-body);font-size:.95rem;padding:1rem 1.2rem;border-radius:.75rem;outline:none;transition:border-color .3s;" onfocus="this.style.borderColor='rgba(16,185,129,.4)'" onblur="this.style.borderColor='rgba(255,255,255,.1)'">
                    <input id="qEmail" type="email" placeholder="Your email" required style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);color:#f1f5f9;font-family:var(--font-body);font-size:.95rem;padding:1rem 1.2rem;border-radius:.75rem;outline:none;transition:border-color .3s;" onfocus="this.style.borderColor='rgba(16,185,129,.4)'" onblur="this.style.borderColor='rgba(255,255,255,.1)'">
                    <textarea id="qMsg" rows="4" placeholder="Your message..." required style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);color:#f1f5f9;font-family:var(--font-body);font-size:.95rem;padding:1rem 1.2rem;border-radius:.75rem;outline:none;transition:border-color .3s;resize:vertical;" onfocus="this.style.borderColor='rgba(16,185,129,.4)'" onblur="this.style.borderColor='rgba(255,255,255,.1)'"></textarea>
                    <button type="submit" style="background:var(--color-brand-green);color:#000;font-family:var(--font-body);font-weight:700;font-size:.95rem;padding:1rem;border-radius:.75rem;border:none;cursor:pointer;transition:all .3s;" onmouseover="this.style.background='#0ea271'" onmouseout="this.style.background='#10b981'">Send Message →</button>
                </form>
            </div>
        </div>
    </section>
    <style>@media(max-width:768px){.connect-grid{grid-template-columns:1fr!important}}</style>
    <script>
    function sendQuickMsg(e){
        e.preventDefault();
        const name=document.getElementById('qName').value;
        const email=document.getElementById('qEmail').value;
        const msg=document.getElementById('qMsg').value;
        window.location.href='mailto:marwan@riadiapp.com?subject=Message from '+encodeURIComponent(name)+'&body='+encodeURIComponent(msg+'\\n\\nFrom: '+email);
    }
    </script>

    '''
    
if cta_marker in index:
    index = index.replace(cta_marker, contact_section + cta_marker)
    print("Contact section added to index.html")
else:
    print("CTA marker not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index)

# Add AIX to resume.html experience
with open('resume.html', 'r', encoding='utf-8') as f:
    resume = f.read()

alx_end = resume.find('<!-- 3. Garnet -->')
if alx_end != -1:
    aix_exp = '''                    <!-- 2b. AIX -->
                    <div class="exp-item">
                        <div class="exp-top">
                            <div>
                                <div class="exp-role">AI Technical Lead <span class="role-badge blue">&#129352; 2nd Place</span></div>
                                <div class="exp-company">AIX &mdash; Huawei Developer Competition 2025</div>
                            </div>
                            <div class="exp-date">May 2025 &middot; Regional</div>
                        </div>
                        <div class="exp-desc">
                            <ul>
                                <li>Led AI integration for the Huawei Developer Competition 2025 across Northern Africa (389 teams, 1,400+ participants, 10+ countries)</li>
                                <li>Secured <strong>2nd Place</strong> &mdash; architected the product from concept to competition-ready</li>
                            </ul>
                        </div>
                        <div class="tags"><span class="tag">AI Architecture</span><span class="tag">Huawei Cloud</span><span class="tag">Competition</span></div>
                    </div>

                    '''
    resume = resume[:alx_end] + aix_exp + resume[alx_end:]
    with open('resume.html', 'w', encoding='utf-8') as f:
        f.write(resume)
    print("AIX added to resume.html")
else:
    print("Could not find Garnet section in resume.html")
