"""
Meril Catalogue — Inject 32 new product cards into products.html
Based on meril_catalogue.md canonical reference.
"""

# All products: (name, description)
# Category A: Surgical Staplers — solution=advanced-surgery, type=disposable
stapler_products = [
    # 1. MIRUS Powered Endocutter (Handles)
    (
        "MIRUS™ Powered Endocutter",
        "Powered endoscopic linear cutter with 60° articulation. 6-row stair-stepping staple formation for superior hemostasis. "
        "Available in 45 mm and 60 mm staple line lengths, each in Small, Medium, and Large shaft variants. "
        "Battery-powered for stable operation. Non-slip anvil technology. Safety switch prevents accidental firing."
    ),
    # 2. MIRUS Powered Endocutter Reloads
    (
        "MIRUS™ Powered Endocutter Reloads",
        "Colour-coded reloads for MIRUS Powered Endocutter. 60 mm: White (2.5 mm), Blue (3.5 mm), Gold (3.8 mm), Green (4.1 mm), Black (4.4 mm). "
        "45 mm: White (2.5 mm), Blue (3.5 mm), Green (4.1 mm). New knife blade with every reload."
    ),
    # 3. MIRUS Linear Cutter
    (
        "MIRUS™ Linear Cutter",
        "Disposable linear cutter for open surgery. Available in 60 mm, 80 mm, and 100 mm cut lengths. "
        "4 rows of titanium staples, 8 firings per device. Dual-side firing knob, push-button quick release, rear hinge alignment. "
        "Compatible with Blue (3.8 mm open / 1.5 mm close) and Green (4.8 mm open / 2.0 mm close) reloads."
    ),
    # 4. MIRUS Linear Cutter Reloads
    (
        "MIRUS™ Linear Cutter Reloads",
        "Reloads for MIRUS Linear Cutter. Available for 60/80/100 mm cutters. "
        "Blue cartridge: 3.8 mm open / 1.5 mm closed staple height. Green cartridge: 4.8 mm open / 2.0 mm closed. "
        "New knife with every reload for smooth, precise transection. Safety lock prevents firing over empty reload."
    ),
    # 5. MIRUS Circular Stapler (3-Row)
    (
        "MIRUS™ Circular Stapler (3-Row)",
        "Disposable circular stapler with 3-row design for enhanced wound security and hemostasis. "
        "For end-to-end, end-to-side, and side-to-side anastomosis. 7 sizes: 21–32 mm head diameter (12–22 mm cutting diameter). "
        "Adjustable staple height (4.5 mm open / 1.0–2.5 mm closed). CE Approved, US 510K Cleared."
    ),
    # 6. MIRUS Circular Stapler (2-Row)
    (
        "MIRUS™ Circular Stapler (2-Row)",
        "Disposable circular stapler with conventional 2-row design. "
        "5 sizes: 24–32 mm head diameter (15–22 mm cutting diameter). "
        "Adjustable staple height, visual compression gauge, white Teflon cutting washer for audible feedback. Safety lock."
    ),
    # 7. MIRUS Skin Stapler
    (
        "MIRUS™ Skin Stapler",
        "Disposable skin stapler with 35 pins for efficient wound closure. "
        "Outstanding performance across wider skin wounds. FG Code: MSSP35. 6 units per box."
    ),
    # 8. MIRUS Skin Stapler Extractors
    (
        "MIRUS™ Skin Stapler Extractors",
        "Skin staple extractor removers. Available in Metal (FG: SSEXT) and Plastic (FG: SSRM) variants. 1 unit per box."
    ),
    # 9. MIRUS Titanium U-Shape Ligation Clips
    (
        "MIRUS™ Titanium U-Shape Ligation Clips",
        "Titanium ligation clips in U-shape design. Available in Small (MLT-100), Medium (MLT-200), "
        "Medium-Large (MLT-300), and Large (MLT-400). 20 clips per box."
    ),
    # 10. MIRUS Endoscopic Clip Applicator (U-Shape)
    (
        "MIRUS™ Endoscopic Clip Applicator",
        "Laparoscopic applicators for MIRUS U-Shape Titanium Clips. "
        "Applicator 300 for Medium-Large clips (FTEA-00300). Applicator 400 for Large clips (FTEA-00400)."
    ),
    # 11. MIRUS Open Clip Applicator (U-Shape)
    (
        "MIRUS™ Open Clip Applicator (U-Shape)",
        "Open surgical applicators for MIRUS U-Shape Titanium Clips. "
        "Available for clip sizes 100/200/300/400 in lengths 15 cm, 20 cm, and 28 cm. 12 variants total."
    ),
    # 12. MIRUS Titanium V-Shape Ligation Clips
    (
        "MIRUS™ Titanium V-Shape Ligation Clips",
        "Titanium ligation clips in V-shape design. 6 sizes: Micro (VMLT-060), Small (VMLT-080), "
        "Small-Medium (VMLT-100), Medium (VMLT-200), Medium-Large (VMLT-300), Large (VMLT-400). 20 clips per box."
    ),
    # 13. V-Shape Ligation Clip Applicators
    (
        "V-Shape Ligation Clip Applicators",
        "Open applicators for MIRUS V-Shape Titanium Clips. "
        "20 cm variants for sizes 60/80/100/200/300/400. 28 cm variants for sizes 80/100/200. "
        "1 unit per box."
    ),
    # 14. MYCLIP Polymer Ligation Clips
    (
        "MYCLIP™ Polymer Ligation Clips",
        "Non-metallic polymer ligation clips. Available in Medium-Large (POLY-200), Large (POLY-300), "
        "and Extra-Large (POLY-400). 10 clips per box. MRI-safe alternative to titanium."
    ),
    # 15. MYCLIP Endoscopic Clip Applicator (Polymer)
    (
        "MYCLIP™ Endoscopic Clip Applicator",
        "Laparoscopic applicators for MYCLIP Polymer Clips. "
        "200mm for Medium-Large (PTEA-00200), 300mm for Large (PTEA-00300), 400mm for Extra-Large (PTEA-00400)."
    ),
    # 16. MYCLIP Open Applicator (Polymer)
    (
        "MYCLIP™ Open Applicator (Polymer)",
        "Open surgical applicators (30° angled) for MYCLIP Polymer Clips. "
        "200-30 DEG for ML clips, 300-30 DEG for L clips, 400-30 DEG for XL clips."
    ),
]

