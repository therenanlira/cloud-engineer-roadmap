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


width, height = 800, 975
bg_color = (11, 21, 37)
img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)

colors = [
    (56, 189, 248), (75, 175, 245), (95, 160, 240),
    (115, 145, 235), (135, 130, 230), (160, 115, 225)
]

font_title = load_font(BOLD_FONT_CANDIDATES, 38)
font_sub = load_font(REGULAR_FONT_CANDIDATES, 18)
font_mod_index = load_font(BOLD_FONT_CANDIDATES, 14)
font_mod_title = load_font(BOLD_FONT_CANDIDATES, 24)
font_mod_text = load_font(REGULAR_FONT_CANDIDATES, 15)

draw.text((400, 45), "Cloud Engineer Roadmap", fill="white", font=font_title, anchor="mm")
draw.text((400, 85), "Guia de estudos gratuito e em português", fill=(200, 200, 200), font=font_sub, anchor="mm")
draw.line([75, 115, 700, 115], fill=(50, 50, 60), width=2)

def draw_rounded_box(draw, x, y, w, h, radius, border_color, index_label, title, text):
    draw.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=(20, 25, 40), outline=border_color, width=3)

    draw.text((x + w/2, y + 26), index_label, fill=border_color, font=font_mod_index, anchor="mm")

    draw.text((x + w/2, y + 57), title, fill="white", font=font_mod_title, anchor="mm")

    draw.text((x + w/2, y + 87), text, fill=(180, 185, 195), font=font_mod_text, anchor="mm")

modules = [
    ("Módulo 1", "Fundamentos", "Linux, Redes, Scripts, Git, Containers"),
    ("Módulo 2", "Cloud", "AWS, Terraform, FinOps"),
    ("Módulo 3", "Pipeline", "GitHub Actions"),
    ("Módulo 4", "Orquestração", "Kubernetes, Helm, ArgoCD"),
    ("Módulo 5", "Observabilidade", "Grafana, Prometheus, Loki, Jaeger"),
    ("Módulo 6", "Plataforma", "Backstage")
]

y_pos = 160
for i, (index_label, title, content) in enumerate(modules):
    draw_rounded_box(draw, 150, y_pos, 500, 114, 15, colors[i], index_label, title, content)

    if i < len(modules) - 1:
        draw.line([400, y_pos+114, 400, y_pos+134], fill=colors[i], width=3)
    y_pos += 134

os.makedirs(OUTPUT_DIR, exist_ok=True)
img.save(os.path.join(OUTPUT_DIR, "cloud-eng-roadmap.png"))
