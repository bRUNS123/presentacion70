import fitz
import os

doc = fitz.open('presentacion_70_correciones.pdf')
outdir = 'pdf_pages'
os.makedirs(outdir, exist_ok=True)

for i in range(len(doc)):
    page = doc[i]
    pix = page.get_pixmap(dpi=200)
    pix.save(os.path.join(outdir, f'page_{i+1:02d}.png'))
    print(f'Saved page {i+1}/{len(doc)}')

print('Done!')
