from PIL import Image, ImageDraw, ImageFont

# 1. Ajuste fino do tamanho e cor de fundo (igual à original)
width, height = 800, 900
bg_color = (11, 21, 37)
img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Cores (Do azul ao roxo)
colors = [
    (56, 189, 248), (75, 175, 245), (95, 160, 240), 
    (115, 145, 235), (135, 130, 230), (160, 115, 225)
]

# Fontes (ajuste o caminho se necessário)
font_title = ImageFont.truetype("/Library/Fonts/Arial Bold.ttf", 35)
font_sub = ImageFont.truetype("/Library/Fonts/Arial.ttf", 18)
font_mod_title = ImageFont.truetype("/Library/Fonts/Arial Bold.ttf", 22)
font_mod_text = ImageFont.truetype("/Library/Fonts/Arial.ttf", 16)

# Títulos
draw.text((400, 40), "Cloud Engineer Roadmap", fill="white", font=font_title, anchor="mm")
draw.text((400, 80), "(DevOps / SRE / Platform)", fill="white", font=font_title, anchor="mm")
draw.text((400, 120), "Roadmap de Aprendizado Prático e Evolutivo", fill="white", font=font_sub, anchor="mm")
draw.line([75, 150, 700, 150], fill=(50, 50, 60), width=2)

def draw_rounded_box(draw, x, y, w, h, radius, border_color, title, text):
    # Fundo da caixa
    draw.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=(20, 25, 40), outline=border_color, width=2)
    
    # Título do módulo agora usando a 'border_color' (a cor do degradê)
    draw.text((x + w/2, y + 25), title, fill=border_color, font=font_mod_title, anchor="mm")
    
    # Texto descritivo permanece em cinza para manter o contraste
    draw.text((x + w/2, y + 55), text, fill=(200, 200, 200), font=font_mod_text, anchor="mm")

modules = [
    ("1. FUNDAMENTOS", "Linux & Redes • Scripts & Git • Containers"),
    ("2. CLOUD", "AWS • Terraform"),
    ("3. PIPELINE", "GitHub Actions"),
    ("4. ORQUESTRAÇÃO", "Kubernetes & Helm • ArgoCD"),
    ("5. OBSERVABILIDADE", "Grafana • Prometheus • Loki • Jaeger"),
    ("6. PLATAFORMA", "Backstage")
]

# Desenho sequencial ajustado para caber no novo height
y_pos = 200
for i, (title, content) in enumerate(modules):
    draw_rounded_box(draw, 150, y_pos, 500, 80, 15, colors[i], title, content)
    
    if i < len(modules) - 1:
        # Linha centralizada em 400 (150 + 500/2)
        draw.line([400, y_pos+80, 400, y_pos+110], fill=colors[i], width=3)
    y_pos += 110

img.save("../images/cloud-eng-roadmap.png")
