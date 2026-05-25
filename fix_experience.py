import re

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<div class="timeline">')
end = content.find('        <!-- Unbounded -->')

assert start != -1
assert end != -1

NEW_EXP = u'''<div class="timeline">

                <!-- Riadi -->
                <div class="timeline-item reveal">
                    <div class="timeline-logo" style="background: #fff;">
                        <img src="assets/logo/riadi/logo-transparent.png" alt="Riadi">
                    </div>
                    <div class="timeline-content">
                        <div class="tl-header">
                            <h3 class="tl-title">Founder &amp; CEO</h3>
                            <div class="tl-company">Riadi \u00b7 Full-time</div>
                            <span class="tl-date">Nov 2024 \u2013 Present</span>
                        </div>
                        <div class="tl-desc">
                            <p style="margin-bottom: 1rem;">Leading the strategic vision, product architecture, and business development for Riadi, a premier sports-tech ecosystem designed to digitize athletic performance, venue management, and tournament logic across the Arab world.</p>
                            <ul>
                                <li>Won 1st Place at EGYPES 2026 (Flat6Labs + Shell Intilaaqah) \u2014 securing accelerator backing.</li>
                                <li>Architecting a scalable mobile and web platform as the operational backbone for modern sports facilities.</li>
                                <li>Driving B2B sales, negotiating partnerships, and pitching to investors at top-tier events.</li>
                                <li>Executing lean canvas models to continuously adapt product-market fit and ensure sustainable growth.</li>
                            </ul>
                            <div style="margin-top: 1.5rem;">
                                <a href="ventures.html" class="btn-preview">Explore Venture \u2197</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ALX -->
                <div class="timeline-item reveal">
                    <div class="timeline-logo" style="background: #fff; padding: 4px;">
                        <img src="assets/logo/alx/alx.svg" alt="ALX" style="width: 100%; height: 100%; object-fit: contain;">
                    </div>
                    <div class="timeline-content">
                        <div class="tl-header">
                            <h3 class="tl-title">Mentor &amp; Coach</h3>
                            <div class="tl-company">ALX</div>
                            <span class="tl-date">Apr 2026 \u2013 Present</span>
                        </div>
                        <div class="tl-desc">
                            <p>Mentoring and coaching aspiring tech professionals within the ALX pan-African ecosystem, guiding them through software development concepts, agile methodologies, and career navigation.</p>
                        </div>
                    </div>
                </div>

                <!-- Garnet -->
                <div class="timeline-item reveal">
                    <div class="timeline-logo" style="background: var(--color-surface); font-weight: bold; color: #fff; font-size: 1.2rem;">G</div>
                    <div class="timeline-content">
                        <div class="tl-header">
                            <h3 class="tl-title">Co-Founder &amp; Business Developer</h3>
                            <div class="tl-company">Garnet (Garnet_eg) \u00b7 Self-employed</div>
                            <span class="tl-date">Jan 2023 \u2013 Apr 2025 \u00b7 2 yrs 4 mos</span>
                            <div style="font-size: 0.85rem; color: var(--color-text-secondary); margin-bottom: 0.5rem;">Cairo, Egypt</div>
                        </div>
                        <div class="tl-desc">
                            <p style="margin-bottom: 1rem;">Co-founded Garnet_eg, a local Egyptian premium streetwear brand, and as Business Developer drove its growth from concept to market. Led strategy, operations, and partnerships to establish the brand in the competitive Egyptian streetwear scene.</p>
                            <ul>
                                <li>Designed and executed the business model and growth strategy from day one.</li>
                                <li>Analyzed market trends, customer behavior, and product opportunities to inform direction.</li>
                                <li>Built strong partnerships with suppliers, manufacturers, and distributors.</li>
                                <li>Planned product launches and coordinated with production teams.</li>
                                <li>Strengthened brand positioning and visibility in the local streetwear market.</li>
                                <li>Oversaw day-to-day operations to ensure a seamless customer experience.</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Judhur / ETENA -->
                <div class="timeline-item reveal">
                    <div class="timeline-logo" style="background: #fff; padding: 4px;">
                        <img src="assets/logo/enpact/enpact logo.png" alt="Enpact" style="width: 100%; height: 100%; object-fit: contain;">
                    </div>
                    <div class="timeline-content">
                        <div class="tl-header">
                            <h3 class="tl-title">Founder</h3>
                            <div class="tl-company">Judhur \u00b7 ETENA Pre-Incubation</div>
                            <span class="tl-date">enpact \u00b7 TUI Care Foundation \u00b7 Startup Haus Cairo</span>
                        </div>
                        <div class="tl-desc">
                            <p style="margin-bottom: 1rem;">Judhur is a digital application connecting tourists with local communities in rural Egypt, offering immersive tours, cooking classes, and handmade products \u2014 promoting sustainable tourism while empowering local businesses.</p>
                            <ul>
                                <li>Selected from <strong>over 100 applications</strong> into the ETENA Tourism Idea Marathon.</li>
                                <li>From 25 competing teams, Judhur was chosen as one of the <strong>12 winning teams</strong> advancing to the pre-incubation phase.</li>
                                <li>Pitched Judhur\u2019s concept to a panel of expert tourism jurors during the marathon.</li>
                                <li>During pre-incubation: turned the idea into a <strong>working prototype</strong>; attended focused sessions on Market Strategy, Financial Modeling, Prototyping &amp; MVP Roadmap, and Startup Legalities.</li>
                                <li>Benefited from one-to-one mentoring sessions on product strategy and MVP testing.</li>
                                <li>Presented a final pitch to a panel of expert tourism jurors at program close.</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Green Pulse -->
                <div class="timeline-item reveal">
                    <div class="timeline-logo" style="background: #022c22; display:flex;align-items:center;justify-content:center;">
                        <span style="font-size:1.3rem;">&#9851;</span>
                    </div>
                    <div class="timeline-content">
                        <div class="tl-header">
                            <h3 class="tl-title">Co-Founder &amp; Lead Developer</h3>
                            <div class="tl-company">Green Pulse \u2014 Green Tech &amp; Recycling Startup</div>
                            <span class="tl-date">2024 \u00b7 Cairo, Egypt</span>
                        </div>
                        <div class="tl-desc">
                            <p style="margin-bottom: 1rem;">Co-founded Green Pulse, a green tech mobile application built to help households collect and recycle waste easily. The app connects users with nearby recycling collection services, making recycling accessible and habitual for everyday Egyptians.</p>
                            <ul>
                                <li>Led end-to-end development of the recycling mobile app \u2014 from ideation to working product.</li>
                                <li>Focused on accessible UI/UX design and a gamified reward system to encourage recycling habits.</li>
                                <li>Green Pulse was also the team name used at <strong>NASA Space Apps Cairo 2024</strong> \u2014 winning Local Winner and Global Nominee recognition for a separate climate tech solution.</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- AIX / Huawei -->
                <div class="timeline-item reveal">
                    <div class="timeline-logo" style="background: var(--color-surface); font-weight: bold; color: #fff; font-size: 1.2rem;">AI</div>
                    <div class="timeline-content">
                        <div class="tl-header">
                            <h3 class="tl-title">Technical Lead (AI Integration)</h3>
                            <div class="tl-company">AIX \u00b7 Huawei Developer Competition</div>
                            <span class="tl-date">Dec 2025 \u00b7 \U0001f948 2nd Place \u2014 North Africa (389 teams)</span>
                        </div>
                        <div class="tl-desc">
                            <p style="margin-bottom: 1rem;">Led AI development for a product competing across 10+ countries, 1,408+ participants. Built, refined, and tested the AI core from scratch under competition pressure.</p>
                            <ul>
                                <li>Awarded 2nd Place across Northern Africa at Huawei Developer Competition, Dec 2025.</li>
                                <li>Developed and tested complex AI architectures under tight time constraints.</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Credit Agricole Egypt -->
                <div class="timeline-item reveal">
                    <div class="timeline-logo" style="background: #fff; padding: 4px;">
                        <img src="assets/logo/cae/cae main logo.jpg" alt="Credit Agricole Egypt" style="width: 100%; height: 100%; object-fit: contain;">
                    </div>
                    <div class="timeline-content">
                        <div class="tl-header">
                            <h3 class="tl-title">Software Quality Assurance Tester</h3>
                            <div class="tl-company">Credit Agricole Egypt</div>
                            <span class="tl-date">Jan 2024 \u2013 Feb 2024</span>
                            <div style="font-size: 0.85rem; color: var(--color-text-secondary); margin-bottom: 0.5rem;">Cairo, Egypt \u00b7 On-site</div>
                        </div>
                        <div class="tl-desc">
                            <p style="margin-bottom: 1rem;">Performed manual tests for the \u201cBanki Mobile\u201d and \u201cBanki Wallet\u201d applications, as well as the bank\u2019s website, ensuring functionality and user satisfaction.</p>
                            <ul>
                                <li>Validated core functionalities of the digital wallet to manage seamless payments and transactions.</li>
                                <li>Conducted extensive manual testing on the Banki Mobile application for reliability and security.</li>
                                <li>Tested the primary CAE banking web platform to ensure a flawless, user-friendly customer experience.</li>
                            </ul>
                            <details style="margin-bottom: 0.8rem; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 0.8rem; cursor: pointer; transition: all 0.3s; margin-top:1rem;">
                                <summary style="font-weight: 600; color: #fff; display: flex; align-items: center; gap: 1rem; list-style: none;">
                                    <img src="assets/logo/cae/banki wallet.jpg" alt="Banki Wallet" style="width: 48px; height: 48px; border-radius: 6px; object-fit: contain; background: #fff;">
                                    <span style="flex: 1;">Banki Wallet</span>
                                    <span style="font-size:0.8rem; color:var(--color-brand-green); font-weight: 500;">Click to expand</span>
                                </summary>
                                <div style="margin-top: 1rem; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 1rem;"><ul>
                                    <li>Validated core functionalities of the digital wallet to manage seamless payments and transactions.</li>
                                    <li>Focused on payment gateway testing to ensure high security and reliability.</li>
                                    <li>Detected and reported critical issues related to security, functionality, and performance.</li>
                                </ul></div>
                            </details>
                            <details style="margin-bottom: 0.8rem; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 0.8rem; cursor: pointer; transition: all 0.3s;">
                                <summary style="font-weight: 600; color: #fff; display: flex; align-items: center; gap: 1rem; list-style: none;">
                                    <img src="assets/logo/cae/banki mobile .jpg" alt="Banki Mobile" style="width: 48px; height: 48px; border-radius: 6px; object-fit: contain; background: #fff;">
                                    <span style="flex: 1;">Banki Mobile</span>
                                    <span style="font-size:0.8rem; color:var(--color-brand-green); font-weight: 500;">Click to expand</span>
                                </summary>
                                <div style="margin-top: 1rem; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 1rem;"><ul>
                                    <li>Conducted extensive manual testing on the Banki Mobile application for reliability and security.</li>
                                    <li>Designed and executed advanced test cases for mobile feature validation.</li>
                                    <li>Reported bugs with detailed reproduction steps to accelerate the resolution process.</li>
                                </ul></div>
                            </details>
                            <details style="margin-bottom: 1.5rem; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 0.8rem; cursor: pointer; transition: all 0.3s;">
                                <summary style="font-weight: 600; color: #fff; display: flex; align-items: center; gap: 1rem; list-style: none;">
                                    <img src="assets/logo/cae/CAE.jpg" alt="Banking Website" style="width: 48px; height: 48px; border-radius: 6px; object-fit: contain; background: #fff;">
                                    <span style="flex: 1;">Banking Website</span>
                                    <span style="font-size:0.8rem; color:var(--color-brand-green); font-weight: 500;">Click to expand</span>
                                </summary>
                                <div style="margin-top: 1rem; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 1rem;"><ul>
                                    <li>Tested the primary CAE banking web platform to ensure a flawless, user-friendly customer experience.</li>
                                    <li>Executed robust security testing protocols to protect highly sensitive customer data.</li>
                                </ul></div>
                            </details>
                        </div>
                    </div>
                </div>

                <!-- Freelancer SQA -->
                <div class="timeline-item reveal">
                    <div class="timeline-logo" style="background: var(--color-surface); font-weight: bold; color: #fff; font-size: 1.2rem;">FL</div>
                    <div class="timeline-content">
                        <div class="tl-header">
                            <h3 class="tl-title">Software Quality Assurance Tester</h3>
                            <div class="tl-company">Freelancer</div>
                            <span class="tl-date">Oct 2024 \u2013 May 2025 \u00b7 8 mos</span>
                        </div>
                        <div class="tl-desc">
                            <p>Hands-on experience in manual testing, bug tracking, and test case execution for web and mobile applications. Utilized JIRA for bug tracking, Selenium for automation, and Postman for API testing. Delivered functional, regression, and cross-browser testing collaborating with development teams.</p>
                        </div>
                    </div>
                </div>

                <!-- Unbounded -->
                <div class="timeline-item reveal">
                    <div class="timeline-logo" style="background: var(--color-surface); font-size:0.75rem; font-weight:800; color:var(--color-brand-green); letter-spacing:-0.03em;">UNB</div>
                    <div class="timeline-content">
                        <div class="tl-header">
                            <h3 class="tl-title">Lead Developer &amp; Team Leader</h3>
                            <div class="tl-company">Unbounded</div>
                            <span class="tl-date">Aug 2023 \u2013 Nov 2023 \u00b7 4 mos</span>
                            <div style="font-size: 0.85rem; color: var(--color-text-secondary); margin-bottom: 0.5rem;">Cairo, Egypt \u00b7 \U0001f948 2nd Place \u2014 CAE Green Contest 2023</div>
                        </div>
                        <div class="tl-desc">
                            <p style="margin-bottom:1rem;">Built a Flutter + Firebase mobile app connecting individuals with disabilities to job opportunities, winning 2nd place at Cr\u00e9dit Agricole Egypt\u2019s CAE Green ESG Contest 2023.</p>
                            <ul>
                                <li>Designed accessibility-first UI with color-blindness themes and high-contrast typography.</li>
                                <li>Led full development lifecycle from Figma wireframes to production-ready Flutter deployment.</li>
                                <li>Pitched the product to a panel of judges, securing 2nd place.</li>
                            </ul>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        '''

# Find where old Unbounded div ends and education begins
edu_marker = '        <!-- EDUCATION TIMELINE -->'
edu_idx = content.find(edu_marker)

new_content = content[:start] + NEW_EXP + content[edu_idx:]

# Remove ISTQB from skills
new_content = new_content.replace(
    '<span class="sk-green">\U0001f3c5 DEPI / AMIT Certified</span>\n                        <span class="sk-green">\U0001f3c5 ISTQB Foundation Level</span>',
    '<span class="sk-green">\U0001f3c5 DEPI / AMIT Certified</span>'
)
new_content = new_content.replace(
    '<span class="sk-green">\U0001f3c5 ISTQB Foundation Level</span>\n                        <span class="sk-green">\U0001f3c5 DEPI / AMIT Certified</span>',
    '<span class="sk-green">\U0001f3c5 DEPI / AMIT Certified</span>'
)

# Remove BLoC/Provider from Flutter skills
new_content = new_content.replace(
    '\n                        <span class="sk">State Management (BLoC/Provider)</span>',
    ''
)
new_content = new_content.replace(
    '\n                        <span class="sk">REST API Integration</span>',
    ''
)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done - experience rewritten, ISTQB removed, BLoC removed.')