# Category B: Surgical Sutures — solution=advanced-surgery, type=disposable
suture_products = [
    # 17. MITSU AB
    (
        "MITSU AB™ — Polyglactin 910 with Triclosan",
        "Synthetic absorbable braided coated suture with antibacterial Triclosan coating. "
        "Inhibits suture-induced Surgical Site Infections (SSIs). Clinically proven safety and efficacy. "
        "35 SKUs across sizes 1 to 5-0. Violet and Undyed variants. Mid-term absorption."
    ),
    # 18. MITSU
    (
        "MITSU™ — Polyglactin 910",
        "Synthetic absorbable braided coated suture. Highest knot security with braided construction. "
        "63 SKUs across sizes 2 to 6-0. Multiple needle configurations: Round Body, Reverse Cutting, Taper Cut, Blunt Point, J-Type. "
        "Violet and Undyed. Includes Double Needle, Loop, and short/extra-length variants."
    ),
    # 19. MITSU CLS
    (
        "MITSU™ CLS — Polyglactin 910 Non-Needled",
        "Pre-cut non-needled synthetic absorbable braided suture (3 × 45 cm per foil). "
        "Available in sizes 0, 2-0, 3-0, and 4-0. Violet. 12 foils per box."
    ),
    # 20. MITSU C+
    (
        "MITSU C+™ — Polyglactin 910 with Chlorhexidine",
        "Synthetic absorbable braided coated suture with Chlorhexidine antibacterial coating. "
        "29 SKUs across sizes 0 to 5-0. Violet and Undyed variants. "
        "Round Body, Reverse Cutting, Taper Cut, and Cutting needle options."
    ),
    # 21. MITSU FST
    (
        "MITSU FST™ — Polyglactin 910 Fast",
        "Short-term absorbable braided coated suture. Low molecular weight Polyglactin 910 for faster absorption. "
        "All Undyed. 17 SKUs across sizes 0 to 5-0. Reverse Cutting, Taper Cut, Cutting, and Round Body needles. "
        "Includes Double Needle variants."
    ),
    # 22. MEGASORB
    (
        "MEGASORB™ — Polyglycolic Acid",
        "Synthetic absorbable braided coated suture (PGA). "
        "30 SKUs across sizes 2 to 5-0. Violet and Undyed. "
        "Includes Heavy, Double Needle (DN/DNL), and short-length variants. Round Body, Reverse Cutting, Taper Cut needles."
    ),
    # 23. MEGASORB CLS
    (
        "MEGASORB™ CLS — PGA Non-Needled",
        "Pre-cut non-needled synthetic absorbable PGA suture (180 cm per foil). "
        "Available in sizes 0 (MS2614NS) and 2-0 (MS2615NS). Violet. 12 foils per box."
    ),
    # 24. FILAXYN
    (
        "FILAXYN™ — Polydioxanone (PDS)",
        "Synthetic absorbable monofilament suture for long-term wound support. "
        "60% tensile strength retention at 28 days, complete absorption at 180–210 days. "
        "37 SKUs across sizes 1 to 7-0. Violet. Includes Loop and Double Needle variants."
    ),
    # 25. FILAPRON
    (
        "FILAPRON™ — Polyglecaprone 25",
        "Synthetic absorbable monofilament suture for scarless sub-cuticular suturing. "
        "60–90% tensile strength retention at 7 days, complete absorption at 90–110 days. "
        "18 SKUs across sizes 1-0 to 6-0. Undyed and Violet. Also available as SubK suture."
    ),
    # 26. FILAMIDE
    (
        "FILAMIDE™ — Polyamide (Nylon)",
        "Synthetic non-absorbable monofilament suture. Black. Polyamide 6-6.6. "
        "Excellent histocompatibility, smooth tissue passage, flexible and easy to handle. "
        "27 SKUs across sizes 2 to 6-0. Available with Elixir Needle for surgical precision."
    ),
    # 27. FILAMIDE Pre-Cut
    (
        "FILAMIDE™ Pre-Cut — Non-Needled",
        "Pre-cut non-needled polyamide monofilament suture (2 × 76 cm and 35 cm lengths). "
        "Available in sizes 0 to 2. Black. 6 SKUs. 12 foils per box."
    ),
    # 28. FILASILK
    (
        "FILASILK™ — Braided Silk",
        "Natural non-absorbable braided coated silk suture. Black. "
        "46 SKUs across sizes 1 to 6-0. Comprehensive needle range including Spatula Point, Taper Cut, V-Black variants. "
        "Versatile for general, cardiovascular, ophthalmic, and plastic surgery."
    ),
    # 29. FILASILK Pre-Cut
    (
        "FILASILK™ Pre-Cut — Non-Needled Silk",
        "Pre-cut non-needled braided silk suture (2 × 76 cm per foil). "
        "Available in sizes 3 to 4-0. Black. 7 SKUs. 12 foils per box."
    ),
    # 30. FILASILK Reel
    (
        "FILASILK™ Reel — Non-Sterile Silk",
        "Non-sterile braided silk reels (25 metres). "
        "Available in sizes 2, 1, 0, 2-0, and 3-0. Black. 6 reels per box."
    ),
    # 31. FILAPROP
    (
        "FILAPROP™ — Polypropylene",
        "Synthetic non-absorbable monofilament suture. Blue. "
        "26 SKUs across sizes 1 to 10-0. Known for exceptional strength and elasticity. "
        "Includes Loop, Double Needle, and short-length variants. Round Body, Cutting, Reverse Cutting, Taper Cut needles."
    ),
    # 32. MERICRON XL
    (
        "MERICRON XL™ — Braided Polyester",
        "Synthetic non-absorbable braided polyester suture. Green. "
        "5 SKUs in sizes 0, 2, and 5. 1/2 Circle Reverse Cutting and Taper Cut needles. "
        "Available in 12-foil and 6-foil boxes."
    ),
]


