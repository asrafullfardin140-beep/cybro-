import re

files = [
    'cybro_marketing.html',
    'social-media.html', 
    'lead-generation.html', 
    'ai-automation.html', 
    'web-development.html'
]

# Base structure of the index
base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cybro Marketing | Future-Proof Your Growth</title>
    <!-- FONT & ICONS -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <style>
/* ───────── GLOBAL CSS INJECTED ───────── */
__GLOBAL_CSS__
/* ───────── COMPONENT CSS INJECTED ───────── */
__COMPONENT_CSS__

/* ───────── SPA ROUTING CSS ───────── */
.page-section {
    display: none; /* Hidden by default */
    opacity: 0;
    transition: opacity 0.3s ease;
}
.page-section.active {
    display: block; /* Shown when active */
    opacity: 1;
}
    </style>
</head>
<body>
    __NAVBAR__
    
    <main id="app-content">
__SECTIONS__
    </main>
    
    __FOOTER__

    <!-- ───────── GLOBAL JS INJECTED ───────── -->
    <script>
__GLOBAL_JS__

/* ───────── SPA ROUTING JS ───────── */
function handleRoute() {
    let hash = window.location.hash || '#home';
    if(hash === '#contact' || hash === '#results' || hash === '#about' || hash.includes('packages')) {
        // If it's a sub-anchor, we don't necessarily want to change the active page unless we are not on home
        // For simplicity, route these to home first if needed, or let native browser scrolling happen if already on home.
        const homeSection = document.getElementById('home');
        if(!homeSection.classList.contains('active')) {
             document.querySelectorAll('.page-section').forEach(sec => sec.classList.remove('active'));
             homeSection.classList.add('active');
        }
        setTimeout(() => {
            const target = document.querySelector(hash);
            if(target) target.scrollIntoView({behavior: 'smooth'});
        }, 100);
        return;
    }

    // Hide all sections
    document.querySelectorAll('.page-section').forEach(sec => sec.classList.remove('active'));
    
    // Show target section
    const targetSection = document.getElementById(hash.substring(1));
    if (targetSection) {
        targetSection.classList.add('active');
        window.scrollTo(0, 0);
    } else {
        // Fallback to home
        document.getElementById('home').classList.add('active');
        window.history.replaceState(null, null, '#home');
        window.scrollTo(0, 0);
    }
}

window.addEventListener('hashchange', handleRoute);
window.addEventListener('DOMContentLoaded', handleRoute);

    </script>
</body>
</html>
"""

# 1. Read the core style.css
with open('style.css', 'r', encoding='utf-8') as f:
    global_css = f.read()

component_css_set = set() # To store unique extra CSS blocks not in style.css
sections_html = []
navbar_html = ""
footer_html = ""
global_js_set = set()

def extract_between(content, start_marker, end_marker):
    start = content.find(start_marker)
    if start == -1: return ""
    start += len(start_marker)
    end = content.find(end_marker, start)
    if end == -1: return ""
    return content[start:end]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Determine strict section ID (e.g. social-media.html -> social-media)
        section_id = file.split('.')[0]
        if section_id == 'cybro_marketing':
            section_id = 'home'
            
        # 1. Extract Navbar (only need one)
        if not navbar_html:
            nav_match = re.search(r'(<div class="nav-wrapper">.*?</nav>\s*</div>)', content, re.DOTALL)
            if nav_match:
                navbar_html = nav_match.group(1)
                
        # 2. Extract Footer (only need one)
        if not footer_html:
            foot_match = re.search(r'(<footer>.*?</footer>)', content, re.DOTALL)
            if foot_match:
                footer_html = foot_match.group(1)
                
        # 3. Extract Script (JS)
        scripts = re.findall(r'<script(?:\s+type="[^"]*")?.*?>(.*?)</script>', content, re.DOTALL)
        for js in scripts:
            # Avoid duplicating schema.org JSON-LD if we want, or just add all JS
            if 'application/ld+json' not in js and 'schema.org' not in js:
                global_js_set.add(js.strip())

        # 4. Extract Internal CSS (<style> inside <head>)
        style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
        if style_match:
            styles = style_match.group(1)
            # We want to ignore exact duplicates of the global style.css (which lead-generation, ai-automation etc often copy)
            # Heuristic: If it's over 1000 lines long, it's probably the entire style.css pasted inside.
            if len(styles.splitlines()) < 800:
                 component_css_set.add(styles.strip())

        # 5. Extract Body Content (everything between </nav> wrapper end and <footer>)
        # Find the end of nav-wrapper
        nav_end = content.find('</nav>\n    </div>')
        if nav_end != -1:
            nav_end += len('</nav>\n    </div>')
        else:
            nav_end = content.find('<div class="nav-wrapper">') # Fallback
            if nav_end != -1:
                # Need to find the closing div of nav-wrapper... this regex is safer:
                nav_match = re.search(r'<div class="nav-wrapper">.*?</nav>\s*</div>', content, re.DOTALL)
                if nav_match:
                    nav_end = nav_match.end()

        foot_start = content.find('<footer>')
        
        if nav_end != -1 and foot_start != -1:
            body_content = content[nav_end:foot_start].strip()
            sections_html.append(f'<!-- ─── {section_id.upper()} SECTION ─── -->\n<section id="{section_id}" class="page-section">\n{body_content}\n</section>\n')

# Process Navigation Links to use #Hashes instead of .html files
navbar_html = navbar_html.replace('href="cybro_marketing.html"', 'href="#home"')
navbar_html = navbar_html.replace('href="social-media.html"', 'href="#social-media"')
navbar_html = navbar_html.replace('href="lead-generation.html"', 'href="#lead-generation"')
navbar_html = navbar_html.replace('href="ai-automation.html"', 'href="#ai-automation"')
navbar_html = navbar_html.replace('href="web-development.html"', 'href="#web-development"')
navbar_html = navbar_html.replace('href="cybro_marketing.html#', 'href="#') # Clean up anchored links like #contact

footer_html = footer_html.replace('href="cybro_marketing.html"', 'href="#home"')
footer_html = footer_html.replace('href="social-media.html"', 'href="#social-media"')
footer_html = footer_html.replace('href="lead-generation.html"', 'href="#lead-generation"')
footer_html = footer_html.replace('href="ai-automation.html"', 'href="#ai-automation"')
footer_html = footer_html.replace('href="web-development.html"', 'href="#web-development"')

# Assemble
final_html = base_html.replace('__GLOBAL_CSS__', global_css)
final_html = final_html.replace('__COMPONENT_CSS__', '\n\n'.join(component_css_set))
final_html = final_html.replace('__NAVBAR__', navbar_html)
final_html = final_html.replace('__SECTIONS__', '\n'.join(sections_html))
final_html = final_html.replace('__FOOTER__', footer_html)
final_html = final_html.replace('__GLOBAL_JS__', '\n\n'.join(global_js_set))

# Basic cleanup
final_html = final_html.replace('href="cybro_marketing.html#', 'href="#')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated index.html successfully!")
