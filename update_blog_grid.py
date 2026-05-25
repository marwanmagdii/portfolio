import re

with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

end_grid = content.find('</div>\n    </main>')

if end_grid != -1:
    NEW_POSTS = '''
            <!-- POST: ALX -->
            <a href="article-alx.html" class="post-card reveal delay-1" data-url="article-alx.html">
                <div class="post-image" style="background:#fff; padding:2rem; display:flex; align-items:center; justify-content:center;">
                    <img src="assets/logo/alx/alx.svg" alt="ALX" style="object-fit:contain;">
                </div>
                <div class="post-body">
                    <div class="post-date">Leadership & Mentoring</div>
                    <h3 class="post-title">Mentoring the Next Generation of Tech Leaders at ALX</h3>
                    <div class="post-content">Guiding aspiring tech professionals within the ALX pan-African ecosystem through software development, agile methodologies, and career navigation.</div>
                    
                    <div class="post-footer">
                        <div class="post-author">
                            <img src="assets/marwan_images/personal/main image.png" alt="Marwan">
                            <span>Marwan Magdy</span>
                        </div>
                        <div class="btn-share" title="Share this article">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        </div>
                    </div>
                </div>
            </a>

            <!-- POST: GARNET -->
            <a href="article-garnet.html" class="post-card reveal delay-2" data-url="article-garnet.html">
                <div class="post-image">
                    <img src="assets/marwan_images/personal/main image.png" alt="Garnet">
                </div>
                <div class="post-body">
                    <div class="post-date">Business Development</div>
                    <h3 class="post-title">Scaling Garnet_eg: A Premium Streetwear Brand</h3>
                    <div class="post-content">Co-founded a premium local Egyptian streetwear brand; managed business model, GTM strategy, and supplier partnerships.</div>
                    
                    <div class="post-footer">
                        <div class="post-author">
                            <img src="assets/marwan_images/personal/main image.png" alt="Marwan">
                            <span>Marwan Magdy</span>
                        </div>
                        <div class="btn-share" title="Share this article">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        </div>
                    </div>
                </div>
            </a>

            <!-- POST: JUDHUR -->
            <a href="article-judhur.html" class="post-card reveal" data-url="article-judhur.html">
                <div class="post-image" style="background:#fff; padding:2rem; display:flex; align-items:center; justify-content:center;">
                    <img src="assets/logo/enpact/enpact logo.png" alt="Judhur" style="object-fit:contain;">
                </div>
                <div class="post-body">
                    <div class="post-date">Sustainable Tourism</div>
                    <h3 class="post-title">Judhur: Connecting Tourists with Rural Egyptian Heritage</h3>
                    <div class="post-content">Selected out of 100+ ideas for the ETENA Tourism Idea Marathon powered by TUI Care Foundation & enpact. Developed MVP for immersive tours.</div>
                    
                    <div class="post-footer">
                        <div class="post-author">
                            <img src="assets/marwan_images/personal/main image.png" alt="Marwan">
                            <span>Marwan Magdy</span>
                        </div>
                        <div class="btn-share" title="Share this article">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        </div>
                    </div>
                </div>
            </a>

            <!-- POST: GREEN PULSE -->
            <a href="article-greenpulse.html" class="post-card reveal delay-1" data-url="article-greenpulse.html">
                <div class="post-image">
                    <img src="assets/marwan_images/NASA space Apps Cairo 2024/Global nominee and Local Winner at NASA space Apps Cairo 2024.jpeg" alt="Green Pulse">
                </div>
                <div class="post-body">
                    <div class="post-date">Green Tech Startup</div>
                    <h3 class="post-title">Green Pulse: Gamifying Recycling in Egypt</h3>
                    <div class="post-content">Co-founded a mobile application focused on connecting households to recycling collections, leading to my participation at NASA Space Apps Cairo.</div>
                    
                    <div class="post-footer">
                        <div class="post-author">
                            <img src="assets/marwan_images/personal/main image.png" alt="Marwan">
                            <span>Marwan Magdy</span>
                        </div>
                        <div class="btn-share" title="Share this article">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        </div>
                    </div>
                </div>
            </a>

            <!-- POST: CAE -->
            <a href="article-cae.html" class="post-card reveal delay-2" data-url="article-cae.html">
                <div class="post-image" style="background:#fff; padding:2rem; display:flex; align-items:center; justify-content:center;">
                    <img src="assets/logo/cae/cae main logo.jpg" alt="Credit Agricole Egypt" style="object-fit:contain;">
                </div>
                <div class="post-body">
                    <div class="post-date">Quality Assurance</div>
                    <h3 class="post-title">Ensuring Flawless Banking Experiences at Crédit Agricole Egypt</h3>
                    <div class="post-content">Performed manual testing on Banki Mobile, Banki Wallet, and the banking web platform to ensure security, functionality, and payment gateway reliability.</div>
                    
                    <div class="post-footer">
                        <div class="post-author">
                            <img src="assets/marwan_images/personal/main image.png" alt="Marwan">
                            <span>Marwan Magdy</span>
                        </div>
                        <div class="btn-share" title="Share this article">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        </div>
                    </div>
                </div>
            </a>

            <!-- POST: UNBOUNDED -->
            <a href="article-unbounded.html" class="post-card reveal" data-url="article-unbounded.html">
                <div class="post-image">
                    <img src="assets/marwan_images/personal/main image.png" alt="Unbounded">
                </div>
                <div class="post-body">
                    <div class="post-date">Accessibility App</div>
                    <h3 class="post-title">Unbounded: Empowering Individuals with Disabilities</h3>
                    <div class="post-content">Built a Flutter + Firebase accessibility app connecting people with disabilities to jobs, winning 2nd place at Crédit Agricole Egypt's ESG Contest.</div>
                    
                    <div class="post-footer">
                        <div class="post-author">
                            <img src="assets/marwan_images/personal/main image.png" alt="Marwan">
                            <span>Marwan Magdy</span>
                        </div>
                        <div class="btn-share" title="Share this article">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                        </div>
                    </div>
                </div>
            </a>

        '''
    new_content = content[:end_grid] + NEW_POSTS + content[end_grid:]
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Blog.html updated with 6 new articles!")
else:
    print("Could not find blog grid boundary.")
