import fitz
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

doc = fitz.open('presentacion_70_correciones.pdf')
print(f'Total pages: {len(doc)}')
for i in range(len(doc)):
    text = doc[i].get_text()
    print(f'\n=== PAGE {i+1} ===')
    print(text)
