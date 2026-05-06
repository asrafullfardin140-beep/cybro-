import re

with open("index.html", "r") as f:
    lines = f.readlines()

# The CSS block starts around 2701 and the JS ends around 3303.
# We look for the exact comments and tags.
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if "<!-- ═══════════════════ FEATURED PROJECTS ═══════════════════ -->" in line:
        start_idx = i
    if "})();" in line and "</script>" in lines[i+1]:
        end_idx = i + 1

if start_idx != -1 and end_idx != -1:
    new_html = """    <!-- ═══════════════════ FEATURED PROJECTS (BENTO BOX) ═══════════════════ -->
    <section class="portfolio-bento-section" id="portfolio">
        <div class="container">
            <div class="portfolio-bento-header">
                <h2>Featured <span class="gradient-text">Projects</span></h2>
                <p>Creative built with strategy. Designed for results.</p>
            </div>
            
            <div class="portfolio-bento-grid">
                <!-- Span 2, Navy -->
                <div class="bento-card span-col-2 card-bg-navy">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/1.png" alt="Restaurant Social Campaign" loading="lazy">
                    </div>
                    <div class="bento-caption">Restaurant Brand Launch</div>
                </div>

                <!-- Span 1, Emerald -->
                <div class="bento-card card-bg-emerald">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/2.png" alt="E-Commerce Ad Creative" loading="lazy">
                    </div>
                    <div class="bento-caption">E-Commerce Growth</div>
                </div>

                <!-- Span 1, Violet -->
                <div class="bento-card card-bg-violet">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/3.png" alt="Product Launch Campaign" loading="lazy">
                    </div>
                    <div class="bento-caption">Premium Product Reveal</div>
                </div>

                <!-- Span 1, Slate -->
                <div class="bento-card card-bg-slate">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/4.png" alt="Social Media Strategy" loading="lazy">
                    </div>
                    <div class="bento-caption">Full-Funnel Rollout</div>
                </div>

                <!-- Span 1, Crimson -->
                <div class="bento-card card-bg-crimson">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/4__1_.png" alt="Carousel Ad Design" loading="lazy">
                    </div>
                    <div class="bento-caption">Scroll-Stopping Creatives</div>
                </div>

                <!-- Span 2, Navy -->
                <div class="bento-card span-col-2 card-bg-navy">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/6.png" alt="Lead Gen Funnel Design" loading="lazy">
                    </div>
                    <div class="bento-caption">High-Ticket Funnel</div>
                </div>
                
                <!-- Span 1, Emerald -->
                <div class="bento-card card-bg-emerald">
                    <div class="bento-image-wrapper">
                        <img src="portfolio/5.png" alt="Video Ads" loading="lazy">
                    </div>
                    <div class="bento-caption">Thumb-Stopping Video</div>
                </div>
            </div>
        </div>
    </section>
"""
    # Replace the chunk
    lines = lines[:start_idx] + [new_html] + lines[end_idx+1:]
    
    # Let's also remove the extra <!-- Lightbox Modal --> block that comes right before the script
    # Actually wait, the script is at 3302. Let's write the whole array back
    with open("index.html", "w") as f:
        f.writelines(lines)
    print("SUCCESS")
else:
    print(f"FAILED: start_idx={start_idx}, end_idx={end_idx}")

