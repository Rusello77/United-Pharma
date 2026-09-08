import re

anaesthesia_products = [
    ("LEVO-BUPIFIX", "20 ml Vial"),
    ("BUPIFIX-H", "Regional / Local Anaesthetic"),
    ("BUPIFIX", "Regional / Local Anaesthetic"),
    ("ROPIFIX", "Regional / Local Anaesthetic"),
    ("Lidofix ADR", "Regional / Local Anaesthetic"),
    ("Lidofix Gel", "Regional / Local Anaesthetic"),
    ("Lidofix", "Lignocaine Hydrochloride Inj 2% w/v (30 ml Vial)"),
    ("ATRABLOC", "Atracurium Besylate Inj 2 mg/ml (1 ml Amp)"),
    ("CIS-ATRABLOC", "Cis-Atracurium Besylate Inj 2 mg/ml"),
    ("RocuroFix", "Rocuronium Bromide Inj 10 mg/ml (5/10 ml Vial)"),
    ("VecuroFix", "Vecuronium Bromide Inj 4 mg/10 mg (Vial)"),
    ("VARPRESS", "Vasopressin Inj IP 20 units/ml (1 ml Amp)"),
    ("TERMIVA", "Terlipressin Acetate Inj IP 1 mg (10 ml Vial)"),
    ("Ephinor", "Noradrenaline Inj IP 2 mg/ml (2 ml Amp)"),
    ("REMISHOT", "Remifentanil Hydrochloride Inj 1 mg/2 mg (Vial)"),
    ("Opifent", "Fentanyl Citrate Inj 50 mcg/ml (2/10 ml Amp)"),
    ("VARPHIN", "Nalbuphine Hydrochloride Inj 10 mg/ml (1 ml Amp)"),
    ("VARMOL", "Paracetamol Inj (100 ml Bottle)"),
    ("Zocifix", "Pentazocine Lactate Inj 30 mg/ml (1 ml Amp)"),
    ("Sugimdex", "Sugammadex Inj 100 mg/ml (2/5 ml Vial)"),
    ("Varcolate-Neo", "Glycopyrrolate 0.5 mg & Neostigmine 2.5 mg (5 ml Amp)"),
    ("Medetofix", "Dexmedetomidine Hydrochloride Inj USP 100 mcg/ml (0.5/1/2 ml Amp)"),
    ("Midfix", "Midazolam Inj IP 1 mg/ml (5/10 ml Vial)"),
    ("Indifol", "Propofol Inj IP 1% (10/20/50 ml Vial)"),
    ("Qualket", "Ketamine Hydrochloride Inj 50 mg/ml (10 ml Vial)"),
    ("Varcolate", "Glycopyrrolate Inj IP 0.2 mg/ml (1 ml Amp)"),
    ("SEVOVAR", "Sevoflurane Liquid for Inhalation IP (50/250 ml Bottle)"),
    ("SEVOFLURANE (YARCOLATE)", "Liquid for Inhalation IP (50/250 ml Bottle)"),
]

def generate_html(products, solution):
    html = ""
    for name, desc in products:
        safe_name = name.replace(' ', '+').replace('&', '%26')
        html += f'''          <div data-solution="{solution}" data-brand="varenyam" data-type="drug">\n            <div class="card card-product"><div class="p-meta"><span class="badge b-drug">Drug</span><span class="badge b-available">Available</span><span class="badge b-hcp">HCP Only</span></div><h3>{name}</h3><div class="b-chip" style="width:fit-content;font-size:11px;">Varenyam / Nidrava</div><p>{desc}</p><div class="p-actions"><a href="#" class="btn btn-outline btn-sm">View</a><a href="request-information.html?product={safe_name}" class="btn btn-primary btn-sm">Request <span class="arr">→</span></a></div></div>\n          </div>\n\n'''
    return html

anaesthesia_html = generate_html(anaesthesia_products, "anaesthesia")

with open('C:\\Users\\Eshwar\\.gemini\\antigravity-ide\\scratch\\united-pharma\\products.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """          <div data-solution="anaesthesia" data-brand="varenyam" data-type="drug">
            <div class="card card-product"><div class="p-meta"><span class="badge b-drug">Drug</span><span class="badge b-available">Available</span><span class="badge b-hcp">HCP Only</span></div><h3>SevoVar (Sevoflurane)</h3><div class="b-chip" style="width:fit-content;font-size:11px;">Varenyam / Nidrava</div><p>Volatile inhalational anaesthetic for induction and maintenance of general anaesthesia.</p><div class="p-actions"><a href="#" class="btn btn-outline btn-sm">View</a><a href="request-information.html?product=SevoVar" class="btn btn-primary btn-sm">Request <span class="arr">→</span></a></div></div>
          </div>

          <div data-solution="anaesthesia" data-brand="varenyam" data-type="drug">
            <div class="card card-product"><div class="p-meta"><span class="badge b-drug">Drug</span><span class="badge b-available">Available</span><span class="badge b-hcp">HCP Only</span></div><h3>Regional &amp; Local Anaesthetics</h3><div class="b-chip" style="width:fit-content;font-size:11px;">Varenyam / Nidrava</div><p>Full range for neuraxial, peripheral nerve block and infiltration techniques.</p><div class="p-actions"><a href="#" class="btn btn-outline btn-sm">View</a><a href="request-information.html?product=Regional+%26+Local+Anaesthetics" class="btn btn-primary btn-sm">Request <span class="arr">→</span></a></div></div>
          </div>

          <div data-solution="anaesthesia" data-brand="varenyam" data-type="drug">
            <div class="card card-product"><div class="p-meta"><span class="badge b-drug">Drug</span><span class="badge b-available">Available</span><span class="badge b-hcp">HCP Only</span></div><h3>Muscle Relaxants</h3><div class="b-chip" style="width:fit-content;font-size:11px;">Varenyam / Nidrava</div><p>Neuromuscular blocking agents for intubation and surgical relaxation.</p><div class="p-actions"><a href="#" class="btn btn-outline btn-sm">View</a><a href="request-information.html?product=Muscle+Relaxants" class="btn btn-primary btn-sm">Request <span class="arr">→</span></a></div></div>
          </div>"""

if target in content:
    content = content.replace(target, anaesthesia_html)
    with open('C:\\Users\\Eshwar\\.gemini\\antigravity-ide\\scratch\\united-pharma\\products.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced placeholders.")
else:
    # Try normalizing newlines
    content_norm = content.replace('\\r\\n', '\\n')
    target_norm = target.replace('\\r\\n', '\\n')
    if target_norm in content_norm:
        content_norm = content_norm.replace(target_norm, anaesthesia_html)
        with open('C:\\Users\\Eshwar\\.gemini\\antigravity-ide\\scratch\\united-pharma\\products.html', 'w', encoding='utf-8') as f:
            f.write(content_norm)
        print("Successfully replaced placeholders with normalized newlines.")
    else:
        print("Could not find exact target string in file.")
