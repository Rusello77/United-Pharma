import os
from PIL import Image, ImageChops

def trim_white(im, threshold=245):
    # Convert to RGB if RGBA/L
    bg = Image.new("RGB", im.size, (255, 255, 255))
    if im.mode == 'RGBA':
        bg.paste(im, mask=im.split()[3])
    else:
        bg.paste(im)
    
    diff = ImageChops.difference(bg, Image.new("RGB", im.size, (255, 255, 255)))
    bbox = diff.getbbox()
    if bbox:
        # add 15px padding around bounding box
        left = max(0, bbox[0] - 15)
        top = max(0, bbox[1] - 15)
        right = min(im.size[0], bbox[2] + 15)
        bottom = min(im.size[1], bbox[3] + 15)
        return im.crop((left, top, right, bottom))
    return im

brain_dir = r'C:\Users\Eshwar\.gemini\antigravity-ide\brain\d3389e79-39c5-475f-9eea-767ddf8e2421'

# 1. Baxter & Hillrom (media__1787294465823.jpg)
img_b_h = Image.open(os.path.join(brain_dir, 'media__1787294465823.jpg'))
w, h = img_b_h.size

# Baxter crop (top half)
baxter_raw = img_b_h.crop((int(w*0.20), int(h*0.20), int(w*0.80), int(h*0.48)))
baxter_trimmed = trim_white(baxter_raw)
baxter_trimmed.save('assets/images/brands/baxter.png')

# Hillrom crop (bottom half)
hillrom_raw = img_b_h.crop((int(w*0.20), int(h*0.45), int(w*0.80), int(h*0.82)))
hillrom_trimmed = trim_white(hillrom_raw)
hillrom_trimmed.save('assets/images/brands/hillrom.png')

# 2. Lyvex (media__1787294465979.jpg)
lyvex_raw = Image.open(os.path.join(brain_dir, 'media__1787294465979.jpg'))
lyvex_trimmed = trim_white(lyvex_raw)
lyvex_trimmed.save('assets/images/brands/lyvex.png')

# 3. Lenvitz (media__1787294466098.png)
lenvitz_raw = Image.open(os.path.join(brain_dir, 'media__1787294466098.png'))
lenvitz_trimmed = trim_white(lenvitz_raw)
lenvitz_trimmed.save('assets/images/brands/lenvitz.png')

# 4. Varenyam (media__1787294466132.jpg)
varenyam_raw = Image.open(os.path.join(brain_dir, 'media__1787294466132.jpg'))
varenyam_trimmed = trim_white(varenyam_raw)
varenyam_trimmed.save('assets/images/brands/varenyam.png')

# 5. Meril (media__1787294466151.jpg)
meril_raw = Image.open(os.path.join(brain_dir, 'media__1787294466151.jpg'))
meril_trimmed = trim_white(meril_raw)
meril_trimmed.save('assets/images/brands/meril.png')

print("Trimmed and saved all 6 brand logos successfully!")
