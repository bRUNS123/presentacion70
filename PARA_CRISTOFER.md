# Para Cristofer — continuación de la presentación (Examen de Título)

Hola Cristofer 👋

Dejé la presentación en su **versión final del Examen de Título** y sincronizada en GitHub
(`bRUNS123/presentacion70`, rama `main`). Acá te dejo el estado y lo que queda para que puedas
seguir.

## Archivo de la presentación
- Fuente: `presentacion70/ArchivoLatex/Presentacion_70_Reordenado.tex`
- Compilado: `presentacion70/ArchivoLatex/Presentacion_70_Reordenado.pdf` (60 páginas)
- Para compilar: `pdflatex` **dos veces** (por TOC / contador de páginas).
- Figuras de espectros generadas con scripts Python (matplotlib) en `ArchivoLatex/`:
  `gen_espectros_2003.py`, `gen_espectros_2025.py`, `gen_espectros_comp.py`.

## Qué quedó actualizado
- Título → "Examen de Título"; fecha 30-06-2026.
- **Viento (cap. 4)** en versión final: q ref 68,47→51,00 kgf/m² (−26%); cortes con
  parapeto Wx 41,5→21,6 / Wy 64,0→33,5 tonf; "---"→0 en solicitaciones.
- **Sismo**: espectros 2003/2025 (referencia, diseño, amplificado 0,7R₁, vertical), límites
  Cmáx/Cmín, clasificación de suelos 2003 vs 2025, períodos T*x=0,2788 / T*y=0,3507 s.
- **Idealización (7.6)**: el modelo idealizado **cumple** con 5 sustituciones (W 12×72 en
  vigas/columnas), 0/274 excede, razón máx 0,81.
- **Costos (7.7)**: 1.400 CLP/kg; acero 59.784→116.185 kg (+94%); costo 83,7→162,7 M CLP
  (sobrecosto ~79 M).
- **Conclusiones** (cap. 8): versión final de la tesis.

## Pendiente (ver detalle en `presentacion70/notas.md`)
- **E2 — Vigas 2 (dato por confirmar):** la tabla F.U. (slide "Factor de utilización máximo")
  da Instalado **0,146** con perfil `[] 200×200×3`; la tabla de Variación da **0,089** con
  `TBC 250×150×3`. No coinciden valor ni perfil → hay que elegir el correcto y dejarlo igual
  en ambas tablas.
- Otros opcionales (no requeridos para la versión final): imágenes muy pequeñas (pase global),
  mostrar Tabla 1 en viento, peso real de costaneras, Pilar G1 (biaxial), Figura zonificación
  (sacar zonas NC), origen de parámetros en viento, recubrimiento no estructural.

Cualquier duda, me dices. ¡Éxito! — Bruno
