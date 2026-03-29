import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

mapping = {}
current_module = "General"

text = text.replace('\n', ' ')
matches = re.finditer(r'<div class="modulo-header">(.*?)</div>|<div class="agenda-item([^"]*?)"[^>]*>.*?<span class="charla">(.*?)</span>', text)
for m in matches:
    if m.group(1):
        current_module = m.group(1).strip()
    elif m.group(3) and 'comida' not in (m.group(2) or ''):
        charla = m.group(3).strip()
        chk = charla.lower()
        if not chk.startswith(('registro', 'inaugura', 'clausura', 'palabras de bienvenida', 'transici', '🎖')):
            mapping[charla] = current_module

print(json.dumps(mapping, indent=2, ensure_ascii=False))
