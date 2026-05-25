with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

end_grid = content.rfind('</div>\n    </main>')

if end_grid != -1:
    NEW_CARD = '''
            <!-- POST: RED CRESCENT -->
            <a href="article-redcrescent.html" class="post-card reveal delay-1" data-url="article-redcrescent.html">
                <div class="post-image" style="background:#fff; padding:2rem; display:flex; align-items:center; justify-content:center;">
                    <img src="assets/logo/Egyptian Red Crescent/Egyptian Red Crescent.jpeg" alt="Egyptian Red Crescent" style="object-fit:contain;">
                </div>
                <div class="post-body">
                    <div class="post-date">Community &amp; Volunteer</div>
                    <h3 class="post-title">Volunteering with the Egyptian Red Crescent</h3>
                    <div class="post-content">Contributing to humanitarian and community service initiatives — from emergency relief coordination to social welfare programs — across Egypt with one of the country's most respected civil society organizations.</div>
                    
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
    new_content = content[:end_grid] + NEW_CARD + content[end_grid:]
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Added Red Crescent card to blog.html")
else:
    print(f"Could not find grid end. end_grid={end_grid}")
