with open('products.html', 'r', encoding='utf-8') as f:
    c = f.read()

total = c.count('data-brand="meril"')
adv = c.count('data-solution="advanced-surgery" data-brand="meril"')
uro = c.count('data-solution="urology" data-brand="meril"')
inf = c.count('data-solution="infection-prevention" data-brand="meril"')

print(f"Total Meril cards: {total}")
print(f"  Advanced Surgery: {adv}")
print(f"  Urology: {uro}")
print(f"  Infection Prevention: {inf}")
print(f"  Sum check: {adv + uro + inf} (should be {total})")
