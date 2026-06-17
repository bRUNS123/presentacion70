# -*- coding: utf-8 -*-
"""Comparacion espectros de diseno NCh2369 Of.2003 (Suelo III) vs 2025 (Suelo C).
   Reemplaza espectros_comp.png con etiquetas correctas (xi=0,03, sin '$' sueltos)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "../Figuras/"
xi = 0.03
damp = (0.05/xi)**0.4
T = np.linspace(0.001, 3.5, 2500)

# --- 2003 (Suelo III): Sa = 2.75 A0 I /R (T'/T)^n damp, tope Cmax=0.203 ---
A0, I, R = 0.30, 1.00, 4.0
Tp, n = 0.62, 1.80
Sa03 = np.minimum(2.75*A0*I/R*(Tp/T)**n*damp, 0.203)

# --- 2025 (Suelo C): Sa = I SaH /R damp, acotado [Cmin, Cmax] ---
Ar, S, r, T0, p, q = 0.42, 1.05, 4.50, 0.40, 1.50, 3.00
Cmin, Cmax = 0.110, 0.298
SaH = Ar*S*(1 + r*(T/T0)**p)/(1 + (T/T0)**q)
Sa25 = np.clip(I*SaH/R*damp, Cmin, Cmax)

fig, ax = plt.subplots(figsize=(5.4, 3.6))
ax.fill_between(T, Sa03, Sa25, where=(Sa25 >= Sa03), color="#c0504d", alpha=0.20,
                label="Incremento demanda (2025)")
ax.fill_between(T, Sa03, Sa25, where=(Sa25 < Sa03), color="#1f4e79", alpha=0.20,
                label="Reducción demanda (2025)")
ax.plot(T, Sa03, lw=2.2, color="#1f4e79", label="NCh2369 Of.2003 (Suelo III)")
ax.plot(T, Sa25, lw=2.2, color="#c0504d", label="NCh2369:2025 (Suelo C)")
ax.set_xlim(0, 3.5); ax.set_ylim(0, 0.35)
ax.set_xlabel("Período T [s]")
ax.set_ylabel("Aceleración espectral Sa [g]")
ax.set_title("Comparación de espectros de diseño  [ξ = 0,03, Zona 2]", fontsize=10)
ax.grid(True, ls=":", alpha=0.6)
ax.legend(fontsize=8, loc="upper right")
fig.tight_layout(); fig.savefig(OUT+"espectros_comp.png", dpi=200); plt.close(fig)
print("OK espectros_comp.png regenerado")
