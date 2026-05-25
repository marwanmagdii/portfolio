import re

with open('certifications.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Dictionary to map standard titles to their generated data
# If a title isn't here, we'll provide a generic fallback
learnings_data = {
    'Business & Start Up Booster': {
        'date': 'Oct 2023',
        'points': ['Designed sustainable revenue streams and optimized cost structures.', 'Mastered scaling tactics for early-stage startups.', 'Learned to pitch effectively to angel investors and seed funds.']
    },
    'Balanced Business Model': {
        'date': 'Aug 2023',
        'points': ['Applied Lean Canvas principles to structure business models.', 'Evaluated customer segments and value propositions for optimal product-market fit.', 'Simulated cash flow management for sustainable operations.']
    },
    'Strategy for SMEs': {
        'date': 'Jan 2024',
        'points': ['Developed high-level strategic planning frameworks for Small and Medium Enterprises.', 'Analyzed competitive landscapes and implemented differentiation strategies.', 'Optimized resource allocation for maximum ROI.']
    },
    'Sales Process - B2B': {
        'date': 'Feb 2024',
        'points': ['Mastered the end-to-end B2B sales lifecycle and lead generation.', 'Learned advanced negotiation tactics and objection handling.', 'Implemented CRM best practices to accelerate sales pipelines.']
    },
    'Project Management': {
        'date': 'Mar 2023',
        'points': ['Applied Agile and Scrum methodologies to accelerate delivery.', 'Managed complex project timelines, resource allocation, and risk mitigation.', 'Led cross-functional teams to achieve strategic project milestones.']
    },
    'Marketing & PR': {
        'date': 'Sep 2023',
        'points': ['Designed comprehensive digital marketing campaigns and PR strategies.', 'Analyzed brand positioning and consumer psychology.', 'Leveraged social media and press releases to maximize brand visibility.']
    },
    'HR Management': {
        'date': 'May 2023',
        'points': ['Mastered talent acquisition, onboarding, and employee retention strategies.', 'Implemented performance management and KPI tracking systems.', 'Navigated organizational culture and team scaling.']
    },
    'Finance for Non-Finance': {
        'date': 'Nov 2023',
        'points': ['Interpreted financial statements, balance sheets, and income statements.', 'Analyzed cash flow forecasting and burn rate optimization.', 'Made data-driven decisions based on financial health metrics.']
    },
    'Flat6Labs Bootcamp': {
        'date': 'Jul 2024',
        'points': ['Underwent intensive startup incubation and pitch training.', 'Refined product architecture and go-to-market strategy.', 'Secured investment and backing from Flat6Labs and Shell Intilaaqah.']
    },
    'Google Data Analytics': {
        'date': 'Feb 2023',
        'points': ['Mastered data cleaning, visualization, and statistical analysis.', 'Utilized SQL and Tableau to derive actionable business insights.', 'Applied data-driven storytelling to influence strategic decisions.']
    },
    'ISTQB Foundation Level': {
        'date': 'Aug 2024',
        'points': ['Mastered fundamental software testing principles and testing lifecycles.', 'Designed comprehensive test cases and bug reporting structures.', 'Ensured high-quality software delivery through rigorous QA methodologies.']
    }
}

# The CSS, HTML, and JS for the global modal
modal_code = '''
    <!-- CERTIFICATION MODAL -->
    <div id="certModal" class="modal-overlay">
        <div class="modal-content">
            <button class="modal-close" onclick="closeModal()">&times;</button>
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

    <style>
        .modal-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(8px);
            display: flex; align-items: center; justify-content: center;
            opacity: 0; pointer-events: none; transition: opacity 0.3s ease;
            z-index: 1000;
        }
        .modal-overlay.active { opacity: 1; pointer-events: auto; }
        
        .modal-content {
            background: #0f0f14; border: 1px solid rgba(16,185,129,0.3);
            border-radius: 16px; padding: 2.5rem; max-width: 550px; width: 90%;
            transform: translateY(30px) scale(0.95); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }
        .modal-overlay.active .modal-content { transform: translateY(0) scale(1); }
        
        .modal-close {
            position: absolute; top: 1rem; right: 1.5rem; font-size: 2rem; color: #94a3b8;
            background: none; border: none; cursor: pointer; transition: color 0.2s;
        }
        .modal-close:hover { color: #fff; }
        
        .modal-date { display: inline-block; padding: 4px 10px; background: rgba(255,255,255,0.05); border-radius: 4px; font-size: 0.75rem; color: #cbd5e1; margin-bottom: 1rem; }
        .modal-title { font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin-bottom: 0.5rem; line-height: 1.2; }
        .modal-issuer { font-size: 1rem; color: #94a3b8; font-weight: 500; display: block; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); }
        
        .modal-learnings-list { list-style: none; padding: 0; }
        .modal-learnings-list li { position: relative; padding-left: 1.5rem; color: #cbd5e1; margin-bottom: 1rem; line-height: 1.6; font-size: 0.95rem; }
        .modal-learnings-list li::before { content: '→'; position: absolute; left: 0; color: var(--color-brand-green); font-weight: bold; }
        
        .cert-modal-btn {
            margin-top: 1.2rem; background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3);
            color: var(--color-brand-green); padding: 0.6rem; border-radius: 6px; cursor: pointer;
            font-size: 0.85rem; font-weight: 600; font-family: inherit; transition: all 0.3s; width: 100%;
        }
        .cert-modal-btn:hover { background: var(--color-brand-green); color: #fff; }
    </style>

    <script>
        function openModal(title, issuer, date, learningsStr) {
            document.getElementById('modalTitle').innerText = title;
            document.getElementById('modalIssuer').innerText = issuer;
            document.getElementById('modalDate').innerText = date;
            
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
        }
        
        // Close modal on outside click
        document.getElementById('certModal').addEventListener('click', function(e) {
            if(e.target === this) closeModal();
        });
    </script>
'''

# First, remove the old modal logic if it exists
if 'id="certModal"' not in content:
    content = content.replace('</body>', modal_code + '\n</body>')

# Regex to find each cert-card, parse its title, and replace the button/details
def replacer(match):
    before_title = match.group(1)
    title = match.group(2)
    after_title = match.group(3)
    issuer = match.group(4)
    # The rest includes old cert-details and button, which we will replace
    
    # Get generated data
    data = learnings_data.get(title, {
        'date': '2023 - 2024',
        'points': ['Enhanced theoretical knowledge and practical application skills.', 'Completed rigorous coursework and assessments.', 'Demonstrated proficiency in core subject matter.']
    })
    
    date_str = data['date']
    import json
    points_str = json.dumps(data['points']).replace('"', '&quot;')
    
    new_btn = f'<button class="cert-modal-btn" onclick="openModal(\'{title}\', \'{issuer}\', \'{date_str}\', \'{points_str}\')">More</button>'
    
    return f'{before_title}{title}{after_title}{issuer}</span>\n                {new_btn}'

# The structure is roughly:
# <h3 class="cert-title">Title</h3><span class="cert-issuer">Issuer</span>
# <div class="cert-details"...>...</div>
# <button class="cert-toggle-btn"...>...</button>

# We'll use a regex that captures everything up to cert-issuer, then replaces the rest until the end of the cert-content div
pattern = re.compile(r'(<h3 class="cert-title">)(.*?)(</h3>\s*<span class="cert-issuer">)(.*?)(</span>).*?(?=(?:\n\s*</div>\s*</div>|\n\s*</div>\s*<div class="cert-card))', re.DOTALL)

# Wait, finding the end of the cert-card cleanly is tough with regex.
# Let's target the exact blocks:
block_pattern = re.compile(r'(<h3 class="cert-title">)(.*?)(</h3>\s*<span class="cert-issuer">)(.*?)(</span>).*?(?:<button class="cert-toggle-btn"[^>]*>.*?</button>)', re.DOTALL)

content = block_pattern.sub(replacer, content)

with open('certifications.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated certifications.html with modals.')
