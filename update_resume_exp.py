import re

with open('resume.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<!-- Experience -->')
end = content.find('<!-- END OF TWO COLUMN -->')

if start != -1 and end != -1:
    NEW_EXP = '''<!-- Experience -->
                <div class="section-title">Experience</div>
                
                <div class="experience-list">
                    <div class="exp-item">
                        <div class="exp-top">
                            <div>
                                <div class="exp-role">Founder & CEO <span class="role-badge">🏆 1st Place EGYPES</span></div>
                                <div class="exp-company">Riadi — Sports Tech</div>
                            </div>
                            <div class="exp-date">Nov 2024 – Present · Cairo</div>
                        </div>
                        <div class="exp-desc">
                            <ul>
                                <li>Building a premier sports-tech ecosystem digitizing venues, tournaments & athlete performance across the Arab world</li>
                                <li>Won 1st Place at EGYPES 2026 (Flat6Labs + Shell Intilaaqah); secured startup backing</li>
                                <li>Drives B2B sales, investor pitches, partnership deals, and lean product iteration</li>
                            </ul>
                        </div>
                        <div class="tags">
                            <span class="tag">Sports Tech</span><span class="tag">B2B Sales</span><span class="tag">Flat6Labs</span><span class="tag">Flutter</span><span class="tag">Lean Canvas</span>
                        </div>
                    </div>

                    <div class="exp-item">
                        <div class="exp-top">
                            <div>
                                <div class="exp-role">Mentor & Coach</div>
                                <div class="exp-company">ALX</div>
                            </div>
                            <div class="exp-date">Apr 2026 – Present</div>
                        </div>
                        <div class="exp-desc">
                            <ul>
                                <li>Mentoring aspiring tech professionals within the ALX pan-African ecosystem</li>
                                <li>Guiding them through software development, agile methodologies, and career navigation</li>
                            </ul>
                        </div>
                    </div>

                    <div class="exp-item">
                        <div class="exp-top">
                            <div>
                                <div class="exp-role">Co-Founder & Business Developer</div>
                                <div class="exp-company">Garnet (Garnet_eg) — Streetwear Brand</div>
                            </div>
                            <div class="exp-date">Jan 2023 – Apr 2025</div>
                        </div>
                        <div class="exp-desc">
                            <ul>
                                <li>Co-founded premium local Egyptian streetwear brand; managed business model & GTM strategy</li>
                                <li>Built supplier partnerships and brand positioning in competitive local market</li>
                            </ul>
                        </div>
                    </div>

                    <div class="exp-item">
                        <div class="exp-top">
                            <div>
                                <div class="exp-role">Founder <span class="role-badge blue">ETENA Pre-Incubation</span></div>
                                <div class="exp-company">Judhur (Juzur)</div>
                            </div>
                            <div class="exp-date">2024 · Cairo</div>
                        </div>
                        <div class="exp-desc">
                            <ul>
                                <li>Selected out of 100+ ideas for ETENA Tourism Idea Marathon powered by TUI Care Foundation & enpact</li>
                                <li>Developed MVP connecting tourists to rural Egyptian communities for immersive, sustainable tours</li>
                            </ul>
                        </div>
                    </div>

                    <div class="exp-item">
                        <div class="exp-top">
                            <div>
                                <div class="exp-role">Co-Founder & Lead Developer</div>
                                <div class="exp-company">Green Pulse — Recycling Tech Startup</div>
                            </div>
                            <div class="exp-date">2024 · Cairo</div>
                        </div>
                        <div class="exp-desc">
                            <ul>
                                <li>Co-founded mobile application focused on connecting households to recycling collections</li>
                                <li>Green Pulse was also the team name used at NASA Space Apps Cairo 2024 (Local Winner & Global Nominee) for a separate climate tech solution</li>
                            </ul>
                        </div>
                    </div>

                    <div class="exp-item">
                        <div class="exp-top">
                            <div>
                                <div class="exp-role">SQA Tester</div>
                                <div class="exp-company">Credit Agricole Egypt</div>
                            </div>
                            <div class="exp-date">Jan – Feb 2024 · On-site</div>
                        </div>
                        <div class="exp-desc">
                            <ul>
                                <li>Tested Banki Mobile, Banki Wallet, and the CAE banking web platform</li>
                                <li>Security, functional, and payment gateway testing for 3 live banking products</li>
                            </ul>
                        </div>
                        <div class="tags"><span class="tag">Manual Testing</span><span class="tag">JIRA</span><span class="tag">Postman</span><span class="tag">Banking</span></div>
                    </div>

                    <div class="exp-item">
                        <div class="exp-top">
                            <div>
                                <div class="exp-role">Lead Developer & Team Leader <span class="role-badge blue">🥈 CAE ESG Contest</span></div>
                                <div class="exp-company">Unbounded</div>
                            </div>
                            <div class="exp-date">Aug – Nov 2023 · 4 mos</div>
                        </div>
                        <div class="exp-desc">
                            <ul>
                                <li>Built Flutter + Firebase accessibility app connecting people with disabilities to jobs</li>
                                <li>2nd place at Crédit Agricole Egypt's Green ESG Contest 2023</li>
                            </ul>
                        </div>
                        <div class="tags"><span class="tag"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flutter/flutter-original.svg"> Flutter</span><span class="tag">Firebase</span><span class="tag">Figma</span><span class="tag">Accessibility</span></div>
                    </div>
                </div>
            </div>
'''
    new_content = content[:start] + NEW_EXP + content[end:]
    with open('resume.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Resume experience updated successfully.")
else:
    print("Could not find Experience tags in resume.html")
