# Guía: Layout Beamer con Fondo Personalizado (Lamina.png)

> [!IMPORTANT]
> Esta guía documenta cómo se resolvió el problema de **superposición de texto con el sidebar verde** en la presentación Beamer. Después de múltiples iteraciones, se logró que todo el contenido respete los límites de la imagen de fondo.

---

## Archivos Involucrados

| Archivo | Descripción |
|---|---|
| [presentacion_v2.tex](file:///d:/PROGRAMACION/%23TESIS-LATEX-AG/presentacion_v2.tex) | Archivo fuente LaTeX principal |
| [Lamina.png](file:///d:/PROGRAMACION/%23TESIS-LATEX-AG/Lamina.png) | Imagen de fondo (1280×720px, 16:9) |
| [medidas_lamina.png](file:///d:/PROGRAMACION/%23TESIS-LATEX-AG/medidas_lamina.png) | Imagen anotada con las medidas de referencia |

---

## 1. Medidas de la Imagen de Fondo

La imagen `Lamina.png` tiene dos zonas restringidas donde **NO debe haber texto**:

```
┌──────────────────────────────────────────────────┐
│▓▓▓▓│                                            │
│▓▓▓▓│                                            │
│▓▓▓▓│        ZONA BLANCA (contenido)             │
│▓▓▓▓│                                            │
│▓▓▓▓│                                            │
│▓▓▓▓├────────────────────────────────────────────│
│▓▓▓▓│  #SOMOSUSACH   franja decorativa inferior  │
└──────────────────────────────────────────────────┘
 22.9mm                                    
       ← sidebar verde →
                          ← franja inferior: 7mm desde abajo →
```

### Medidas exactas (verificadas por píxeles)

| Zona | Medida en px | Medida en mm | Cómo se obtuvo |
|---|---|---|---|
| **Sidebar verde** (ancho) | 183 px de 1280 | **22.9 mm** de 160 mm | Línea roja en `medidas_lamina.png` |
| **Franja inferior** (alto desde abajo) | 56 px de 720 | **7.0 mm** de 90 mm | Línea azul en `medidas_lamina.png` |
| **Transición verde→blanco** | empieza en x=127 px | 15.9 mm | Primer píxel blanco puro en `Lamina.png` |

### Dimensiones del papel Beamer 16:9

```
paperwidth  = 160 mm
paperheight =  90 mm
```

> [!NOTE]
> Conversión píxeles → mm: `mm = (px / ancho_imagen) × paperwidth`
> Ejemplo: `183 / 1280 × 160 = 22.9 mm`

---

## 2. El Problema: Texto Invadiendo el Sidebar

### Síntomas
- Los bullet points aparecían **encima del logo USACH** y del sidebar verde
- Esto ocurría **solo en slides con `\begin{columns}`**, no en slides simples
- El margen izquierdo de 3.5cm (35mm) funcionaba bien para slides sin columnas

### Diagnóstico por píxeles

Se verificó en los PNG renderizados usando Python + PIL:

```python
from PIL import Image
import numpy as np

img = Image.open('slide_renderizado.png')
w, h = img.size
arr = np.array(img)

# Buscar primer píxel oscuro (texto) en una fila
for x in range(200, 600):
    r, g, b = arr[300, x, :3]
    if r < 80 and g < 80 and b < 80:
        mm = x / w * 160  # convertir a mm
        print(f'Texto empieza en x={x}px = {mm:.1f}mm')
        break

# Buscar dónde termina el sidebar
for x in range(150, 400):
    r, g, b = arr[h//2, x, :3]
    if r > 240 and g > 240 and b > 240:
        mm = x / w * 160
        print(f'Sidebar termina en x={x}px = {mm:.1f}mm')
        break
```

### Resultados del diagnóstico

| Versión | Texto empieza en | Sidebar termina en | ¿Invade? |
|---|---|---|---|
| **Antes del fix** | 21.8 mm | 23.1 mm | ✅ Sí, 1.3mm dentro del sidebar |
| **Después del fix** | 42.8 mm | 23.0 mm | ❌ No, 19.8mm de buffer |

---

## 3. La Causa Raíz

> [!WARNING]
> En Beamer, el entorno `\begin{columns}` **NO respeta** completamente el `\setbeamersize{text margin left}`. Las columnas pueden expandirse más allá de los márgenes de texto configurados.

El comando `\setbeamersize{text margin left=3.5cm}` establece `\textwidth = paperwidth - margen_izq - margen_der = 160 - 35 - 3 = 122mm`. En slides simples (sin columnas), esto funciona perfecto. Pero en slides con `\begin{columns}[T]`, las columnas podían desbordarse hacia la izquierda.

---

## 4. La Solución

### 4.1. Forzar `totalwidth` en columnas

**Antes (malo):**
```latex
\begin{columns}[T]
    \column{0.60\textwidth}
    ...
    \column{0.37\textwidth}
```

**Después (correcto):**
```latex
\begin{columns}[T,totalwidth=\textwidth]
    \column{0.55\textwidth}
    ...
    \column{0.40\textwidth}
```

> [!TIP]
> `totalwidth=\textwidth` **fuerza** a que las columnas se ajusten exactamente al ancho de texto disponible, respetando los márgenes. Sin esta opción, Beamer puede expandir las columnas más allá del `\textwidth`.

### 4.2. Reducir el ancho de la columna de texto

Se redujo de `0.60` a `0.55` para dar más espacio y evitar que el texto largo haga wrap hacia la zona del sidebar. La columna de imagen se ajustó de `0.37` a `0.40`.

### 4.3. Acortar textos

Se acortaron los textos de los bullets para reducir el número de líneas de wrap:

```diff
-\item Los galpones de acero \alert{cerrados} son más susceptibles al
-      \alert{viento} que al sismo, por su baja masa y gran área expuesta.
+\item Galpones de acero \alert{cerrados}: más susceptibles al
+      \alert{viento} que al sismo, por su baja masa y gran área expuesta.
```

### 4.4. Footer blanco con texto negro

**Antes:**
```latex
\setbeamertemplate{footline}{%
  \begin{beamercolorbox}[...]{author in head/foot}%
    \usebeamerfont{author in head/foot}%
    Presentación N°1\hfill...%
  \end{beamercolorbox}%
}
```

**Después:**
```latex
\setbeamercolor{footline bar}{bg=white,fg=black}
\setbeamertemplate{footline}{%
  \begin{beamercolorbox}[...]{footline bar}%
    {\color{black}\usebeamerfont{author in head/foot}%
    Presentación N°1\hfill...}%
  \end{beamercolorbox}%
}
```

---

## 5. Configuración Completa de Márgenes

Estos son los valores finales en [presentacion_v2.tex](file:///d:/PROGRAMACION/%23TESIS-LATEX-AG/presentacion_v2.tex):

```latex
% === MÁRGENES ===
\setbeamersize{text margin left=3.5cm, text margin right=0.3cm}
% textwidth resultante = 160 - 35 - 3 = 122mm

% === BACKGROUND ===
\usebackgroundtemplate{%
    \includegraphics[width=\paperwidth,height=0.96\paperheight]{Lamina.png}}
% height=0.96 deja espacio para el footer

% === FRAMETITLE (centrado en zona blanca) ===
\setbeamertemplate{frametitle}{%
  \nointerlineskip%
  \begin{beamercolorbox}[wd=\paperwidth,sep=0.3cm]{frametitle}%
    \usebeamerfont{frametitle}%
    \hspace{3.5cm}%  ← empuja el título más allá del sidebar
    \makebox[\dimexpr\paperwidth-3.5cm-0.3cm\relax][c]{%
      \underline{\insertframetitle}}%
  \end{beamercolorbox}%
}

% === FOOTER (blanco + negro) ===
\setbeamercolor{footline bar}{bg=white,fg=black}
\setbeamertemplate{footline}{%
  \begin{beamercolorbox}[wd=\paperwidth,ht=2.5ex,dp=1.5ex,
      leftskip=3.5cm,rightskip=0.3cm]{footline bar}%
    {\color{black}\usebeamerfont{author in head/foot}%
    Presentación N°1\hfill\insertshortauthor\hfill
    \insertframenumber{} / \inserttotalframenumber}%
  \end{beamercolorbox}%
}

% === COLUMNAS (siempre con totalwidth) ===
\begin{columns}[T,totalwidth=\textwidth]
    \column{0.55\textwidth}  % texto
    \column{0.40\textwidth}  % imagen
\end{columns}
```

---

## 6. Comandos de Compilación

Ejecutar **cada línea por separado** en la terminal:

```powershell
cd "d:\PROGRAMACION\#TESIS-LATEX-AG"
pdflatex -interaction=nonstopmode presentacion_v2.tex
biber presentacion_v2
pdflatex -interaction=nonstopmode presentacion_v2.tex
pdflatex -interaction=nonstopmode presentacion_v2.tex
```

> [!CAUTION]
> Son **4 comandos separados**, no uno solo. La secuencia es: `pdflatex` → `biber` → `pdflatex` → `pdflatex`. Esto resuelve bibliografía y referencias cruzadas.

---

## 7. Cómo Verificar el Layout (Diagnóstico Futuro)

Si en el futuro se modifica el contenido y se necesita verificar que el texto sigue dentro de los límites:

### Paso 1: Renderizar slide a PNG

```python
import fitz  # PyMuPDF
doc = fitz.open('presentacion_v2.pdf')
page = doc[2]  # página 3 (0-indexed)
pix = page.get_pixmap(dpi=200)
pix.save('check.png')
```

### Paso 2: Verificar posiciones

```python
from PIL import Image
import numpy as np

img = Image.open('check.png')
w, h = img.size
arr = np.array(img)

# ¿Dónde empieza el texto? (escanear fila por fila)
for y in [250, 300, 350, 400]:
    for x in range(150, 600):
        r, g, b = arr[y, x, :3]
        if r < 80 and g < 80 and b < 80:
            mm = x / w * 160
            print(f'y={y}: texto en x={x}px = {mm:.1f}mm')
            break

# ¿Dónde termina el sidebar?
for x in range(150, 400):
    r, g, b = arr[h//2, x, :3]
    if r > 240 and g > 240 and b > 240:
        mm = x / w * 160
        print(f'Sidebar termina en x={x}px = {mm:.1f}mm')
        break
```

### Paso 3: Validar

| Condición | Valor esperado |
|---|---|
| Texto empieza después de | > 23 mm (sidebar) |
| Texto empieza antes de | < 50 mm (no demasiado lejos) |
| Buffer mínimo recomendado | ≥ 10 mm |

---

## 8. Reglas de Oro para Futuras Ediciones

1. **Siempre usar `totalwidth=\textwidth`** en `\begin{columns}`
2. **No usar columnas > 0.55 para texto** cuando hay sidebar
3. **Probar con PyMuPDF + PIL** si hay duda sobre superposición
4. **Los bullets largos wrappean** — acortar texto si necesario
5. **El footer usa `footline bar`** (no `author in head/foot`) para mantenerlo blanco
6. **`\setbeamersize` afecta `\textwidth`** pero NO afecta el `frametitle` — por eso el frametitle tiene su propio `\hspace{3.5cm}`
