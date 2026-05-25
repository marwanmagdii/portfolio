import re, json

with open('certifications.html', 'r', encoding='utf-8') as f:
    old = f.read()

pattern = r"openModal\('([^']+)',\s*'([^']+)',\s*'([^']+)',\s*'(\[[^\]]+\])',\s*'([^']+)',\s*'([^']+)'\)"
certs_raw = re.findall(pattern, old)
cats_raw = re.findall(r'data-category="([^"]+)"', old)

# Build structured cert list
ICON = {
    'business': '💼', 'tech': '💻', 'hackathon': '🏆'
}
COLOR = {
    'business': ('#10b981', 'rgba(16,185,129,'),
    'tech': ('#3b82f6', 'rgba(59,130,246,'),
    'hackathon': ('#8b5cf6', 'rgba(139,92,246,'),
}
LABEL = {
    'business': 'Business & Entrepreneurship',
    'tech': 'Software & Technology',
    'hackathon': 'Hackathons & Events',
}

def make_card(i, title, issuer, date, learnings_str, pdf, cid, cat):
    accent, rgba = COLOR.get(cat, COLOR['tech'])
    icon = ICON.get(cat, '📜')
    # Parse learnings safely
    try:
        learnings = json.loads(learnings_str)
    except:
        learnings = []
    
    tags_html = ''.join(f'<span class="tag">{l[:55]}{"..." if len(l)>55 else ""}</span>' for l in learnings[:3])
    
    return f'''
        <div class="cert-card reveal" data-cat="{cat}" onclick="openDetail({i})">
            <div class="cert-top" style="background:linear-gradient(135deg,{rgba}0.12) 0%,{rgba}0.04) 100%);">
                <div class="cert-icon">{icon}</div>
                <div class="cert-cat-badge" style="color:{accent};border-color:{rgba}0.3);background:{rgba}0.08);">{LABEL.get(cat,cat)}</div>
            </div>
            <div class="cert-body">
                <h3 class="cert-name">{title}</h3>
                <div class="cert-meta">
                    <span class="cert-issuer">{issuer}</span>
                    <span class="cert-date">{date}</span>
                </div>
                <div class="cert-id">ID: {cid}</div>
                <div class="cert-tags">{tags_html}</div>
            </div>
            <div class="cert-footer" style="border-top:1px solid rgba(255,255,255,0.06);">
                <span class="cert-view-btn" style="color:{accent};">View Details →</span>
                <a href="{pdf}" download onclick="event.stopPropagation()" class="cert-dl" title="Download PDF">⬇</a>
            </div>
        </div>'''

# Build modal data JS array
modal_data = []
for i,(title,issuer,date,learnings_str,pdf,cid) in enumerate(certs_raw):
    cat = cats_raw[i] if i < len(cats_raw) else 'tech'
    try:
        learnings = json.loads(learnings_str)
    except:
        learnings = []
    modal_data.append({
        'title': title, 'issuer': issuer, 'date': date,
        'learnings': learnings, 'pdf': pdf, 'cid': cid, 'cat': cat
    })

cards_html = ''
for i,(title,issuer,date,lstr,pdf,cid) in enumerate(certs_raw):
    cat = cats_raw[i] if i < len(cats_raw) else 'tech'
    cards_html += make_card(i, title, issuer, date, lstr, pdf, cid, cat)

modal_js = 'const CERTS=' + json.dumps(modal_data, ensure_ascii=False) + ';'

COUNTS = {'business': 0, 'tech': 0, 'hackathon': 0}
for cat in cats_raw[:len(certs_raw)]:
    if cat in COUNTS: COUNTS[cat] += 1

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Certifications | Marwan Magdy</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
:root{{--bg:#050507;--surf:rgba(255,255,255,0.025);--surf2:rgba(255,255,255,0.05);--border:rgba(255,255,255,0.07);--border2:rgba(255,255,255,0.14);--text:#f1f5f9;--muted:#64748b;--sub:#94a3b8;--green:#10b981;--blue:#3b82f6;--purple:#8b5cf6;--head:'Playfair Display',serif;--body:'Outfit',sans-serif;--ease:cubic-bezier(.16,1,.3,1)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--text);font-family:var(--body);line-height:1.6;overflow-x:hidden}}
a{{text-decoration:none;color:inherit}}
.ambient{{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}}
.amb1{{position:absolute;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(16,185,129,.1) 0%,transparent 70%);top:-200px;right:-100px;animation:drift 22s ease-in-out infinite alternate}}
.amb2{{position:absolute;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(139,92,246,.07) 0%,transparent 70%);bottom:-100px;left:-50px;animation:drift 18s ease-in-out infinite alternate-reverse}}
@keyframes drift{{0%{{transform:translate(0,0)}}100%{{transform:translate(30px,40px)}}}}
.wrap{{max-width:1280px;margin:0 auto;padding:0 5%;position:relative;z-index:1}}

