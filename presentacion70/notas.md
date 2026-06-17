# Notas — Presentación 70% (Reordenado)

## ✅ LISTO
- 3. ~~Mostrar metodología desglosada (etapas 1–5) en varias diapositivas.~~
- 4. ~~Mencionar condiciones de apoyo (P1 empotrado / P2 articulado + figura + tabla).~~
- 5. ~~Mencionar cargas muertas (costaneras).~~ *(mencionadas; valor de peso aún "[pendiente]" — ver Pendiente #5b)*
- 6. ~~Explicación desarrollo Espectro de Diseño (2003 y 2025): fórmulas (Ec. 5-5 / Ec. 1a, 2, 3, 4).~~
- 7. ~~Parámetros que dependen del suelo + Periodos T*x, T*y en diapositiva de análisis modal.~~
- 8. ~~Espectro Referencia (2025): corte máximo (Cmáx) y mínimo (Cmín) marcados.~~
- 10. ~~Mostrar Planta y Elevación en diapositivas separadas.~~
- 12. ~~Cambiar "Falla" por "NO CUMPLE".~~
- 13. ~~Mencionar que utilizamos ASD (NCh3171 / NCh427/1).~~
- 14. ~~Figura 13 y 14 (viento Of.1971) cada una en su diapositiva.~~
- 16. ~~Corregir nota NCh3171.Of2010 (versión 2017 oficializada en 2024).~~
- 17. ~~Zonificación y presiones: rojos de variación → flechas (sin color).~~
- 19. ~~Sismo NCh2369:2025: "s" en T*, líneas corte mín/máx, "Asimilación" → "homologación".~~
- 20. ~~Explicar el cambio de suelo (clasificación 2003 vs 2025) — diapositiva nueva.~~

## ⏳ PENDIENTE
- 1. Imágenes muy pequeñas (pase global). *Parcial: varias ya se agrandaron al separarlas (planta/elevación, viento, discrepancia); falta el ajuste global de tamaños.*
- 2. Mostrar Tabla 1 cuando se mencione (Viento).
- 5b. Cargas muertas: cargar el **peso real de costaneras** (hoy "[pendiente]").
- 9. Analizar viento considerando paramentos.
- 11. Pilar G1: presión biaxial (verificación con fuerza lateral; chequear si la carga lateral de la norma nueva afecta).
- 15. Figura 19 (Zonificación NCh432:2025): sacar zonas NC y mejorar identificación "ZONA III-A".
- 18. Viento — solicitaciones globales: donde se anula poner 0 (o valor), no una raya "---".
- 21. Mencionar de dónde vienen los parámetros (modelo vs tabla/normativa). *Parcial: hecho en tablas de sismo; falta en viento/otros.*
- 22. Viento: calcular por alturas distintas (tramos).
- 23. Recubrimiento de techo y paredes sin responsabilidad estructural (el esqueleto toma la carga).

## ⚠️ ERRORES / INCONSISTENCIAS DETECTADAS
- **E1. Períodos T\*:** ~~Masa Modal indica T_x=0,2788 s y T_y=0,3507 s, pero las slides de Sismo usaban T*x=0,22 / T*y=0,34.~~ **CORREGIDO**: T*x=0,2788 s y T*y=0,3507 s (mismos para 2003 y 2025) en Sismo 2025 y Comparativa.

### Por corregir
- **E2. Vigas 2:** la tabla F.U. (slide 52) da Instalado = 0,146 con perfil [] 200×200×3; la tabla de Variación (slide 53) da 0,089 con perfil TBC 250×150×3. No coinciden valor ni perfil del Instalado. → confirmar el correcto.
- **E3. Conclusiones (F.U.):** dice "diagonales horizontales [1,464]" (valor inexistente; la diag. horizontal real es 0,737 = OK, no falla) y "vigas [1,353]" (ese es el Instalado; el Actualizado es 1,173). Los que realmente NO CUMPLEN (Actualizado) son: Columnas 1 (1,474), Diagonales vert. (2,265) y Vigas 1 (1,173).
- **E4. Conclusiones (desplazamientos):** dice "superando los 11,14 mm del viento", pero el máximo de viento es 9,02 mm (instalado) / 2,96 mm (actualizado). El 11,14 no aparece en ninguna tabla.

### 🧹 Limpieza
- Figuras huérfanas sin uso: `fig04.png` y `fig05.png` (reemplazadas por los espectros nuevos) — se pueden borrar.
