import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

dead_links = re.findall(r'href="#" class="cl"', html)
solution_links = re.findall(r'href="(products\.html\?solution=[^"]+)"', html)
has_search = 'id="hero-live-search"' in html

print(f"Dead solution links remaining: {len(dead_links)}")
print(f"Active solution filter links: {len(solution_links)}")
for l in solution_links:
    print(f"  - {l}")
print(f"Live search bar integrated: {has_search}")
