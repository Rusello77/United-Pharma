import json
import re

with open('assets/data/meril-catalogue.json', 'r', encoding='utf-8') as f:
    meril_data = json.load(f)

with open('products.html', 'r', encoding='utf-8') as f:
    html = f.read()

# For each product in the JSON, find the corresponding card in products.html
# and update the <a href="#">View</a> to <a href="product-detail.html?id={id}">View range</a>

for item in meril_data:
    pid = item['id']
    # The title in HTML is often matching the name we generated
    # The card has <h3 class="card-title"> or just <h3>
    
    # We can search for the <h3>{name}</h3> inside the HTML
    # and then the nearest <a href="#"...
    
    # Let's find the exact H3 text.
    # We know the inject_meril.py script created them like:
    # <h3>{h3_name}</h3>
    h3_name = item['title'].replace("&", "&amp;").replace("™", "")
    
    # But wait, in the inject_meril.py script, the h3_name was derived from the python list, not the json.
    # Let's just find <div data-brand="meril".*?</div></div>
    pass

# A simpler approach: use regex to replace all `href="#" class="btn btn-outline btn-sm">View` 
# specifically in Meril cards, by mapping the product name in `request-information.html?product=XYZ`
def replacer(match):
    full_card = match.group(0)
    # find product name from request link
    req_match = re.search(r'request-information\.html\?product=([^"]+)', full_card)
    if req_match:
        prod_param = req_match.group(1).replace('+', ' ').replace('%26', '&')
        # match this prod_param to our JSON
        best_id = ""
        # normalize
        p_norm = prod_param.lower().replace('mirus', '').replace('mitsu', '').replace('megasorb', '').strip()
        for item in meril_data:
            t_norm = item['title'].lower()
            if p_norm in t_norm or t_norm in p_norm:
                best_id = item['id']
                break
        
        # Special cases or exact matches
        for item in meril_data:
            # check if title starts with the prod_param
            if item['title'].lower().startswith(prod_param.lower()):
                best_id = item['id']
                break
                
        if best_id:
            # Replace the href="#" with href="product-detail.html?id=..."
            new_card = re.sub(r'href="#"', f'href="product-detail.html?id={best_id}"', full_card, count=1)
            # Also change View to View details
            new_card = re.sub(r'>View<', '>View details<', new_card, count=1)
            return new_card
            
    return full_card

new_html = re.sub(r'<div data-solution="[^"]+" data-brand="meril".*?</div></div>\s*</div>', replacer, html, flags=re.DOTALL)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("products.html updated with dynamic View links.")
