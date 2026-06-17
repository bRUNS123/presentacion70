# -*- coding: utf-8 -*-
"""Espectros NCh2369:2025 (Zona 2, Suelo C) para la presentacion:
   - espectro_2025_H.png : diseno horizontal con limites Cmax y Cmin
   - espectro_2025_V.png : diseno vertical (Ec. 2, R_V=2)
Formulas: Ec.(3) referencia H, Ec.(4) referencia V, Ec.(1a) diseno H, Ec.(2) diseno V.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "../Figuras/"

# ---- Parametros sitio: Zona 2, Suelo C ----
A0 = 0.30
Ar = 1.40*A0          # 0.42 g (Tabla 3)
S, r, T0, p, q = 1.05, 4.50, 0.40, 1.50, 3.00   # Tabla 6, Suelo C
I  = 1.00
R  = 4.0
Rv = 2.0
xi = 0.03
damp = (0.05/xi)**0.4

# Limites del coeficiente sismico (horizontal)
Cmin = 0.25*I*Ar*S                       # Ec. (12)
Cmax = I*(2.75*Ar*S/(R+1.0))*damp        # C5.13

T = np.linspace(0.001, 3.0, 2000)

# ---- Espectro de diseno HORIZONTAL (desde txt del modelo) + amplificado ----
TXT = "../../espectro_NCh2369-2025_X_Zona2_C_R4.txt"   # T[s], Sa_X[g]
try:
    d = np.loadtxt(TXT, skiprows=1, usecols=(0, 1))
    Td, Sa_H = d[:, 0], d[:, 1]
except Exception:
    Td = T
    SaH = Ar*S*(1 + r*(T/T0)**p)/(1 + (T/T0)**q)       # Ec. (3)
    Sa_H = np.clip(I*SaH/R*damp, Cmin, Cmax)           # Ec. (1a)

R1 = 4.0
Sa_amp = 0.7*R1*Sa_H                                    # espectro amplificado (0,7 R1)

# Espectro de referencia (elastico, Ec. 3) desde txt
try:
    dref = np.loadtxt("../../espectro_ref_2025.txt", skiprows=1, usecols=(0, 1))
    Tref, Sa_ref = dref[:, 0], dref[:, 1]
except Exception:
    Tref = T
    Sa_ref = Ar*S*(1 + r*(T/T0)**p)/(1 + (T/T0)**q)

fig, ax = plt.subplots(figsize=(5.8, 4.0))
ax.plot(Tref, Sa_ref, lw=2.0, color="#555555",
        label=r"$S_a$ referencia (elástico, Ec. 3)")
ax.plot(Td, Sa_amp, lw=2.0, ls="--", color="#c55a11",
        label=r"$S_a$ amplificado ($0{,}7R_1$)")
ax.plot(Td, Sa_H, lw=2.4, color="#1f4e79", label=r"$S_a$ diseño (R=4)")
Cmax_amp = 0.7*R1*Cmax                                  # tope del amplificado
ax.axhline(Cmax_amp, ls="--", lw=1.3, color="#c55a11")
ax.axhline(Cmax, ls="--", lw=1.3, color="#c0504d")
ax.axhline(Cmin, ls="--", lw=1.3, color="#548235")
ax.annotate(r"$C_{máx,amp}=0{,}834$", xy=(2.4, Cmax_amp), xytext=(1.55, Cmax_amp+0.03),
            color="#c55a11", fontsize=9, fontweight="bold")
ax.annotate(r"$C_{máx}=0{,}298$", xy=(2.4, Cmax), xytext=(2.0, Cmax+0.03),
            color="#c0504d", fontsize=9, fontweight="bold")
ax.annotate(r"$C_{mín}=0{,}110$", xy=(2.4, Cmin), xytext=(2.0, Cmin+0.03),
            color="#548235", fontsize=9, fontweight="bold")
ax.set_xlim(0, 3.0); ax.set_ylim(0, 1.30)
ax.set_xlabel(r"Período $T$ [s]"); ax.set_ylabel(r"$S_a$ [g]")
ax.set_title("Espectro horizontal NCh2369:2025  [Zona 2, Suelo C, R=4]", fontsize=10)
ax.grid(True, ls=":", alpha=0.6)
ax.legend(fontsize=8.5, loc="upper right")
fig.tight_layout(); fig.savefig(OUT+"espectro_2025_H.png", dpi=200); plt.close(fig)

# ---- Espectro de referencia y diseno VERTICAL ----
SaV = 0.7*Ar*S*(1 + r*(1.7*T/T0)**p)/(1 + (1.7*T/T0)**q)   # Ec. (4)
Sa_V = I*SaV/Rv*damp                                         # Ec. (2)

fig, ax = plt.subplots(figsize=(5.8, 4.0))
ax.plot(T, Sa_V, lw=2.4, color="#7030a0", label=r"$S_{a,v}$ diseño ($R_V$=2)")
ax.set_xlim(0, 3.0); ax.set_ylim(0, max(0.34, Sa_V.max()*1.1))
ax.set_xlabel(r"Período $T_V$ [s]"); ax.set_ylabel(r"$S_{a,v}$ [g]")
ax.set_title("Espectro vertical NCh2369:2025  [Ec. (2), $R_V$=2, ξ=0,03]", fontsize=10)
ax.grid(True, ls=":", alpha=0.6)
ax.legend(fontsize=9, loc="upper right")
fig.tight_layout(); fig.savefig(OUT+"espectro_2025_V.png", dpi=200); plt.close(fig)

print(f"OK  Cmin={Cmin:.3f}  Cmax={Cmax:.3f}  SaV_max={Sa_V.max():.3f}")
