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

RESAMPLE = getattr(Image, "Resampling", Image).LANCZOS


def load_font(candidates, size):
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


# Mesma paleta de --bg-color, --accent-blue e --muted-text do docs/assets/css/style.css.
# Sem o título "Cloud Engineer Roadmap": ele já aparece no H1 do README logo acima
# e na imagem do roadmap logo abaixo, então aqui o destaque fica só para o CTA.
width, height = 1000, 160
bg_color = (11, 21, 37)
accent_blue = (56, 189, 248)
muted_text = (148, 163, 184)

# Desenha em escala maior (supersampling) num canvas transparente e reduz no
# final. Assim os cantos fora do botão arredondado ficam transparentes (em vez
# do quadrado da cor de fundo) e a borda arredondada continua lisa, sem
# serrilhado, mesmo sem antialiasing nativo no rounded_rectangle do Pillow.
scale = 4
big = Image.new("RGBA", (width * scale, height * scale), (0, 0, 0, 0))
draw = ImageDraw.Draw(big)

border_margin = 6 * scale
draw.rounded_rectangle(
    [border_margin, border_margin, width * scale - border_margin, height * scale - border_margin],
    radius=24 * scale,
    fill=(20, 25, 40, 255),
    outline=accent_blue + (255,),
    width=3 * scale,
)

font_cta = load_font(BOLD_FONT_CANDIDATES, 40 * scale)
font_tagline = load_font(REGULAR_FONT_CANDIDATES, 18 * scale)

center_x = (width * scale) / 2
draw.text((center_x, 55 * scale), "Guia de estudos gratuito e em português", fill=muted_text, font=font_tagline, anchor="mm")
draw.text((center_x, 105 * scale), "Acesse o site →", fill=accent_blue, font=font_cta, anchor="mm")

img = big.resize((width, height), RESAMPLE)

os.makedirs(OUTPUT_DIR, exist_ok=True)
img.save(os.path.join(OUTPUT_DIR, "cta-banner.png"))
