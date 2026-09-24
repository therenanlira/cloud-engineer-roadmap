import os
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "docs", "assets", "img")

BOLD_FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",  # macOS
    "/Library/Fonts/Arial Bold.ttf",  # macOS (legacy)
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",  # Linux
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
    "C:\\Windows\\Fonts\\arialbd.ttf",  # Windows
]

REGULAR_FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",  # macOS
    "/Library/Fonts/Arial.ttf",  # macOS (legacy)
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",  # Linux
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
    "C:\\Windows\\Fonts\\arial.ttf",  # Windows
]


def load_font(candidates, size):
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


# 1200x630 é o tamanho recomendado para prévias de link (Open Graph). Sem cantos
# transparentes: alguns apps (ex: WhatsApp) pintam a transparência de preto.
width, height = 1200, 630
bg_color = (11, 21, 37)
accent_blue = (56, 189, 248)
muted_text = (148, 163, 184)
colors = [
    (56, 189, 248), (75, 175, 245), (95, 160, 240),
    (115, 145, 235), (135, 130, 230), (160, 115, 225)
]

img = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(img)

font_title = load_font(BOLD_FONT_CANDIDATES, 76)
font_sub = load_font(REGULAR_FONT_CANDIDATES, 34)
font_tag = load_font(BOLD_FONT_CANDIDATES, 30)
font_chip = load_font(BOLD_FONT_CANDIDATES, 19)
font_url = load_font(REGULAR_FONT_CANDIDATES, 24)

margin = 80
draw.text((margin, 120), "Cloud Engineer Roadmap", fill="white", font=font_title)
draw.text((margin, 225), "Guia de estudos gratuito e em português", fill=muted_text, font=font_sub)
draw.text((margin, 285), "DevOps  ·  SRE  ·  Platform Engineering", fill=accent_blue, font=font_tag)

modules = ["Fundamentos", "Cloud", "Pipeline", "Orquestração", "Observabilidade", "Plataforma"]
gap = 14
chip_w = (width - 2 * margin - gap * (len(modules) - 1)) / len(modules)
chip_y, chip_h = 400, 64
for i, name in enumerate(modules):
    x = margin + i * (chip_w + gap)
    draw.rounded_rectangle([x, chip_y, x + chip_w, chip_y + chip_h], radius=14, fill=(20, 25, 40), outline=colors[i], width=3)
    draw.text((x + chip_w / 2, chip_y + chip_h / 2), name, fill="white", font=font_chip, anchor="mm")

draw.text((margin, 540), "therenanlira.github.io/cloud-engineer-roadmap", fill=muted_text, font=font_url)

os.makedirs(OUTPUT_DIR, exist_ok=True)
img.save(os.path.join(OUTPUT_DIR, "og-image.png"))
