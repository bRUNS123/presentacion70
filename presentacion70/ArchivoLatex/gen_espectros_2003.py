# -*- coding: utf-8 -*-
"""Genera espectros NCh2369.Of2003 para la presentacion:
   - espectro_2003_H.png : horizontal R=4, xi=0.03, con linea Cmax=0.203
   - espectro_2003_V.png : vertical   R=3, xi=0.03 (datos provistos)
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "../Figuras/"

# ---- Parametros comunes (Nave F) ----
A0 = 0.30        # Zona 2
I  = 1.00        # importancia
xi = 0.03
Tp = 0.62        # T'  suelo III
n  = 1.80        # n   suelo III
damp = (0.05/xi)**0.4

# =================================================================
# 1) ESPECTRO HORIZONTAL  R=4  (Ec. 5-5) con tope Cmax = 0.203
# =================================================================
R_h   = 4.0
Cmax  = 0.203
T = np.linspace(0.001, 3.0, 1500)
Sa_raw = (2.75*A0*I/R_h)*(Tp/T)**n*damp
Sa = np.minimum(Sa_raw, Cmax)

fig, ax = plt.subplots(figsize=(5.6, 4.0))
ax.plot(T, Sa, lw=2.4, color="#1f4e79", label=r"$S_a$ diseño (R=4)")
ax.axhline(Cmax, ls="--", lw=1.6, color="#c0504d")
ax.annotate(r"$C_{máx}=0{,}203\,g$", xy=(2.0, Cmax), xytext=(1.45, Cmax+0.022),
            color="#c0504d", fontsize=11, fontweight="bold")
ax.set_xlim(0, 3.0); ax.set_ylim(0, 0.30)
ax.set_xlabel(r"Período $T$ [s]"); ax.set_ylabel(r"$S_a$ [g]")
ax.set_title("Espectro horizontal NCh2369.Of2003  [Zona 2, Suelo III, R=4]",
             fontsize=10)
ax.grid(True, ls=":", alpha=0.6)
ax.legend(fontsize=9, loc="upper right")
fig.tight_layout()
fig.savefig(OUT+"espectro_2003_H.png", dpi=200)
plt.close(fig)

# =================================================================
# 2) ESPECTRO VERTICAL  R=3  (Cl. 5.5.2) -- datos provistos
# =================================================================
DATA_V = """
0.000 0.255
0.720 0.255
0.730 0.251
0.800 0.213
0.900 0.172
1.000 0.143
1.200 0.103
1.400 0.078
1.600 0.061
1.800 0.050
2.000 0.041
2.500 0.027
3.000 0.020
3.500 0.015
4.000 0.012
4.500 0.010
5.000 0.008
"""
# Reconstruccion fiel: plateau 0.255 hasta 0.72 s, luego 0.255*(0.72/T)^1.8
Tv = np.linspace(0.001, 5.0, 2000)
Tb = 0.72
Sav = np.where(Tv <= Tb, 0.255, 0.255*(Tb/Tv)**1.8)
IA0 = I*A0   # 0.30 -> ordenada no necesita superar I*A0

fig, ax = plt.subplots(figsize=(5.6, 4.0))
ax.plot(Tv, Sav, lw=2.2, color="#7030a0", label=r"$S_a$ vertical (R=3)")
ax.axhline(IA0, ls="--", lw=1.4, color="0.4")
ax.annotate(r"$I\,A_0 = 0{,}30\,g$ (límite)", xy=(2.0, IA0), xytext=(1.35, IA0+0.013),
            color="0.3", fontsize=10)
ax.annotate(r"meseta $0{,}255\,g$", xy=(0.35, 0.255), xytext=(0.65, 0.220),
            color="#7030a0", fontsize=10, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#7030a0", lw=1))
ax.set_xlim(0, 3.0); ax.set_ylim(0, 0.34)
ax.set_xlabel(r"Período $T$ [s]"); ax.set_ylabel(r"$S_a$ [g]")
ax.set_title("Espectro vertical NCh2369.Of2003  [Cl. 5.5.2, R=3, ξ=0,03]",
             fontsize=10)
ax.grid(True, ls=":", alpha=0.6)
ax.legend(fontsize=9, loc="lower left")
fig.tight_layout()
fig.savefig(OUT+"espectro_2003_V.png", dpi=200)
plt.close(fig)

print("OK: espectro_2003_H.png y espectro_2003_V.png generados")
