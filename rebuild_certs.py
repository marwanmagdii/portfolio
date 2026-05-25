import json, sys
sys.path.insert(0,'.')
from certs_data import CERTS

ACCENT = {'business':'#10b981','tech':'#3b82f6','hackathon':'#8b5cf6'}
RGBA   = {'business':'rgba(16,185,129,','tech':'rgba(59,130,246,','hackathon':'rgba(139,92,246,'}
ICON   = {'business':'💼','tech':'💻','hackathon':'🏆'}
LABEL  = {'business':'Business & Entrepreneurship','tech':'Software & Technology','hackathon':'Hackathons & Events'}
counts = {k:sum(1 for c in CERTS if c['cat']==k) for k in ['business','tech','hackathon']}

IS_IMG = lambda p: any(p.lower().endswith(x) for x in ['.jpg','.jpeg','.png'])

def card(i,c):
    cat=c['cat']; acc=ACCENT[cat]; rg=RGBA[cat]; icon=ICON[cat]
    thumb=c['thumb']
    if IS_IMG(thumb):
        top_inner = f'<img src="{thumb}" alt="{c["title"]}" style="width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s;"><div style="position:absolute;inset:0;background:linear-gradient(to bottom,transparent 30%,rgba(5,5,7,.85));"></div>'
    else:
        top_inner = f'<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,{rg}.12),{rg}.03));font-size:2.5rem;">{icon}</div>'
    tags = ''.join(f'<span class="tag">{l[:60]}</span>' for l in c['learnings'][:2])
    return f'''<div class="cert-card reveal" data-cat="{cat}" onclick="openD({i})">
      <div class="cert-img">{top_inner}
        <div style="position:absolute;top:.75rem;left:.75rem;">
          <span class="badge" style="color:{acc};border-color:{rg}.3);background:{rg}.1);backdrop-filter:blur(8px);">{icon} {LABEL[cat]}</span>
        </div>
      </div>
      <div class="cert-body">
        <h3 class="cert-title">{c["title"]}</h3>
        <div class="cert-meta"><span class="cert-iss">{c["issuer"]}</span><span class="cert-dt">{c["date"]}</span></div>
        <div class="cert-tags">{tags}</div>
      </div>
      <div class="cert-foot"><span style="color:{acc};font-size:.82rem;font-weight:600;">View Details →</span></div>
    </div>'''

