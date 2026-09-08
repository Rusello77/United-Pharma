import json
import urllib.parse

# 1. Load Spyrox products from products-catalogue.json
with open('assets/data/products-catalogue.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

spyrox_prods = [p for p in products if p.get('brandSlug') == 'spyrox']

cards_html = []
for p in spyrox_prods:
    h3 = p['title']
    p_id = p['id']
    overview = p['overview'][:110] + '...'
    req_param = urllib.parse.quote_plus(h3)
    card = f'''          <div data-solution="orthopaedics" data-brand="spyrox" data-type="implant">
            <div class="card card-product"><div class="p-meta"><span class="badge b-implant">Implant</span><span class="badge b-available">Available</span></div><h3>{h3}</h3><div class="b-chip" style="width:fit-content;font-size:11px;">Spyrox (Sorath Ortho)</div><p>{overview}</p><div class="p-actions"><a href="product-detail.html?id={p_id}" class="btn btn-outline btn-sm">View</a><a href="request-information.html?product={req_param}" class="btn btn-primary btn-sm">Request <span class="arr">→</span></a></div></div>
          </div>'''
    cards_html.append(card)

cards_block = '\n'.join(cards_html)

# 2. Update products.html
with open('products.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add filter checkbox
if 'id="f-spyrox"' not in html:
    html = html.replace('<label class="filter-opt"><input type="checkbox" data-group="brand" value="curotherm" id="f-curotherm"> Curotherm</label>',
                        '<label class="filter-opt"><input type="checkbox" data-group="brand" value="spyrox" id="f-spyrox"> Spyrox (Sorath Ortho)</label>\n            <label class="filter-opt"><input type="checkbox" data-group="brand" value="curotherm" id="f-curotherm"> Curotherm</label>')

# Insert cards before Urology
target_marker = '<!-- UROLOGY -->'
if target_marker in html and 'data-brand="spyrox"' not in html:
    html = html.replace(target_marker, f'<!-- SPYROX IMPLANTS -->\n{cards_block}\n\n          {target_marker}')

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Updated products.html with {len(cards_html)} Spyrox product cards!")

# 3. Update partner-brands.html
with open('partner-brands.html', 'r', encoding='utf-8') as f:
    brands_html = f.read()

spyrox_brand_card = '''      <!-- Spyrox -->
      <div class="card card-brand" id="brand-card-spyrox">
        <div class="brand-logo-box">SPYROX</div>
        <h3>Spyrox (Sorath Ortho / Sigma Surgical)</h3>
        <p>Next-generation Veriaxial Locking System engineered for reliable fixation across complex fracture patterns. Features variable angle locking technology (+/- 18° off-axis angulation), anatomical contouring, and a unique color-coded interface (Right/Left borders, 2.7mm Blue, 3.5mm Pink, 5.0mm Green screws).</p>
        <div class="brand-chips" style="justify-content:center;">
          <span class="b-chip-sm">Orthopaedics</span>
          <span class="b-chip-sm">Implants</span>
        </div>
        <a href="products.html?brand=spyrox" class="btn btn-outline btn-sm btn-full" style="margin-top:auto;" id="spyrox-products-link">View Spyrox products <span class="arr">→</span></a>
      </div>'''

if 'id="brand-card-spyrox"' not in brands_html:
    # Insert after DePuy card
    depuy_end_marker = '<!-- Takeda -->'
    if depuy_end_marker in brands_html:
        brands_html = brands_html.replace(depuy_end_marker, f'{spyrox_brand_card}\n\n      {depuy_end_marker}')
        # Update partner count text from 9 Confirmed Partners to 10 Confirmed Partners
        brands_html = brands_html.replace('9 Confirmed Partners', '10 Confirmed Partners')
        with open('partner-brands.html', 'w', encoding='utf-8') as f:
            f.write(brands_html)
        print("Updated partner-brands.html with Spyrox brand card!")
