import re

with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a toast notification style if not exists
if '.share-toast' not in content:
    toast_css = '''
        .share-toast {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: rgba(16, 185, 129, 0.9);
            color: #fff;
            padding: 1rem 1.5rem;
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.9rem;
            box-shadow: 0 10px 30px rgba(16, 185, 129, 0.4);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            z-index: 9999;
            backdrop-filter: blur(10px);
            pointer-events: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .share-toast.show {
            transform: translateY(0);
            opacity: 1;
        }
        .share-toast svg { width: 18px; height: 18px; }
    </style>'''
    content = content.replace('</style>', toast_css)

# Add the script logic before </body>
if 'share-toast-el' not in content:
    share_script = '''
    <!-- Share Toast Notification -->
    <div id="share-toast-el" class="share-toast">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
        Link copied to clipboard!
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const toast = document.getElementById('share-toast-el');
            
            document.querySelectorAll('.btn-share').forEach(btn => {
                btn.addEventListener('click', async (e) => {
                    const postCard = btn.closest('.post-card');
                    const title = postCard ? postCard.querySelector('.post-title').innerText : 'Marwan Magdy Blog';
                    const url = window.location.href;
                    
                    if (navigator.share) {
                        try {
                            await navigator.share({
                                title: title,
                                url: url
                            });
                        } catch (err) {
                            console.log('Share dismissed or failed:', err);
                        }
                    } else {
                        // Fallback: Copy to clipboard
                        navigator.clipboard.writeText(url).then(() => {
                            toast.classList.add('show');
                            setTimeout(() => toast.classList.remove('show'), 3000);
                        });
                    }
                });
            });
        });
    </script>
</body>'''
    content = content.replace('</body>', share_script)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Blog share updated.")
