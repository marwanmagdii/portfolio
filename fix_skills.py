with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<!-- THE ARSENAL -->')
end_idx = content.find('<!-- \u2500\u2500 VOLUNTEER')

assert start_idx != -1, 'start not found'
assert end_idx != -1, 'end not found'

S = '''        <!-- THE ARSENAL -->
        <section id="section-skills" class="reveal" style="border-top: 1px solid var(--color-border); padding-top: 4rem;">
            <h2 style="font-family: var(--font-heading); font-size: 2.5rem; text-align: center; margin-bottom: 0.8rem;">Technical Arsenal &amp; Business Acumen</h2>
            <p style="color: var(--color-text-secondary); text-align: center; margin-bottom: 3rem; font-size: 1.1rem;">Built across real startups, hackathons, and international programs \u2014 not just courses.</p>
            <style>
                .sk { display:inline-flex;align-items:center;gap:0.4rem;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);color:#cbd5e1;padding:0.35rem 0.75rem;border-radius:6px;font-size:0.78rem;font-weight:500; }
                .sk-green { display:inline-flex;align-items:center;gap:0.4rem;background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.35);color:var(--color-brand-green);padding:0.35rem 0.75rem;border-radius:6px;font-size:0.78rem;font-weight:700; }
                .sk-card { background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.1);padding:2rem;border-radius:1.5rem;transition:all 0.35s; }
            </style>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem;padding:1rem 0 4rem 0;">
                <div class="sk-card" onmouseover="this.style.transform='translateY(-5px)';this.style.borderColor='rgba(16,185,129,0.4)';" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(255,255,255,0.1)';">
                    <h3 style="font-family:var(--font-heading);font-size:1.2rem;color:#fff;margin-bottom:1.2rem;display:flex;align-items:center;gap:0.7rem;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flutter/flutter-original.svg" width="24" height="24" alt=""> Mobile Development</h3>
                    <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flutter/flutter-original.svg" width="13" height="13"> Flutter</span>
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dart/dart-original.svg" width="13" height="13"> Dart</span>
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/firebase/firebase-plain.svg" width="13" height="13"> Firebase</span>
                        <span class="sk">Cross-Platform Dev</span>
                        <span class="sk">REST API Integration</span>
                        <span class="sk">State Management (BLoC/Provider)</span>
                        <span class="sk-green">\U0001f3c5 ITI Certified</span>
                    </div>
                </div>
                <div class="sk-card" onmouseover="this.style.transform='translateY(-5px)';this.style.borderColor='rgba(59,130,246,0.4)';" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(255,255,255,0.1)';">
                    <h3 style="font-family:var(--font-heading);font-size:1.2rem;color:#fff;margin-bottom:1.2rem;display:flex;align-items:center;gap:0.7rem;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="24" height="24" alt=""> Web Development</h3>
                    <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="13" height="13"> HTML5</span>
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="13" height="13"> CSS3</span>
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="13" height="13"> JavaScript</span>
                        <span class="sk">Responsive &amp; Glassmorphism UI</span>
                        <span class="sk">DOM &amp; IntersectionObserver</span>
                        <span class="sk-green">\u26a1 Vibe Coding</span>
                    </div>
                </div>
                <div class="sk-card" onmouseover="this.style.transform='translateY(-5px)';this.style.borderColor='rgba(16,185,129,0.4)';" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(255,255,255,0.1)';">
                    <h3 style="font-family:var(--font-heading);font-size:1.2rem;color:#fff;margin-bottom:1.2rem;display:flex;align-items:center;gap:0.7rem;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="24" height="24" alt=""> Backend &amp; Languages</h3>
                    <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="13" height="13"> Python</span>
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" width="13" height="13"> Java</span>
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" width="13" height="13"> C++</span>
                        <span class="sk">Machine Learning</span>
                        <span class="sk">Deep Learning</span>
                        <span class="sk">Twitter Sentiment Analysis</span>
                    </div>
                </div>
                <div class="sk-card" onmouseover="this.style.transform='translateY(-5px)';this.style.borderColor='rgba(16,185,129,0.4)';" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(255,255,255,0.1)';">
                    <h3 style="font-family:var(--font-heading);font-size:1.2rem;color:#fff;margin-bottom:1.2rem;display:flex;align-items:center;gap:0.7rem;">\U0001f6e1\ufe0f Quality Assurance</h3>
                    <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                        <span class="sk">Manual &amp; Automated Testing</span>
                        <span class="sk">Functional &amp; Regression Testing</span>
                        <span class="sk">API Testing (Postman)</span>
                        <span class="sk">Performance Testing (JMeter)</span>
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" width="13" height="13"> Selenium</span>
                        <span class="sk">Bug Tracking (JIRA)</span>
                        <span class="sk-green">\U0001f3c5 DEPI / AMIT Certified</span>
                    </div>
                </div>
                <div class="sk-card" onmouseover="this.style.transform='translateY(-5px)';this.style.borderColor='rgba(16,185,129,0.4)';" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(255,255,255,0.1)';">
                    <h3 style="font-family:var(--font-heading);font-size:1.2rem;color:#fff;margin-bottom:1.2rem;display:flex;align-items:center;gap:0.7rem;">\U0001f9e0 AI &amp; Prompt Engineering</h3>
                    <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                        <span class="sk-green">\u2728 Prompt Engineer</span>
                        <span class="sk">LLM Integration</span>
                        <span class="sk">AI Product Architecture</span>
                        <span class="sk">Blockchain Fundamentals</span>
                        <span class="sk">AI Ecosystem Strategy</span>
                        <span class="sk-green">\u26a1 Vibe Coding</span>
                        <span class="sk-green">\U0001f3c5 Zewail City &amp; Impact AI Certified</span>
                    </div>
                </div>
                <div class="sk-card" onmouseover="this.style.transform='translateY(-5px)';this.style.borderColor='rgba(59,130,246,0.4)';" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(255,255,255,0.1)';">
                    <h3 style="font-family:var(--font-heading);font-size:1.2rem;color:#fff;margin-bottom:1.2rem;display:flex;align-items:center;gap:0.7rem;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg" width="24" height="24" alt=""> UI/UX &amp; Design</h3>
                    <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                        <span class="sk"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg" width="13" height="13"> Figma</span>
                        <span class="sk">User Journey Mapping</span>
                        <span class="sk">Accessibility-First Design</span>
                        <span class="sk">Prototyping &amp; Wireframing</span>
                        <span class="sk">Design Systems</span>
                    </div>
                </div>
                <div class="sk-card" style="grid-column:1/-1;" onmouseover="this.style.transform='translateY(-5px)';this.style.borderColor='rgba(16,185,129,0.4)';" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(255,255,255,0.1)';">
                    <h3 style="font-family:var(--font-heading);font-size:1.2rem;color:#fff;margin-bottom:1.2rem;display:flex;align-items:center;gap:0.7rem;">\U0001f4c8 Business Strategy &amp; Entrepreneurship</h3>
                    <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                        <span class="sk">Business Model Canvas</span>
                        <span class="sk">Lean Canvas &amp; Startup Validation</span>
                        <span class="sk">B2B Sales &amp; Partnership Development</span>
                        <span class="sk">Investor Pitching</span>
                        <span class="sk">Go-to-Market Strategy</span>
                        <span class="sk">OKR &amp; Team Leadership</span>
                        <span class="sk">Ecosystem Scaling</span>
                        <span class="sk">ESG &amp; Sustainability Strategy</span>
                        <span class="sk">Digital Marketing (Udacity)</span>
                        <span class="sk">Business English (DEPI / OTO)</span>
                        <span class="sk-green">\U0001f3c5 McKinsey Forward Graduate</span>
                        <span class="sk-green">\U0001f3c5 Mini MBA in Entrepreneurship</span>
                        <span class="sk-green">\U0001f3c5 ALX Founder Academy Deep Dive</span>
                        <span class="sk-green">\U0001f3c5 TIEC Innov Egypt Program</span>
                    </div>
                </div>
            </div>
        </section>

        '''

new_content = content[:start_idx] + S + content[end_idx:]
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Skills section replaced successfully.')