def make_card(name, desc, solution="advanced-surgery", brand="meril", dtype="disposable"):
    safe_name = name.replace("™", "").replace(" ", "+").replace("&", "%26").replace("—", "-")
    # Escape HTML entities in name and desc
    h3_name = name.replace("&", "&amp;")
    p_desc = desc.replace("&", "&amp;")
    return (
        f'          <div data-solution="{solution}" data-brand="{brand}" data-type="{dtype}">\r\n'
        f'            <div class="card card-product"><div class="p-meta"><span class="badge b-disposable">Disposable</span>'
        f'<span class="badge b-available">Available</span></div>'
        f'<h3>{h3_name}</h3>'
        f'<div class="b-chip" style="width:fit-content;font-size:11px;">Meril</div>'
        f'<p>{p_desc}</p>'
        f'<div class="p-actions"><a href="#" class="btn btn-outline btn-sm">View</a>'
        f'<a href="request-information.html?product={safe_name}" class="btn btn-primary btn-sm">'
        f'Request <span class="arr">\u2192</span></a></div></div>\r\n'
        f'          </div>\r\n'
    )


# Build all HTML
all_html = "\r\n          <!-- MERIL SURGICAL STAPLERS -->\r\n"
for name, desc in stapler_products:
    all_html += make_card(name, desc)

all_html += "\r\n          <!-- MERIL SURGICAL SUTURES -->\r\n"
for name, desc in suture_products:
    all_html += make_card(name, desc)

# Read products.html
with open(r'C:\Users\Eshwar\.gemini\antigravity-ide\scratch\united-pharma\products.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before the Infection Prevention section (which has existing Meril cards)
# We'll insert right before <!-- INFECTION PREVENTION -->
marker = '          <!-- INFECTION PREVENTION -->\r\n'
if marker in content:
    content = content.replace(marker, all_html + "\r\n" + marker)
    print(f"Successfully inserted 32 Meril product cards before INFECTION PREVENTION section.")
else:
    # Try without \r\n
    marker2 = '          <!-- INFECTION PREVENTION -->\n'
    if marker2 in content:
        content = content.replace(marker2, all_html + "\n" + marker2)
        print(f"Successfully inserted 32 Meril product cards (LF newlines).")
    else:
        print("ERROR: Could not find INFECTION PREVENTION marker!")
        exit(1)

with open(r'C:\Users\Eshwar\.gemini\antigravity-ide\scratch\united-pharma\products.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done. products.html updated.")
