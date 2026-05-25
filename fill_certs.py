import re

with open('certifications.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Complete, accurate data for every certificate
# Format: 'Title match': ('correct date', ['learning1', 'learning2', 'learning3'])
CERT_DATA = {
    "Founder Academy Deep Dive": (
        "2024",
        ["Underwent an intensive deep-dive into startup architecture, product-market fit, and fundraising mechanics with ALX Ventures.", "Refined investor storytelling and pitch narrative for early-stage B2B ventures.", "Built a structured founder operating system for team leadership and OKR tracking."]
    ),
    "McKinsey Forward Program": (
        "2024",
        ["Completed McKinsey's elite leadership program covering problem-solving, structured thinking, and executive communication.", "Applied McKinsey's analytical frameworks — MECE principle, issue trees, and hypothesis-driven analysis — to real business challenges.", "Graduated as a McKinsey Forward Fellow, recognized for demonstrated leadership and analytical excellence."]
    ),
    "Mini MBA in Entrepreneurship": (
        "2023",
        ["Covered the full entrepreneurship lifecycle: idea validation, business modeling, fundraising, and scaling.", "Applied frameworks like the Business Model Canvas and Value Proposition Canvas to real startup scenarios.", "Developed financial literacy for entrepreneurs — cash flow management, unit economics, and investor-ready projections."]
    ),
    "Business &amp; Start Up Booster": (
        "Oct 2023",
        ["Designed sustainable revenue streams and optimized cost structures for early-stage ventures.", "Mastered scaling tactics including growth hacking, channel strategy, and product-led growth.", "Practiced pitching to angel investors and seed funds with structured narrative and financial modeling."]
    ),
    "Balanced Business Model": (
        "Aug 2023",
        ["Applied Lean Canvas principles to design, test, and iterate on business models for high-growth startups.", "Evaluated customer segments and value propositions to achieve sustainable product-market fit.", "Stress-tested business model assumptions by mapping revenue streams against cost structures."]
    ),
    "Strategy for SMEs": (
        "Jan 2024",
        ["Developed competitive strategy frameworks tailored for Small and Medium Enterprises in emerging markets.", "Analyzed market positioning, differentiation strategies, and competitive moat building.", "Optimized resource allocation and operational efficiency for maximum return on investment."]
    ),
    "Entrepreneurship 2.0: Business Model Canvas": (
        "2023",
        ["Mastered the Business Model Canvas as a live tool for rapid startup ideation and validation.", "Mapped all nine building blocks — from key partners to customer relationships — for a real venture.", "Learned to pivot business model assumptions based on user feedback and market signals."]
    ),
    "Entrepreneurship Ecosystem": (
        "2023",
        ["Studied the structure and dynamics of startup ecosystems across MENA and global markets.", "Understood how accelerators, incubators, VCs, and corporates interact within innovation ecosystems.", "Identified opportunities within the Egyptian startup ecosystem and mapped key players and funding pathways."]
    ),
    "Innov Egypt Entrepreneurship Program": (
        "2023",
        ["Participated in Egypt's premier national entrepreneurship program run by TIEC (Technology Innovation and Entrepreneurship Center).", "Developed a high-growth startup roadmap including market analysis, go-to-market strategy, and funding plan.", "Engaged with top mentors from Egypt's tech and investment ecosystem to validate and sharpen the venture thesis."]
    ),
    "Pitching Your Business Idea": (
        "2023",
        ["Mastered the structure of a winning investor pitch: problem, solution, market size, traction, and ask.", "Practiced delivery, storytelling, and handling tough investor Q&A under simulated conditions.", "Developed a compelling pitch deck narrative that communicates vision, differentiation, and commercial potential."]
    ),
    "Project Management Crash Course": (
        "2024",
        ["Applied Agile and Scrum methodologies to manage multi-functional project teams.", "Learned to define project scope, manage timelines, mitigate risks, and track KPIs using sprint reviews.", "Practiced cross-functional team coordination and stakeholder communication within the ALX framework."]
    ),
    "Business English Track": (
        "2024",
        ["Completed intensive business English training focused on professional writing, executive communication, and presentation skills.", "Developed the ability to write compelling business proposals, investor emails, and executive summaries.", "Refined verbal communication skills for high-stakes environments such as investor pitches and corporate meetings."]
    ),
    "Software Tester": (
        "2024",
        ["Completed Egypt's DEPI national program specializing in Software Quality Assurance with AMIT Learning.", "Mastered manual and automated testing methodologies including functional, regression, and performance testing.", "Applied industry-standard tools — JIRA for bug tracking, Selenium for automation, Postman for API testing — in real projects."]
    ),
    "DEPI Round 2 Graduation Ceremony": (
        "2024",
        ["Successfully graduated from Egypt's Digital Egypt Pioneers Initiative (DEPI) Round 2 as a QA Tester.", "Demonstrated mastery in software testing practices through a combination of coursework and live project assessments.", "One of an elite cohort selected to advance through the national tech training program backed by the Egyptian government."]
    ),
    "Mobile Development (Flutter)": (
        "2023",
        ["Trained in cross-platform mobile development using Flutter and Dart at ITI (Information Technology Institute).", "Built and deployed mobile applications with state management (Provider/Bloc), REST API integration, and Firebase.", "Developed the technical foundation that directly informs Riadi's mobile product architecture."]
    ),
    "AI Introduction &amp; Applications": (
        "2023",
        ["Gained foundational understanding of AI and Machine Learning concepts at Zewail City of Science and Technology.", "Explored real-world AI applications in healthcare, finance, and sustainability across the MENA region.", "Applied introductory ML models and understood the product implications of AI integration."]
    ),
    "Intro to AI and Applications": (
        "2023",
        ["Covered the fundamentals of Artificial Intelligence including supervised/unsupervised learning and neural networks.", "Explored AI application development patterns and how to integrate AI capabilities into existing products.", "Built analytical intuition for evaluating AI solutions for startup use cases and investor narratives."]
    ),
    "ITIDA Gigs Certification": (
        "2024",
        ["Completed Egypt's ITIDA Gigs digital freelancing and technology certification program.", "Developed digital skills validated by the Information Technology Industry Development Agency (ITIDA).", "Gained certification in digital work readiness and remote collaboration for the Egyptian digital economy."]
    ),
    "ITIDA Gigs Certification (Advanced)": (
        "2024",
        ["Completed the advanced level of Egypt's ITIDA Gigs certification, demonstrating superior digital proficiency.", "Validated expertise in technology-driven project management, digital marketing, and online business operations.", "Recognized by ITIDA as an advanced digital professional within Egypt's national tech skills ecosystem."]
    ),
    "Blockchain (Part 1)": (
        "2023",
        ["Studied the foundational concepts of blockchain technology including decentralization, consensus mechanisms, and cryptographic hashing.", "Explored the architecture of public and private blockchains and their business applications across industries.", "Evaluated blockchain's potential impact on fintech, supply chain, and digital identity solutions."]
    ),
    "Blockchain (Part 2)": (
        "2023",
        ["Deepened understanding of smart contracts, decentralized applications (dApps), and the Ethereum ecosystem.", "Explored token economics, NFTs, and the emerging Web3 landscape for startup opportunities.", "Applied blockchain concepts to evaluate real-world use cases for integration into tech-driven ventures."]
    ),
    "Digital Marketing Challenger": (
        "2023",
        ["Completed Udacity's Digital Marketing Challenger program covering SEO, SEM, social media, and content marketing.", "Applied data-driven marketing frameworks to build and measure growth campaigns for digital products.", "Developed skills in Google Analytics, paid advertising strategy, and conversion rate optimization."]
    ),
    "Huawei Developer Competition 2025": (
        "2025",
        ["Won 2nd Place across North Africa among 389 teams and 1,408+ participants as Technical Lead of AIX.", "Built and deployed an AI-driven solution under extreme competitive pressure over multiple elimination rounds.", "Demonstrated applied expertise in AI architecture, rapid prototyping, and cross-functional technical leadership."]
    ),
    "NASA Space Apps Challenge": (
        "Oct 2024",
        ["Selected as a Global Nominee out of thousands of global teams for NASA Space Apps Challenge 2024.", "Led Team Green Pulse in developing a tech solution to address climate change using NASA open data.", "Gained international exposure and recognition on the global NASA innovation platform."]
    ),
    "NASA Space Apps Cairo 2024": (
        "Oct 2024",
        ["Won 1st Place at the NASA Space Apps Cairo 2024 local competition as Team Leader of Green Pulse.", "Developed a sustainability-focused tech solution leveraging NASA datasets and geospatial tools.", "Advanced from local winner to Global Nominee, representing Egypt on the world stage."]
    ),
    "NASA Space Apps Cairo Bootcamp 2025": (
        "2025",
        ["Participated in the NASA Space Apps Cairo 2025 preparatory bootcamp covering space tech, data science, and design thinking.", "Sharpened skills in rapid ideation, problem framing, and building MVPs for planetary-scale challenges.", "Networked with top scientists, engineers, and entrepreneurs within Egypt's space and deep-tech community."]
    ),
    "AI for Life Hackathon": (
        "Dec 2025",
        ["Won 2nd Place at the 'AI for Life' Human-Centered Hackathon held at Cairo ICT 2025.", "Built a human-centered AI solution blending empathy, design thinking, and technical implementation.", "Competed at one of the Arab world's largest technology events with thousands of attendees and global judges."]
    ),
    "E-Gnite Bootcamp and Competition": (
        "2024",
        ["Competed in Nile University's E-Gnite entrepreneurship bootcamp and innovation competition.", "Developed and pitched a startup concept through structured design thinking and lean startup workshops.", "Received mentorship from Nile University faculty and industry experts across tech, business, and impact sectors."]
    ),
    "ESG Contest 2nd Place": (
        "2023",
        ["Won 2nd Place at Credit Agricole Egypt's CAE Green Contest 2023 with the 'Unbounded' inclusive app concept.", "Developed an ESG (Environmental, Social, Governance) focused technology solution addressing social inclusion.", "Competed against top Egyptian university students and professionals in a bank-sponsored sustainability innovation challenge."]
    ),
    "Accelerator Backing": (
        "Mar 2026",
        ["Secured acceptance and backing from Flat6Labs — the MENA region's leading startup accelerator — for Riadi.", "Won 1st Place at the Flat6Labs & Shell Intilaaqah Competition at EGYPES 2026 (Egypt Energy Show).", "Gained access to Flat6Labs' investor network, mentorship ecosystem, and pan-MENA startup community."]
    ),
    "Arab Youth Summit": (
        "2023",
        ["Represented innovative Arab youth at the Arab Youth Summit during Arab Sustainable Development Week.", "Engaged with policymakers, UN representatives, and sustainability leaders on technology-driven solutions for the Arab world.", "Networked with top young leaders and entrepreneurs from across the Arab League on shared sustainability challenges."]
    ),
}

def replace_learnings(match):
    full_btn = match.group(0)
    # Find the title
    title_match = re.search(r"openModal\('([^']+)'", full_btn)
    if not title_match:
        return full_btn
    
    title = title_match.group(1)
    
    # Find matching data
    data = None
    for key, val in CERT_DATA.items():
        # decode HTML entities for comparison
        clean_key = key.replace('&amp;', '&')
        clean_title = title.replace('&', '&amp;').replace('&amp;amp;', '&amp;')
        if clean_key == title or key == title:
            data = val
            break
    
    if not data:
        # Try partial match
        for key, val in CERT_DATA.items():
            clean_key = key.replace('&amp;', '&')
            if clean_key in title or title in clean_key:
                data = val
                break
    
    if not data:
        return full_btn  # Keep as-is if no match
    
    date_str, learnings = data
    
    # Build the learnings JSON string (HTML-encoded for attribute)
    import json
    learnings_json = json.dumps(learnings)
    # Encode double quotes as &quot; for HTML attribute
    learnings_attr = learnings_json.replace('"', '&quot;')
    
    # Build the new onclick
    # Extract existing file src from the current onclick
    file_match = re.search(r",\s*'(assets/certifications/[^']+)'\)", full_btn)
    file_src = file_match.group(1) if file_match else ''
    
    # Extract issuer
    issuer_match = re.search(r"openModal\('[^']+',\s*'([^']+)'", full_btn)
    issuer = issuer_match.group(1) if issuer_match else ''
    
    if file_src:
        new_onclick = f"openModal('{title}', '{issuer}', '{date_str}', '{learnings_attr}', '{file_src}')"
    else:
        new_onclick = f"openModal('{title}', '{issuer}', '{date_str}', '{learnings_attr}')"
    
    new_btn = f'<button class="cert-modal-btn" onclick="{new_onclick}">More</button>'
    return new_btn

# Replace all buttons
pattern = re.compile(r'<button class="cert-modal-btn" onclick="[^"]*">More</button>')
content = pattern.sub(replace_learnings, content)

with open('certifications.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('All certification data updated with real, specific learnings.')
