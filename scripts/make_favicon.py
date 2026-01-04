from PIL import Image
import os

src = 'assets/img/icons/medicoIcon.png'
out = 'favicon.ico'  # will be created in atrio/

if not os.path.exists(src):
    raise SystemExit(f"Fuente no encontrada: {src}")

img = Image.open(src).convert('RGBA')
# Make square canvas to avoid distortion
max_side = max(img.size)
square = Image.new('RGBA', (max_side, max_side), (0,0,0,0))
square.paste(img, ((max_side - img.width)//2, (max_side - img.height)//2), img)

sizes = [(16,16),(32,32),(48,48),(64,64),(128,128)]
square.save(out, format='ICO', sizes=sizes)

print('Creado:', os.path.abspath(out))
print('Tamaños incluidos:', sizes)
