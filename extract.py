import re

with open('products.html', 'r', encoding='utf-8') as f:
    html = f.read()

cards = re.findall(r'<div data-solution=".*?" data-brand="(baxter|takeda|lenvitz|lyvex)".*?>.*?<h3>(.*?)</h3>.*?<p>(.*?)</p>', html, re.DOTALL)

for b, t, d in cards:
    print(f'{b.upper()}: {t} - {d}')
