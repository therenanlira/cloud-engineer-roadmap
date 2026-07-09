from PIL import Image, ImageDraw, ImageFont
import os

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


# Configurações de cores (do seu script original)
colors = [
    (56, 189, 248), (75, 175, 245), (95, 160, 240),
    (115, 145, 235), (135, 130, 230), (160, 115, 225)
]

def criar_card(index, titulo, subtitulo):
    width, height = 600, 150 # Formato retangular de botão
    img = Image.new('RGB', (width, height), (20, 25, 40))
    draw = ImageDraw.Draw(img)

    # Borda colorida
    color = colors[index]
    draw.rounded_rectangle([0, 0, width, height], radius=15, outline=color, width=3)

    # Textos
    font_title = load_font(BOLD_FONT_CANDIDATES, 30)
    font_sub = load_font(REGULAR_FONT_CANDIDATES, 18)

    draw.text((width/2, 60), titulo, fill=color, font=font_title, anchor="mm")
    draw.text((width/2, 100), subtitulo, fill=(200, 200, 200), font=font_sub, anchor="mm")

    img.save(os.path.join(OUTPUT_DIR, f"card_{index+1}.png"))

modules = [
    ("1. FUNDAMENTOS", "Linux, Redes, Git, Containers"),
    ("2. CLOUD", "AWS, Terraform"),
    ("3. PIPELINE", "GitHub Actions"),
    ("4. ORQUESTRAÇÃO", "Kubernetes, Helm, ArgoCD"),
    ("5. OBSERVABILIDADE", "Grafana, Prometheus, Loki, Jaeger"),
    ("6. PLATAFORMA", "Backstage")
]

os.makedirs(OUTPUT_DIR, exist_ok=True)
for i, (t, s) in enumerate(modules): criar_card(i, t, s)