/* HERO */
.hero{{padding:9rem 0 4rem;text-align:center;border-bottom:1px solid var(--border)}}
.hero-kicker{{display:inline-flex;align-items:center;gap:.5rem;background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.2);color:var(--green);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em;padding:.4rem 1rem;border-radius:50px;margin-bottom:1.5rem}}
.hero-dot{{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 2s ease infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}
.hero h1{{font-family:var(--head);font-size:clamp(2.8rem,6vw,5.5rem);line-height:1.08;letter-spacing:-.03em;margin-bottom:1.2rem}}
.hero h1 em{{font-style:italic;background:linear-gradient(135deg,var(--green),var(--blue));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}}
.hero-sub{{color:var(--sub);font-size:1.1rem;max-width:520px;margin:0 auto 2.5rem}}

/* STATS ROW */
.stats-row{{display:flex;justify-content:center;gap:4rem;flex-wrap:wrap;padding:2.5rem 0;border-bottom:1px solid var(--border)}}
.stat{{text-align:center}}
.stat-n{{font-size:2.2rem;font-weight:900;color:var(--text);line-height:1}}
.stat-l{{font-size:.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:.1em;margin-top:.3rem}}

/* FILTERS */
.filter-bar{{display:flex;align-items:center;justify-content:center;gap:.75rem;flex-wrap:wrap;padding:2.5rem 0}}
.fb{{padding:.55rem 1.4rem;border-radius:50px;border:1px solid var(--border2);color:var(--sub);font-size:.8rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;background:transparent;cursor:pointer;transition:all .25s var(--ease);font-family:var(--body);display:inline-flex;align-items:center;gap:.4rem}}
.fb:hover{{border-color:rgba(255,255,255,.25);color:var(--text)}}
.fb.active-all{{background:var(--green);color:#000;border-color:var(--green);box-shadow:0 4px 20px rgba(16,185,129,.3)}}
.fb.active-business{{background:var(--green);color:#000;border-color:var(--green)}}
.fb.active-tech{{background:var(--blue);color:#fff;border-color:var(--blue);box-shadow:0 4px 20px rgba(59,130,246,.3)}}
.fb.active-hackathon{{background:var(--purple);color:#fff;border-color:var(--purple);box-shadow:0 4px 20px rgba(139,92,246,.3)}}

/* SEARCH */
.search-wrap{{max-width:520px;margin:0 auto 2.5rem;position:relative}}
.search-wrap input{{width:100%;background:rgba(255,255,255,.03);border:1px solid var(--border2);color:var(--text);font-family:var(--body);font-size:.95rem;padding:.9rem 1.2rem .9rem 3rem;border-radius:50px;outline:none;transition:border-color .3s}}
.search-wrap input:focus{{border-color:rgba(16,185,129,.4)}}
.search-wrap input::placeholder{{color:var(--muted)}}
.search-icon{{position:absolute;left:1.1rem;top:50%;transform:translateY(-50%);color:var(--muted);font-size:1rem}}

/* GRID */
.grid-label{{font-size:.8rem;color:var(--muted);text-align:center;margin-bottom:2rem;text-transform:uppercase;letter-spacing:.1em}}
.certs-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;padding-bottom:6rem}}

/* CARD */
.cert-card{{background:var(--surf);border:1px solid var(--border);border-radius:1.25rem;overflow:hidden;cursor:pointer;transition:transform .35s var(--ease),border-color .35s,box-shadow .35s;display:flex;flex-direction:column}}
.cert-card:hover{{transform:translateY(-7px);border-color:rgba(255,255,255,.18);box-shadow:0 20px 50px rgba(0,0,0,.5)}}
.cert-top{{padding:1.5rem 1.5rem 1rem;display:flex;justify-content:space-between;align-items:flex-start;gap:1rem}}
.cert-icon{{font-size:1.8rem;line-height:1}}
.cert-cat-badge{{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;padding:.3rem .7rem;border-radius:50px;border:1px solid;white-space:nowrap}}
.cert-body{{padding:0 1.5rem 1rem;flex:1}}
.cert-name{{font-family:var(--head);font-size:1.05rem;line-height:1.3;margin-bottom:.6rem;color:var(--text)}}
.cert-card:hover .cert-name{{color:var(--green)}}
.cert-meta{{display:flex;justify-content:space-between;align-items:center;margin-bottom:.5rem}}
.cert-issuer{{font-size:.82rem;color:var(--sub);font-weight:500}}
.cert-date{{font-size:.78rem;color:var(--muted)}}
.cert-id{{font-size:.72rem;color:var(--muted);font-family:monospace;margin-bottom:.8rem;opacity:.7}}
.cert-tags{{display:flex;flex-wrap:wrap;gap:.4rem}}
.tag{{background:rgba(255,255,255,.04);border:1px solid var(--border);color:var(--sub);font-size:.68rem;padding:.25rem .6rem;border-radius:6px;line-height:1.3}}
.cert-footer{{padding:1rem 1.5rem;display:flex;justify-content:space-between;align-items:center}}
.cert-view-btn{{font-size:.82rem;font-weight:600;transition:opacity .2s}}
.cert-dl{{font-size:1.1rem;color:var(--muted);transition:color .2s;cursor:pointer}}
.cert-dl:hover{{color:var(--text)}}

/* MODAL */
.modal-overlay{{position:fixed;inset:0;background:rgba(0,0,0,.85);backdrop-filter:blur(12px);z-index:1000;display:flex;align-items:center;justify-content:center;padding:2rem;opacity:0;pointer-events:none;transition:opacity .3s}}
.modal-overlay.open{{opacity:1;pointer-events:all}}
.modal{{background:#0c0c12;border:1px solid var(--border2);border-radius:1.5rem;max-width:760px;width:100%;max-height:90vh;overflow-y:auto;transform:translateY(30px) scale(.97);transition:transform .4s var(--ease);position:relative}}
.modal-overlay.open .modal{{transform:none}}
.modal-pdf{{width:100%;height:280px;background:#000;border-bottom:1px solid var(--border)}}
.modal-pdf iframe{{width:100%;height:100%;border:none}}
.modal-body{{padding:2rem}}
.modal-cat{{display:inline-flex;align-items:center;gap:.4rem;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;padding:.35rem .9rem;border-radius:50px;border:1px solid;margin-bottom:1.2rem}}
.modal-title{{font-family:var(--head);font-size:clamp(1.6rem,3vw,2.2rem);margin-bottom:.6rem;line-height:1.2}}
.modal-meta{{display:flex;gap:1.5rem;color:var(--sub);font-size:.9rem;margin-bottom:.4rem;flex-wrap:wrap}}
.modal-id{{font-family:monospace;font-size:.78rem;color:var(--muted);margin-bottom:1.5rem;opacity:.8}}
.modal-section{{font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);margin-bottom:.8rem}}
.modal-learnings{{list-style:none;display:flex;flex-direction:column;gap:.6rem;margin-bottom:2rem}}
.modal-learnings li{{display:flex;gap:.75rem;color:#cbd5e1;font-size:.95rem;line-height:1.5}}
.modal-learnings li::before{{content:"→";color:var(--green);flex-shrink:0;font-weight:700}}
.modal-actions{{display:flex;gap:1rem;flex-wrap:wrap}}
.btn-dl{{display:inline-flex;align-items:center;gap:.6rem;background:var(--green);color:#000;font-weight:700;font-size:.9rem;padding:.75rem 1.75rem;border-radius:50px;transition:all .3s;border:none;cursor:pointer;font-family:var(--body);text-decoration:none}}
.btn-dl:hover{{background:#0ea271;transform:translateX(3px)}}
.btn-close{{background:rgba(255,255,255,.06);border:1px solid var(--border2);color:var(--sub);font-size:.9rem;padding:.75rem 1.75rem;border-radius:50px;cursor:pointer;font-family:var(--body);transition:all .3s}}
.btn-close:hover{{background:rgba(255,255,255,.1);color:var(--text)}}
.modal-close-x{{position:absolute;top:1rem;right:1rem;width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,.06);border:1px solid var(--border2);color:var(--sub);font-size:1.2rem;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .3s;z-index:10}}
.modal-close-x:hover{{background:rgba(255,255,255,.12);color:var(--text)}}

/* REVEAL */
.reveal{{opacity:0;transform:translateY(28px);transition:opacity .7s var(--ease),transform .7s var(--ease)}}
.reveal.active{{opacity:1;transform:none}}

/* EMPTY STATE */
.empty-state{{grid-column:1/-1;text-align:center;padding:4rem;color:var(--muted)}}
.empty-state h3{{font-size:1.3rem;margin-bottom:.5rem;color:var(--sub)}}

@media(max-width:1024px){{.certs-grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:640px){{.certs-grid{{grid-template-columns:1fr}}.stats-row{{gap:2rem}}}}
</style>
</head>
<body>
<div class="ambient"><div class="amb1"></div><div class="amb2"></div></div>
<div id="nav-placeholder"></div>

<main class="wrap">
  <header class="hero reveal">
    <div class="hero-kicker"><span class="hero-dot"></span>Verified Learning</div>
    <h1>30+ Certifications &amp;<br><em>Counting</em></h1>
    <p class="hero-sub">A comprehensive record of every course, program, and competition credential — all in one place.</p>
  </header>

  <div class="stats-row reveal">
    <div class="stat"><div class="stat-n">{COUNTS['business']}</div><div class="stat-l">Business &amp; Entrepreneurship</div></div>
    <div class="stat"><div class="stat-n">{COUNTS['tech']}</div><div class="stat-l">Software &amp; Technology</div></div>
    <div class="stat"><div class="stat-n">{COUNTS['hackathon']}</div><div class="stat-l">Hackathons &amp; Events</div></div>
    <div class="stat"><div class="stat-n">30+</div><div class="stat-l">Total Credentials</div></div>
  </div>

  <div class="filter-bar reveal">
    <button class="fb active-all" data-cat="all" onclick="filterCerts('all',this)">✦ All ({len(certs_raw)})</button>
    <button class="fb" data-cat="business" onclick="filterCerts('business',this)">💼 Business ({COUNTS['business']})</button>
    <button class="fb" data-cat="tech" onclick="filterCerts('tech',this)">💻 Technology ({COUNTS['tech']})</button>
    <button class="fb" data-cat="hackathon" onclick="filterCerts('hackathon',this)">🏆 Hackathons ({COUNTS['hackathon']})</button>
  </div>

  <div class="search-wrap">
    <span class="search-icon">🔍</span>
    <input type="text" id="search-input" placeholder="Search certifications..." oninput="searchCerts(this.value)">
  </div>

  <div class="grid-label" id="grid-label">Showing all {len(certs_raw)} certifications</div>

  <div class="certs-grid" id="certs-grid">
    {cards_html}
  </div>
</main>

<!-- MODAL -->
<div class="modal-overlay" id="modal-overlay" onclick="if(event.target===this)closeModal()">
  <div class="modal" id="modal">
    <button class="modal-close-x" onclick="closeModal()">✕</button>
    <div class="modal-pdf" id="modal-pdf"></div>
    <div class="modal-body">
      <div class="modal-cat" id="modal-cat"></div>
      <h2 class="modal-title" id="modal-title"></h2>
      <div class="modal-meta" id="modal-meta"></div>
      <div class="modal-id" id="modal-id"></div>
      <div class="modal-section">Key Learnings</div>
      <ul class="modal-learnings" id="modal-learnings"></ul>
      <div class="modal-actions">
        <a id="modal-dl" class="btn-dl" download>⬇ Download Certificate</a>
        <button class="btn-close" onclick="closeModal()">Close</button>
      </div>
    </div>
  </div>
</div>

<div id="footer-placeholder"></div>

<script>
{modal_js}

const CAT_COLOR={{'business':'#10b981','tech':'#3b82f6','hackathon':'#8b5cf6'}};
const CAT_RGBA={{'business':'rgba(16,185,129,','tech':'rgba(59,130,246,','hackathon':'rgba(139,92,246,'}};
const CAT_LABEL={{'business':'💼 Business & Entrepreneurship','tech':'💻 Software & Technology','hackathon':'🏆 Hackathons & Events'}};

function openDetail(i){{
  const c=CERTS[i];
  const col=CAT_COLOR[c.cat]||'#10b981';
  const rgba=CAT_RGBA[c.cat]||'rgba(16,185,129,';
  document.getElementById('modal-pdf').innerHTML=`<iframe loading="lazy" src="${{c.pdf}}#toolbar=0&navpanes=0&scrollbar=0&view=FitH"></iframe>`;
  const mc=document.getElementById('modal-cat');
  mc.textContent=CAT_LABEL[c.cat]||c.cat;
  mc.style.color=col;mc.style.borderColor=rgba+'0.3)';mc.style.background=rgba+'0.08)';
  document.getElementById('modal-title').textContent=c.title;
  document.getElementById('modal-meta').innerHTML=`<span>${{c.issuer}}</span><span>•</span><span>${{c.date}}</span>`;
  document.getElementById('modal-id').textContent='Certificate ID: '+c.cid;
  const ul=document.getElementById('modal-learnings');
  ul.innerHTML=c.learnings.map(l=>`<li>${{l}}</li>`).join('');
  document.getElementById('modal-dl').href=c.pdf;
  document.getElementById('modal-overlay').classList.add('open');
  document.body.style.overflow='hidden';
}}

function closeModal(){{
  document.getElementById('modal-overlay').classList.remove('open');
  document.body.style.overflow='';
  document.getElementById('modal-pdf').innerHTML='';
}}

let currentCat='all';
function filterCerts(cat,btn){{
  currentCat=cat;
  document.querySelectorAll('.fb').forEach(b=>b.className='fb');
  btn.className='fb active-'+cat;
  applyFilters();
}}

function searchCerts(q){{applyFilters();}}

function applyFilters(){{
  const q=document.getElementById('search-input').value.toLowerCase();
  const cards=[...document.querySelectorAll('#certs-grid .cert-card')];
  let visible=0;
  cards.forEach(c=>{{
    const matchCat=currentCat==='all'||c.dataset.cat===currentCat;
    const name=c.querySelector('.cert-name').textContent.toLowerCase();
    const issuer=c.querySelector('.cert-issuer').textContent.toLowerCase();
    const matchQ=!q||name.includes(q)||issuer.includes(q);
    const show=matchCat&&matchQ;
    c.style.display=show?'flex':'none';
    if(show)visible++;
  }});
  document.getElementById('grid-label').textContent='Showing '+visible+' certification'+(visible!==1?'s':'');
  const empty=document.getElementById('empty-state');
  if(visible===0&&!empty){{
    const d=document.createElement('div');
    d.id='empty-state';d.className='empty-state';
    d.innerHTML='<h3>No results found</h3><p>Try a different search or filter.</p>';
    document.getElementById('certs-grid').appendChild(d);
  }}else if(visible>0&&empty){{empty.remove();}}
}}

document.addEventListener('DOMContentLoaded',()=>{{
  fetch('nav.html').then(r=>r.text()).then(d=>{{
    const t=document.createElement('div');t.innerHTML=d;
    const ph=document.getElementById('nav-placeholder');
    while(t.firstChild){{const c=t.firstChild;if(c.tagName==='SCRIPT'){{const s=document.createElement('script');s.textContent=c.textContent;document.body.appendChild(s);t.removeChild(c);}}else ph.appendChild(c);}}
  }});
  fetch('footer.html').then(r=>r.text()).then(d=>document.getElementById('footer-placeholder').innerHTML=d);
  const obs=new IntersectionObserver(es=>{{es.forEach(e=>{{if(e.isIntersecting)e.target.classList.add('active');}});}},{{threshold:.07,rootMargin:'0px 0px -40px 0px'}});
  document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));

  document.addEventListener('keydown',e=>{{if(e.key==='Escape')closeModal();}});
}});
</script>
</body>
</html>"""

with open('certifications.html','w',encoding='utf-8') as f:
    f.write(html)
print(f"Done — {len(certs_raw)} certs rebuilt")
