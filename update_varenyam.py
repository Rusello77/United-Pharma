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

critical_care_products = [
    ("COLISTIMETHATE SODIUM INJECTION", "1/2/3/4.5 MIU"),
    ("TIGECYCLINE INJECTION", "50 mg"),
    ("TEICOPLANIN INJECTION", "200/400 mg"),
    ("MEROPENEM INJECTION", "500/1000 mg"),
    ("CEFTRIAXONE INJECTION", "1 g"),
    ("VARTAZ-P", "Piperacillin 4g & Tazobactam 0.5g Inj (4.5g Vial)"),
    ("VARXON-S", "Ceftriaxone 1g & Sulbactam 0.5g Inj (1.5g Vial)"),
    ("Varpraz-S", "Cefoperazone 1g & Sulbactam 0.5g Inj (1.5g Vial)"),
    ("CLINDYM", "Clindamycin Inj 150 mg/ml (2/4 ml Amp)"),
    ("Varmox-CV", "Amoxycillin & Potassium Clavulanate Inj 1.2g (1.2g Vial)"),
    ("D-CYCLINE", "Doxycycline Inj 100 mg (100 mg Vial)"),
    ("PENTOVAR", "Pantoprazole Inj 40 mg (40 mg Vial)"),
    ("HEPARIN SODIUM INJECTION", "1000/5000 IU/ml"),
    ("ENOXAPARIN SODIUM INJECTION", "40/60 mg"),
    ("N-ACETYL CYSTEINE INJECTION", "200 mg/ml"),
    ("CALCIUM GLUCONATE & CALCIUM LACTOBIONATE INJECTION", "Critical Care Range"),
    ("SODIUM BICARBONATE INJECTION", "8.4% w/v"),
    ("POTASSIUM CHLORIDE INJECTION", "150 mg/ml (10 ml Amp)"),
    ("Glycipresin", "Terlipressin Acetate Inj 1mg/10ml (10 ml Amp)"),
    ("Labelbloc", "Labetalol Hydrochloride Inj 5mg/ml (4 ml Amp)"),
    ("VARCLOT", "Tranexamic Acid Inj 100mg/ml (5 ml Amp)"),
    ("VARDOL", "Tramadol Hydrochloride Inj 50mg/ml (1/2 ml Amp)"),
    ("SUFFICORT", "Hydrocortisone Sodium Succinate Inj 100mg (100mg Vial)"),
    ("VARPRED-S", "Methyl Prednisolone Sodium Succinate Inj 500mg/1g (Vial)"),
]

def generate_html(products, solution):
    html = ""
    for name, desc in products:
        safe_name = name.replace(' ', '+').replace('&', '%26')
        html += f'''          <div data-solution="{solution}" data-brand="varenyam" data-type="drug">
            <div class="card card-product"><div class="p-meta"><span class="badge b-drug">Drug</span><span class="badge b-available">Available</span><span class="badge b-hcp">HCP Only</span></div><h3>{name}</h3><div class="b-chip" style="width:fit-content;font-size:11px;">Varenyam / Nidrava</div><p>{desc}</p><div class="p-actions"><a href="#" class="btn btn-outline btn-sm">View</a><a href="request-information.html?product={safe_name}" class="btn btn-primary btn-sm">Request <span class="arr">→</span></a></div></div>
          </div>\n'''
    return html

anaesthesia_html = generate_html(anaesthesia_products, "anaesthesia")
critical_care_html = generate_html(critical_care_products, "critical-care")

with open('C:\\Users\\Eshwar\\.gemini\\antigravity-ide\\scratch\\united-pharma\\products.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Anaesthesia placeholders (lines 118-129 approximately)
# Looking for:
#           <div data-solution="anaesthesia" data-brand="varenyam" data-type="drug">
# ...
#           <div data-solution="anaesthesia" data-brand="varenyam" data-type="drug">
# ...
#           <div data-solution="anaesthesia" data-brand="varenyam" data-type="drug">
# ... </div>\n          </div>\n
placeholder_regex = r'(          <div data-solution="anaesthesia" data-brand="varenyam" data-type="drug">.*?</div>\n          </div>\n){3}'

if re.search(placeholder_regex, content, re.DOTALL):
    content = re.sub(placeholder_regex, anaesthesia_html, content, count=1, flags=re.DOTALL)
else:
    print("Could not find Anaesthesia placeholders!")

# Insert Critical Care products right under the <!-- CRITICAL CARE --> comment
cc_marker = '          <!-- CRITICAL CARE -->\n'
if cc_marker in content:
    content = content.replace(cc_marker, cc_marker + critical_care_html)
else:
    print("Could not find Critical Care marker!")

with open('C:\\Users\\Eshwar\\.gemini\\antigravity-ide\\scratch\\united-pharma\\products.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated products.html")
