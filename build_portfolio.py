with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract head up to </head>
head_end = content.find('</head>')
if head_end == -1:
    print("Could not find </head>")
    exit()
head_html = content[:head_end]

# Extract navbar
nav_start = content.find('<div class="nav-wrapper">')
nav_end = content.find('</nav>', nav_start)
if nav_start != -1 and nav_end != -1:
    # Need to include the wrapper ending div
    wrapper_end = content.find('</div>', nav_end)
    navbar_html = content[nav_start:wrapper_end + 6]
else:
    navbar_html = ''
    
navbar_html = navbar_html.replace('href="#', 'href="index.html#')

# Extract footer
foot_start = content.find('<footer')
foot_end = content.find('</footer>', foot_start)
if foot_start != -1 and foot_end != -1:
    footer_html = content[foot_start:foot_end + 9]
else:
    footer_html = ''
    
footer_html = footer_html.replace('href="#', 'href="index.html#')

bento_css = """
<style>
/* ═══════════════════ BENTO BOX PORTFOLIO ═══════════════════ */
.portfolio-bento-section {
    padding: 160px 0 100px;
    position: relative;
    background: var(--bg-dark);
}

.portfolio-bento-header {
    text-align: center;
    margin-bottom: 50px;
}

.portfolio-bento-header h2 {
    font-size: clamp(2rem, 4vw, 3rem);
    margin-bottom: 16px;
    font-family: var(--font-heading);
}

.portfolio-bento-header p {
    color: var(--text-muted);
}

.portfolio-bento-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 20px;
}

.bento-card {
    position: relative;
    border-radius: 32px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    cursor: pointer;
    min-height: 440px;
    padding: 30px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.bento-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4);
}

.bento-card img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    transition: transform 0.6s ease;
}

.bento-card:hover img {
    transform: scale(1.04);
}

.bento-image-wrapper {
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding-bottom: 24px;
}

.bento-caption {
    text-align: center;
    font-weight: 700;
    font-size: 1.25rem;
    color: #fff;
    font-family: var(--font-heading);
    letter-spacing: 0.5px;
    margin-top: auto;
    text-shadow: 0 4px 12px rgba(0,0,0,0.4);
}

/* Color Themes */
.card-bg-navy { background: linear-gradient(135deg, #0c182c, #132440); }
.card-bg-emerald { background: linear-gradient(135deg, #0d3b26, #14593a); border:1px solid rgba(13,59,38,0.5); }
.card-bg-violet { background: linear-gradient(135deg, #2b1154, #411b7e); }
.card-bg-slate { background: linear-gradient(135deg, #1e293b, #334155); }
.card-bg-crimson { background: linear-gradient(135deg, #4a1515, #7a2222); }
:root.light-mode .card-bg-emerald { background: #eaffe9; }
:root.light-mode .card-bg-emerald .bento-caption { color: #0d3b26; text-shadow: none; }

/* Grid Spanning */
.span-col-2 { grid-column: span 2; }
.span-row-2 { grid-row: span 2; }

@media (max-width: 900px) {
    .portfolio-bento-grid { grid-template-columns: repeat(2, 1fr); }
    .span-col-2 { grid-column: span 2; }
}

@media (max-width: 768px) {
    .portfolio-bento-grid { grid-template-columns: 1fr; }
    .span-col-2 { grid-column: span 1; }
    .bento-card { min-height: 380px; }
}
</style>
"""

head_html += bento_css + '\n</head>'

body_html = f"""
<body>
    {navbar_html}
    
    <main>
    <section class="portfolio-bento-section" id="portfolio">
        <div class="container">
            <div class="portfolio-bento-header">
                <h2>Featured <span class="gradient-text">Projects</span></h2>
                <p>Creative built with strategy. Designed for results.</p>
            </div>
            
            <div class="portfolio-bento-grid">
                <div class="bento-card span-col-2 card-bg-navy">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/1.png" alt="Restaurant Social Campaign" loading="lazy" style="border-radius:12px;">
                    </div>
                    <div class="bento-caption">Restaurant Brand Launch</div>
                </div>

                <div class="bento-card card-bg-emerald">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/2.png" alt="E-Commerce Ad Creative" loading="lazy" style="border-radius:12px;">
                    </div>
                    <div class="bento-caption">E-Commerce Growth</div>
                </div>

                <div class="bento-card card-bg-violet">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/3.png" alt="Product Launch Campaign" loading="lazy" style="border-radius:12px;">
                    </div>
                    <div class="bento-caption">Premium Product Reveal</div>
                </div>

                <div class="bento-card card-bg-slate">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/4.png" alt="Social Media Strategy" loading="lazy" style="border-radius:12px;">
                    </div>
                    <div class="bento-caption">Full-Funnel Rollout</div>
                </div>

                <div class="bento-card card-bg-crimson">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/4__1_.png" alt="Carousel Ad Design" loading="lazy" style="border-radius:12px;">
                    </div>
                    <div class="bento-caption">Scroll-Stopping Creatives</div>
                </div>

                <div class="bento-card span-col-2 card-bg-navy">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/6.png" alt="Lead Gen Funnel Design" loading="lazy" style="border-radius:12px;">
                    </div>
                    <div class="bento-caption">High-Ticket Funnel</div>
                </div>
                
                <div class="bento-card card-bg-emerald">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/5.png" alt="Video Ads" loading="lazy" style="border-radius:12px;">
                    </div>
                    <div class="bento-caption">Thumb-Stopping Video</div>
                </div>
            </div>
        </div>
    </section>
    </main>

    {footer_html}

    <script>
    const themeBtn = document.querySelector('.theme-toggle');
    if (themeBtn) {{
        themeBtn.addEventListener('click', () => {{
            document.documentElement.classList.toggle('light-mode');
        }});
    }}
    </script>
</body>
</html>
"""

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(head_html + '\n' + body_html)

print("Created portfolio.html successfully")