cards_html = '\n'.join(card(i,c) for i,c in enumerate(CERTS))
js_data = 'const CERTS='+json.dumps(CERTS,ensure_ascii=False)+';'

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Certifications | Marwan Magdy</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
:root{{--bg:#050507;--surf:rgba(255,255,255,.025);--bdr:rgba(255,255,255,.08);--bdr2:rgba(255,255,255,.14);--text:#f1f5f9;--sub:#94a3b8;--muted:#64748b;--green:#10b981;--blue:#3b82f6;--purple:#8b5cf6;--H:'Playfair Display',serif;--B:'Outfit',sans-serif;--ease:cubic-bezier(.16,1,.3,1)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{background:var(--bg);color:var(--text);font-family:var(--B);overflow-x:hidden}}a{{text-decoration:none;color:inherit}}
.amb{{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}}
.amb::before{{content:'';position:absolute;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(16,185,129,.1) 0%,transparent 70%);top:-200px;right:-100px;animation:drift 22s ease-in-out infinite alternate}}
.amb::after{{content:'';position:absolute;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(139,92,246,.07) 0%,transparent 70%);bottom:-100px;left:-50px;animation:drift 18s ease-in-out infinite alternate-reverse}}
@keyframes drift{{0%{{transform:translate(0,0)}}100%{{transform:translate(30px,40px)}}}}
.wrap{{max-width:1280px;margin:0 auto;padding:0 5%;position:relative;z-index:1}}
.hero{{padding:9rem 0 4rem;text-align:center;border-bottom:1px solid var(--bdr)}}
.kicker{{display:inline-flex;align-items:center;gap:.5rem;background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.2);color:var(--green);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em;padding:.4rem 1rem;border-radius:50px;margin-bottom:1.5rem}}
.kicker-dot{{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 2s ease infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}
.hero h1{{font-family:var(--H);font-size:clamp(2.8rem,6vw,5rem);line-height:1.08;letter-spacing:-.03em;margin-bottom:1rem}}
.hero h1 em{{font-style:italic;background:linear-gradient(135deg,var(--green),var(--blue));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}}
.hero p{{color:var(--sub);font-size:1.05rem;max-width:500px;margin:0 auto}}
.stats{{display:flex;justify-content:center;gap:4rem;flex-wrap:wrap;padding:2.5rem 0;border-bottom:1px solid var(--bdr)}}
.stat-n{{font-size:2rem;font-weight:900;line-height:1}}.stat-l{{font-size:.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:.1em;margin-top:.3rem;text-align:center}}
.filters{{display:flex;justify-content:center;gap:.6rem;flex-wrap:wrap;padding:2rem 0}}
.fb{{padding:.5rem 1.25rem;border-radius:50px;border:1px solid var(--bdr2);color:var(--sub);font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;background:transparent;cursor:pointer;transition:all .25s var(--ease);font-family:var(--B)}}
.fb:hover{{border-color:rgba(255,255,255,.25);color:var(--text)}}
.fb.on-all{{background:var(--green);color:#000;border-color:var(--green);box-shadow:0 4px 20px rgba(16,185,129,.3)}}
.fb.on-business{{background:var(--green);color:#000;border-color:var(--green)}}
.fb.on-tech{{background:var(--blue);color:#fff;border-color:var(--blue);box-shadow:0 4px 20px rgba(59,130,246,.3)}}
.fb.on-hackathon{{background:var(--purple);color:#fff;border-color:var(--purple);box-shadow:0 4px 20px rgba(139,92,246,.3)}}
.search-row{{max-width:480px;margin:0 auto 1.5rem;position:relative}}
.search-row input{{width:100%;background:rgba(255,255,255,.03);border:1px solid var(--bdr2);color:var(--text);font-family:var(--B);font-size:.92rem;padding:.85rem 1.2rem .85rem 2.8rem;border-radius:50px;outline:none;transition:border-color .3s}}
.search-row input:focus{{border-color:rgba(16,185,129,.4)}}.search-row input::placeholder{{color:var(--muted)}}
.search-icon{{position:absolute;left:1rem;top:50%;transform:translateY(-50%);color:var(--muted)}}
.count-label{{text-align:center;font-size:.78rem;color:var(--muted);text-transform:uppercase;letter-spacing:.1em;margin-bottom:2rem}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem;padding-bottom:6rem}}
.cert-card{{background:var(--surf);border:1px solid var(--bdr);border-radius:1.1rem;overflow:hidden;cursor:pointer;transition:transform .35s var(--ease),border-color .3s,box-shadow .3s;display:flex;flex-direction:column}}
.cert-card:hover{{transform:translateY(-6px);border-color:rgba(255,255,255,.16);box-shadow:0 16px 40px rgba(0,0,0,.5)}}
.cert-img{{height:160px;position:relative;overflow:hidden;background:#0a0a12;flex-shrink:0}}
.cert-card:hover .cert-img img{{transform:scale(1.06)}}
.badge{{font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;padding:.28rem .7rem;border-radius:50px;border:1px solid;white-space:nowrap;display:inline-block}}
.cert-body{{padding:1.1rem 1.25rem .8rem;flex:1}}
.cert-title{{font-family:var(--H);font-size:1rem;line-height:1.3;margin-bottom:.5rem;color:var(--text)}}
.cert-card:hover .cert-title{{color:var(--green)}}
.cert-meta{{display:flex;justify-content:space-between;margin-bottom:.6rem}}
.cert-iss{{font-size:.8rem;color:var(--sub);font-weight:500}}.cert-dt{{font-size:.75rem;color:var(--muted)}}
.cert-tags{{display:flex;flex-wrap:wrap;gap:.35rem}}
.tag{{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);color:var(--sub);font-size:.65rem;padding:.2rem .55rem;border-radius:5px;line-height:1.4}}
.cert-foot{{padding:.75rem 1.25rem;border-top:1px solid rgba(255,255,255,.05)}}
.modal-ov{{position:fixed;inset:0;background:rgba(0,0,0,.88);backdrop-filter:blur(14px);z-index:1000;display:flex;align-items:center;justify-content:center;padding:1.5rem;opacity:0;pointer-events:none;transition:opacity .3s}}
.modal-ov.open{{opacity:1;pointer-events:all}}
.modal{{background:#0c0c12;border:1px solid var(--bdr2);border-radius:1.4rem;max-width:720px;width:100%;max-height:90vh;overflow-y:auto;transform:translateY(24px) scale(.97);transition:transform .4s var(--ease);position:relative}}
.modal-ov.open .modal{{transform:none}}
.mpdf{{width:100%;height:320px;background:#111;border-bottom:1px solid var(--bdr);overflow:hidden}}
.mpdf iframe{{width:100%;height:100%;border:none}}
.mpdf img{{width:100%;height:100%;object-fit:contain;background:#fff}}
.mbody{{padding:1.75rem}}
.mcat{{display:inline-flex;align-items:center;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;padding:.3rem .85rem;border-radius:50px;border:1px solid;margin-bottom:1rem}}
.mtitle{{font-family:var(--H);font-size:clamp(1.4rem,3vw,2rem);margin-bottom:.5rem;line-height:1.2}}
.mmeta{{display:flex;gap:1.5rem;color:var(--sub);font-size:.88rem;margin-bottom:1.25rem;flex-wrap:wrap}}
.msec{{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);margin-bottom:.7rem}}
.mlist{{list-style:none;display:flex;flex-direction:column;gap:.55rem;margin-bottom:1.75rem}}
.mlist li{{display:flex;gap:.65rem;color:#cbd5e1;font-size:.92rem;line-height:1.5}}
.mlist li::before{{content:"→";color:var(--green);flex-shrink:0;font-weight:700}}
.mclose{{position:absolute;top:.9rem;right:.9rem;width:34px;height:34px;border-radius:50%;background:rgba(255,255,255,.07);border:1px solid var(--bdr2);color:var(--sub);font-size:1.1rem;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .25s;z-index:10}}
.mclose:hover{{background:rgba(255,255,255,.12);color:var(--text)}}
.mbtn-close{{background:rgba(255,255,255,.06);border:1px solid var(--bdr2);color:var(--sub);font-size:.88rem;padding:.7rem 1.5rem;border-radius:50px;cursor:pointer;font-family:var(--B);transition:all .3s}}
.mbtn-close:hover{{background:rgba(255,255,255,.1);color:var(--text)}}
.reveal{{opacity:0;transform:translateY(24px);transition:opacity .7s var(--ease),transform .7s var(--ease)}}.reveal.active{{opacity:1;transform:none}}
@media(max-width:1024px){{.grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:600px){{.grid{{grid-template-columns:1fr}}.stats{{gap:2rem}}}}
</style>
</head>
<body>
<div class="amb"></div>
<div id="nav-ph"></div>
<main class="wrap">
  <header class="hero reveal">
    <div class="kicker"><span class="kicker-dot"></span>Verified Learning</div>
    <h1>30+ Certifications &amp;<br><em>Counting</em></h1>
    <p>Every course, program, and competition credential — all in one place.</p>
  </header>
  <div class="stats reveal">
    <div><div class="stat-n">{counts['business']}</div><div class="stat-l">Business &amp; Entrepreneurship</div></div>
    <div><div class="stat-n">{counts['tech']}</div><div class="stat-l">Software &amp; Technology</div></div>
    <div><div class="stat-n">{counts['hackathon']}</div><div class="stat-l">Hackathons &amp; Events</div></div>
    <div><div class="stat-n">{len(CERTS)}+</div><div class="stat-l">Total Credentials</div></div>
  </div>
  <div class="filters reveal">
    <button class="fb on-all" onclick="filt('all',this)">✦ All ({len(CERTS)})</button>
    <button class="fb" onclick="filt('business',this)">💼 Business ({counts['business']})</button>
    <button class="fb" onclick="filt('tech',this)">💻 Technology ({counts['tech']})</button>
    <button class="fb" onclick="filt('hackathon',this)">🏆 Hackathons ({counts['hackathon']})</button>
  </div>
  <div class="search-row"><span class="search-icon">🔍</span><input type="text" placeholder="Search certifications..." oninput="search(this.value)"></div>
  <div class="count-label" id="cnt">Showing all {len(CERTS)} certifications</div>
  <div class="grid" id="grid">{cards_html}</div>
</main>
<div class="modal-ov" id="ov" onclick="if(event.target===this)close()">
  <div class="modal">
    <button class="mclose" onclick="close()">✕</button>
    <div class="mpdf" id="mpdf"></div>
    <div class="mbody">
      <div class="mcat" id="mcat"></div>
      <h2 class="mtitle" id="mtitle"></h2>
      <div class="mmeta" id="mmeta"></div>
      <div class="msec">Key Learnings</div>
      <ul class="mlist" id="mlist"></ul>
      <button class="mbtn-close" onclick="close()">Close</button>
    </div>
  </div>
</div>
<div id="foot-ph"></div>
<script>
{js_data}
const ACC={{'business':'#10b981','tech':'#3b82f6','hackathon':'#8b5cf6'}};
const RG={{'business':'rgba(16,185,129,','tech':'rgba(59,130,246,','hackathon':'rgba(139,92,246,'}};
const LBL={{'business':'💼 Business & Entrepreneurship','tech':'💻 Software & Technology','hackathon':'🏆 Hackathons & Events'}};
const isImg=s=>s&&/\\.(jpg|jpeg|png)$/i.test(s);
function openD(i){{
  const c=CERTS[i],col=ACC[c.cat],rg=RG[c.cat];
  const el=document.getElementById('mpdf');
  if(isImg(c.thumb))el.innerHTML=`<img src="${{c.thumb}}" alt="${{c.title}}">`;
  else if(c.pdf&&c.pdf.endsWith('.pdf'))el.innerHTML=`<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;background:#111;text-align:center;"><div style="font-size:3rem;margin-bottom:1rem;">📄</div><a href="${{c.pdf}}" target="_blank" style="background:#10b981;color:#000;padding:0.75rem 1.5rem;border-radius:50px;text-decoration:none;font-weight:700;font-size:0.9rem;transition:transform 0.3s;">View Certificate PDF</a></div>`;
  else el.innerHTML='<div style="display:flex;align-items:center;justify-content:center;height:100%;color:#64748b;">No preview</div>';
  const mc=document.getElementById('mcat');
  mc.textContent=LBL[c.cat];mc.style.color=col;mc.style.borderColor=rg+'0.3)';mc.style.background=rg+'0.08)';
  document.getElementById('mtitle').textContent=c.title;
  document.getElementById('mmeta').innerHTML=`<span>${{c.issuer}}</span><span>·</span><span>${{c.date}}</span>`;
  document.getElementById('mlist').innerHTML=c.learnings.map(l=>`<li>${{l}}</li>`).join('');
  document.getElementById('ov').classList.add('open');
  document.body.style.overflow='hidden';
}}
function close(){{document.getElementById('ov').classList.remove('open');document.body.style.overflow='';document.getElementById('mpdf').innerHTML='';}}
let curCat='all';
function filt(cat,btn){{curCat=cat;document.querySelectorAll('.fb').forEach(b=>b.className='fb');btn.className='fb on-'+cat;applyF();}}
function search(q){{applyF();}}
function applyF(){{
  const q=document.querySelector('.search-row input').value.toLowerCase();
  const cards=[...document.querySelectorAll('#grid .cert-card')];
  let v=0;
  cards.forEach(c=>{{
    const ok=(curCat==='all'||c.dataset.cat===curCat)&&(!q||c.querySelector('.cert-title').textContent.toLowerCase().includes(q)||c.querySelector('.cert-iss').textContent.toLowerCase().includes(q));
    c.style.display=ok?'flex':'none';if(ok)v++;
  }});
  document.getElementById('cnt').textContent='Showing '+v+' certification'+(v!==1?'s':'');
}}
document.addEventListener('DOMContentLoaded',()=>{{
  fetch('nav.html').then(r=>r.text()).then(d=>{{const t=document.createElement('div');t.innerHTML=d;const ph=document.getElementById('nav-ph');while(t.firstChild){{const c=t.firstChild;if(c.tagName==='SCRIPT'){{const s=document.createElement('script');s.textContent=c.textContent;document.body.appendChild(s);t.removeChild(c);}}else ph.appendChild(c);}}}});
  fetch('footer.html').then(r=>r.text()).then(d=>document.getElementById('foot-ph').innerHTML=d);
  const obs=new IntersectionObserver(es=>{{es.forEach(e=>{{if(e.isIntersecting)e.target.classList.add('active');}});}},{{threshold:.07}});
  document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
  document.addEventListener('keydown',e=>{{if(e.key==='Escape')close();}});
}});
</script>
</body></html>"""

with open('certifications.html','w',encoding='utf-8') as f:
    f.write(html)
print(f"Rebuilt — {len(CERTS)} certs")
