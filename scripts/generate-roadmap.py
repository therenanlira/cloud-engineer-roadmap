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


width, height = 800, 900
bg_color = (11, 21, 37)
img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)

colors = [
    (56, 189, 248), (75, 175, 245), (95, 160, 240),
    (115, 145, 235), (135, 130, 230), (160, 115, 225)
]

font_title = load_font(BOLD_FONT_CANDIDATES, 35)
font_sub = load_font(REGULAR_FONT_CANDIDATES, 18)
font_mod_title = load_font(BOLD_FONT_CANDIDATES, 22)
font_mod_text = load_font(REGULAR_FONT_CANDIDATES, 16)

draw.text((400, 40), "Cloud Engineer Roadmap", fill="white", font=font_title, anchor="mm")
draw.text((400, 80), "(DevOps / SRE / Platform)", fill="white", font=font_title, anchor="mm")
draw.text((400, 120), "Roadmap de Aprendizado Prático e Evolutivo", fill="white", font=font_sub, anchor="mm")
draw.line([75, 150, 700, 150], fill=(50, 50, 60), width=2)

def draw_rounded_box(draw, x, y, w, h, radius, border_color, title, text):
    draw.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=(20, 25, 40), outline=border_color, width=2)

    draw.text((x + w/2, y + 25), title, fill=border_color, font=font_mod_title, anchor="mm")

    draw.text((x + w/2, y + 55), text, fill=(200, 200, 200), font=font_mod_text, anchor="mm")

modules = [
    ("1. FUNDAMENTOS", "Linux & Redes • Scripts & Git • Containers"),
    ("2. CLOUD", "AWS • Terraform"),
    ("3. PIPELINE", "GitHub Actions"),
    ("4. ORQUESTRAÇÃO", "Kubernetes & Helm • ArgoCD"),
    ("5. OBSERVABILIDADE", "Grafana • Prometheus • Loki • Jaeger"),
    ("6. PLATAFORMA", "Backstage")
]

y_pos = 200
for i, (title, content) in enumerate(modules):
    draw_rounded_box(draw, 150, y_pos, 500, 80, 15, colors[i], title, content)

    if i < len(modules) - 1:
        draw.line([400, y_pos+80, 400, y_pos+110], fill=colors[i], width=3)
    y_pos += 110

os.makedirs(OUTPUT_DIR, exist_ok=True)
img.save(os.path.join(OUTPUT_DIR, "cloud-eng-roadmap.png"))
