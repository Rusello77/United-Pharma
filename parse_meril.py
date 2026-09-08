import json
import re
import os

def parse_markdown_to_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    products = []
    
    # We are looking for H2s that represent product families.
    # From the file, staplers start with "## MIRUS " or "## V Shape" or "## MYCLIP"
    # Sutures start with "## Product Family: "
    
    sections = re.split(r'\n## ', content)
    
    for section in sections[1:]: # Skip the intro
        lines = section.split('\n')
        title = lines[0].strip()
        
        # Determine if it's a product section we care about
        if not (title.startswith('MIRUS') or title.startswith('V Shape') or title.startswith('MYCLIP') or title.startswith('Product Family:')):
            continue
            
        # Clean title
        clean_title = title.replace('Product Family:', '').strip()
        
        # Generate ID
        safe_id = clean_title.lower()
        safe_id = re.sub(r'[^a-z0-9]+', '-', safe_id)
        safe_id = safe_id.strip('-')
        
        product_data = {
            "id": safe_id,
            "title": clean_title,
            "overview": [],
            "features": [],
            "specifications": [],
            "skus": [],
            "anatomy": [],
            "raw_html": "" # fallback
        }
        
        # We will parse out Overview, Features, Specs, SKUs
        current_subsection = "overview"
        table_headers = []
        
        for line in lines[1:]:
            line_stripped = line.strip()
            
            if line_stripped.startswith('### '):
                sub_title = line_stripped.replace('### ', '').strip().lower()
                if 'overview' in sub_title or 'positioning' in sub_title:
                    current_subsection = "overview"
                elif 'anatomy' in sub_title:
                    current_subsection = "anatomy"
                elif 'advantage' in sub_title or 'feature' in sub_title:
                    current_subsection = "features"
                elif 'specification' in sub_title or 'colour' in sub_title:
                    current_subsection = "specifications"
                elif 'product' in sub_title or 'ordering' in sub_title or 'individual' in sub_title:
                    current_subsection = "skus_raw"
                else:
                    current_subsection = "other"
                continue
                
            if not line_stripped:
                continue
                
            if current_subsection == "overview":
                if not line_stripped.startswith('*Source') and not line_stripped.startswith('---'):
                    product_data["overview"].append(line_stripped)
                    
            elif current_subsection == "anatomy":
                if line_stripped.startswith('- '):
                    product_data["anatomy"].append(line_stripped[2:])
                    
            elif current_subsection == "features":
                if line_stripped.startswith('- '):
                    product_data["features"].append(line_stripped[2:])
                else:
                    product_data["features"].append(line_stripped)
                    
            elif current_subsection == "specifications":
                # It could be a table or bullet points
                if line_stripped.startswith('|'):
                    # Table row
                    parts = [p.strip() for p in line_stripped.split('|')[1:-1]]
                    if set(parts) == set(['-']) or all(p.startswith('-') for p in parts):
                        pass # separator
                    elif not table_headers:
                        table_headers = parts
                    else:
                        spec_row = dict(zip(table_headers, parts))
                        product_data["specifications"].append(spec_row)
                elif line_stripped.startswith('- '):
                    product_data["specifications"].append({"Feature": line_stripped[2:]})
                    
            elif current_subsection == "skus_raw":
                if line_stripped.startswith('#### '):
                    # It's an individual product block
                    sku_name = line_stripped.replace('#### ', '').strip()
                    product_data["skus"].append({"_Name": sku_name})
                elif line_stripped.startswith('- **'):
                    if product_data["skus"]:
                        # parse key value
                        match = re.match(r'- \*\*(.*?)\*\*(.*)', line_stripped)
                        if match:
                            key = match.group(1).replace(':', '').strip()
                            val = match.group(2).replace(':', '', 1).strip()
                            product_data["skus"][-1][key] = val
                elif line_stripped.startswith('|'):
                    # SKU Table
                    parts = [p.strip() for p in line_stripped.split('|')[1:-1]]
                    if set(parts) == set(['-']) or all(p.startswith('-') for p in parts):
                        pass # separator
                    elif not table_headers:
                        table_headers = parts
                    else:
                        sku_row = dict(zip(table_headers, parts))
                        product_data["skus"].append(sku_row)

        # Cleanup
        product_data["overview"] = "\n\n".join(product_data["overview"])
        products.append(product_data)
        
    return products

if __name__ == "__main__":
    filepath = r"c:\Users\Eshwar\Downloads\meril_catalogue.md"
    parsed_data = parse_markdown_to_json(filepath)
    
    out_dir = r"C:\Users\Eshwar\.gemini\antigravity-ide\scratch\united-pharma\assets\data"
    os.makedirs(out_dir, exist_ok=True)
    
    out_file = os.path.join(out_dir, "meril-catalogue.json")
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(parsed_data, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully extracted {len(parsed_data)} product families to {out_file}")
