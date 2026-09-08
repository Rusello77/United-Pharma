import json
import re

with open('assets/data/meril-catalogue.json', 'r', encoding='utf-8') as f:
    meril_data = json.load(f)

with open('products.html', 'r', encoding='utf-8') as f:
    html = f.read()

# For every Meril card, we have <div data-brand="meril".*?<h3>(.*?)</h3>
def replacer(match):
    full_card = match.group(0)
    # Find h3 title
    h3_match = re.search(r'<h3>(.*?)</h3>', full_card)
    if not h3_match:
        return full_card
        
    h3_title = h3_match.group(1).replace('amp;', '').replace('&', '').strip()
    
    best_id = ""
    # Try to find a match in json
    # e.g. "MIRUS™ Powered Endocutter" vs "MIRUS Powered Endocutter (Powered Endoscopic Linear Cutter with Reloads)"
    h3_clean = h3_title.replace('™', '').lower()
    
    for item in meril_data:
        t_clean = item['title'].lower()
        if h3_clean in t_clean or t_clean in h3_clean or h3_clean.split('—')[0].strip() in t_clean:
            best_id = item['id']
            break
            
    # Some specific fallbacks
    if "endocutter reloads" in h3_clean:
        best_id = "mirus-powered-endocutter-reloads"
    elif "linear cutter reloads" in h3_clean:
        best_id = "mirus-linear-cutter-reloads"
    elif "3-row" in h3_clean:
        best_id = "mirus-circular-stapler"
    elif "2-row" in h3_clean:
        best_id = "mirus-circular-stapler"
    elif "skin stapler extractor" in h3_clean:
        best_id = "mirus-skin-stapler-extractors"
    elif "skin stapler" in h3_clean:
        best_id = "mirus-skin-stapler"
    elif "open clip applicator (u-shape)" in h3_clean:
        best_id = "mirus-open-clip-applicator-for-u-shape-titanium-clips"
    elif "v-shape ligation clip applicators" in h3_clean:
        best_id = "mirus-v-shape-ligation-clip-applicators"
    elif "open applicator (polymer)" in h3_clean:
        best_id = "myclip-open-applicator-for-polymer-clips"
    elif "mitsu c+" in h3_clean:
        best_id = "product-family-mitsu-c"
    elif "mitsu cls" in h3_clean:
        best_id = "product-family-mitsu-cls"
    elif "mitsu fst" in h3_clean:
        best_id = "product-family-mitsu-fst"
    elif "mitsu ab" in h3_clean:
        best_id = "product-family-mitsu-ab"
    elif "mitsu" in h3_clean:
        best_id = "product-family-mitsu"
    elif "megasorb cls" in h3_clean:
        best_id = "product-family-megasorb-cls"
    elif "megasorb" in h3_clean:
        best_id = "product-family-megasorb"
    elif "filaxyn" in h3_clean:
        best_id = "product-family-filaxyn"
    elif "filapron" in h3_clean:
        best_id = "product-family-filapron"
    elif "filamide pre-cut" in h3_clean:
        best_id = "product-family-filamide-pre-cut"
    elif "filamide" in h3_clean:
        best_id = "product-family-filamide"
    elif "filasilk pre-cut" in h3_clean:
        best_id = "product-family-filasilk-pre-cut"
    elif "filasilk reel" in h3_clean:
        best_id = "product-family-filasilk-reel"
    elif "filasilk" in h3_clean:
        best_id = "product-family-filasilk"
    elif "filaprop" in h3_clean:
        best_id = "product-family-filaprop"
    elif "mericron xl" in h3_clean:
        best_id = "product-family-mericron-xl"

    if best_id:
        # replace any href="#" or href="product-detail.html?id=..." with the correct one
        full_card = re.sub(r'href="[^"]*" class="btn btn-outline btn-sm">View(?: details)?', 
                           f'href="product-detail.html?id={best_id}" class="btn btn-outline btn-sm">View details', 
                           full_card)
                           
    return full_card

# Regex to match the entire card div
new_html = re.sub(r'<div class="card card-product">.*?</div></div>', replacer, html, flags=re.DOTALL)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Pass 2 links updated.")
