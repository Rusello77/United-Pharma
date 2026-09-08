import os, re

dir_path = '.'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

# Pattern 1 for formatted index.html
pattern1 = re.compile(r'<li class="nav-item">\s*<a href="solutions-anaesthesia\.html" class="nav-link[^>]*>\s*Solutions <span class="chev">▾</span>\s*</a>\s*<div class="mega-menu" role="menu">.*?</div>\s*</div>\s*</li>', re.DOTALL)

# Pattern 2 for single-line HTML files
pattern2 = re.compile(r'<li class="nav-item"><a href="solutions-anaesthesia\.html" class="nav-link[^>]*>Solutions <span class="chev">▾</span></a><div class="mega-menu">.*?</div></div></li>', re.DOTALL)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Solutions <span class="chev">▾</span>' in content:
        new_content = pattern1.sub('<li class="nav-item">\n          <a href="index.html#solutions-overview" class="nav-link">Solutions</a>\n        </li>', content)
        new_content = pattern2.sub('<li class="nav-item"><a href="index.html#solutions-overview" class="nav-link">Solutions</a></li>', new_content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {file}')
        else:
            print(f'Warning: Regex failed to match in {file}')
