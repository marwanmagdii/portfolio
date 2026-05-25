import re

with open('certifications.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the CSS and HTML for the Modal
new_modal_code = '''
    <!-- CERTIFICATION MODAL -->
    <div id="certModal" class="modal-overlay">
        <div class="modal-content modal-large">
            <button class="modal-close" onclick="closeModal()">&times;</button>
            
            <div class="modal-grid">
                <!-- Left: Preview -->
                <div class="modal-preview" id="modalPreview">
                    <!-- Image or iframe injected here -->
                </div>
                
                <!-- Right: Details -->
                <div class="modal-info">
                    <div class="modal-header">
                        <span id="modalDate" class="modal-date"></span>
                        <h3 id="modalTitle" class="modal-title"></h3>
                        <span id="modalIssuer" class="modal-issuer"></span>
                    </div>
                    <div class="modal-body">
                        <h4 style="color: var(--color-brand-green); font-size: 0.9rem; margin-bottom: 0.8rem; text-transform: uppercase; letter-spacing: 1px;">Key Insights & Learnings</h4>
                        <ul id="modalLearnings" class="modal-learnings-list">
                            <!-- Populated by JS -->
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <style>
        .modal-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(8px);
            display: flex; align-items: center; justify-content: center;
            opacity: 0; pointer-events: none; transition: opacity 0.3s ease;
            z-index: 1000; padding: 2rem;
        }
        .modal-overlay.active { opacity: 1; pointer-events: auto; }
        
        .modal-content.modal-large {
            background: #0f0f14; border: 1px solid rgba(16,185,129,0.3);
            border-radius: 16px; width: 100%; max-width: 900px;
            transform: translateY(30px) scale(0.95); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); overflow: hidden;
            display: flex; flex-direction: column; max-height: 90vh;
        }
        .modal-overlay.active .modal-content { transform: translateY(0) scale(1); }
        
        .modal-close {
            position: absolute; top: 1rem; right: 1.5rem; font-size: 2rem; color: #94a3b8;
            background: #000; border: 1px solid rgba(255,255,255,0.2); cursor: pointer; transition: color 0.2s;
            width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
            z-index: 10;
        }
        .modal-close:hover { color: #fff; border-color: rgba(16,185,129,0.5); }
        
        .modal-grid {
            display: grid; grid-template-columns: 1fr 1fr; height: 100%; overflow: hidden;
        }
        
        .modal-preview {
            background: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center;
            border-right: 1px solid rgba(255,255,255,0.1); padding: 1rem;
        }
        .modal-preview img, .modal-preview iframe {
            width: 100%; height: 100%; max-height: 60vh; object-fit: contain; border-radius: 8px; border: none;
        }
        
        .modal-info { padding: 3rem 2.5rem; overflow-y: auto; }
        
        .modal-date { display: inline-block; padding: 4px 10px; background: rgba(255,255,255,0.05); border-radius: 4px; font-size: 0.75rem; color: #cbd5e1; margin-bottom: 1rem; }
        .modal-title { font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin-bottom: 0.5rem; line-height: 1.2; }
        .modal-issuer { font-size: 1rem; color: #94a3b8; font-weight: 500; display: block; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); }
        
        .modal-learnings-list { list-style: none; padding: 0; }
        .modal-learnings-list li { position: relative; padding-left: 1.5rem; color: #cbd5e1; margin-bottom: 1rem; line-height: 1.6; font-size: 0.95rem; }
        .modal-learnings-list li::before { content: '→'; position: absolute; left: 0; color: var(--color-brand-green); font-weight: bold; }
        
        @media (max-width: 768px) {
            .modal-grid { grid-template-columns: 1fr; overflow-y: auto; }
            .modal-content.modal-large { overflow-y: hidden; }
            .modal-preview { border-right: none; border-bottom: 1px solid rgba(255,255,255,0.1); min-height: 300px; }
            .modal-info { padding: 2rem; }
        }
        
        .cert-modal-btn {
            margin-top: 1.2rem; background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3);
            color: var(--color-brand-green); padding: 0.6rem; border-radius: 6px; cursor: pointer;
            font-size: 0.85rem; font-weight: 600; font-family: inherit; transition: all 0.3s; width: 100%;
        }
        .cert-modal-btn:hover { background: var(--color-brand-green); color: #fff; }
    </style>

    <script>
        function openModal(title, issuer, date, learningsStr, fileSrc) {
            document.getElementById('modalTitle').innerText = title;
            document.getElementById('modalIssuer').innerText = issuer;
            document.getElementById('modalDate').innerText = date;
            
            const preview = document.getElementById('modalPreview');
            if (fileSrc.endsWith('.pdf')) {
                preview.innerHTML = `<iframe src="${fileSrc}#toolbar=0&navpanes=0&scrollbar=0&view=FitH"></iframe>`;
            } else {
                preview.innerHTML = `<img src="${fileSrc}" alt="Certificate Preview">`;
            }
            
            const list = document.getElementById('modalLearnings');
            list.innerHTML = '';
            const learnings = JSON.parse(learningsStr);
            learnings.forEach(l => {
                const li = document.createElement('li');
                li.innerText = l;
                list.appendChild(li);
            });
            
            document.getElementById('certModal').classList.add('active');
        }
        
        function closeModal() {
            document.getElementById('certModal').classList.remove('active');
            document.getElementById('modalPreview').innerHTML = '';
        }
        
        // Close modal on outside click
        document.getElementById('certModal').addEventListener('click', function(e) {
            if(e.target === this) closeModal();
        });
    </script>
'''

# Remove old modal structure (starts at <!-- CERTIFICATION MODAL --> up to </script>)
old_modal_pattern = re.compile(r'<!-- CERTIFICATION MODAL -->.*?</script>', re.DOTALL)
content = old_modal_pattern.sub(new_modal_code, content)

# 2. Update the buttons to include the fileSrc
# We need to find the src of the img or iframe inside each cert-card, and inject it into the openModal call.

def button_replacer(match):
    before_visual = match.group(1)
    visual_tag = match.group(2)
    after_visual_to_btn = match.group(3)
    old_onclick = match.group(4)
    after_btn = match.group(5)
    
    # Extract src from visual_tag
    src_match = re.search(r'src="([^"]+)"', visual_tag)
    file_src = ""
    if src_match:
        file_src = src_match.group(1).split('#')[0] # remove any #toolbar=0
    
    # old_onclick looks like: onclick="openModal('Title', 'Issuer', 'Date', 'Learnings')"
    # We want to change it to: onclick="openModal('Title', 'Issuer', 'Date', 'Learnings', 'fileSrc')"
    
    # Insert file_src before the closing parenthesis of the openModal call
    # The last char of old_onclick is `)`
    new_onclick = old_onclick[:-1] + f", '{file_src}')"
    
    return f"{before_visual}{visual_tag}{after_visual_to_btn}{new_onclick}{after_btn}"

# We find each <div class="cert-card"> block to the button
card_pattern = re.compile(r'(<div class="cert-card[^>]*>.*?<div class="cert-visual">)(.*?)(</div>.*?<button class="cert-modal-btn" )(onclick="openModal\([^)]+\)")(>More</button>)', re.DOTALL)
content = card_pattern.sub(button_replacer, content)

with open('certifications.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated certifications.html with 2-column modal and file preview.')
