"""Render the conceptual method figures as vector PDFs and 300 dpi PNGs."""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

OUT = Path(__file__).resolve().parent.parent
INK = "#1b1d1f"
MUTED = "#454b50"
RULE = "#9aa0a3"
ACCENT = "#e9eff2"
mpl.rcParams.update({"font.family": "DejaVu Sans", "pdf.fonttype": 42})


def page(height):
    fig = plt.figure(figsize=(516 / 72, height / 72))
    ax = fig.add_axes((0, 0, 1, 1), xlim=(0, 516), ylim=(0, height))
    ax.set_axis_off()
    return fig, ax


def label(ax, x, y, text, size=8, color=INK, weight="normal", align="left"):
    return ax.text(x, y, text, fontsize=size, color=color, weight=weight,
                   ha=align, va="center", linespacing=1.22)


def line(ax, points, color=INK, width=0.85, style="-"):
    x, y = zip(*points)
    ax.plot(x, y, color=color, lw=width, ls=style, solid_capstyle="round")


def arrow(ax, start, end, color=INK, width=0.85):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=7.5,
                                shrinkA=0, shrinkB=0, lw=width,
                                color=color))


def panel(ax, x, y, title, right):
    label(ax, x, y, title, size=7.5, weight="bold")
    line(ax, [(x, y - 10), (right, y - 10)], RULE, 0.65)


def block(ax, left, bottom, width, height, title, detail=None, *, accent=False):
    face = ACCENT if accent else "white"
    ax.add_patch(Rectangle((left, bottom), width, height, facecolor=face,
                           edgecolor=INK, lw=0.75))
    x = left + width / 2
    y = bottom + height / 2
    label(ax, x, y + (5 if detail else 0), title, 8.4, weight="medium", align="center")
    if detail:
        label(ax, x, y - 5, detail, 7.8, align="center")

def save(fig, name):
    fig.savefig(OUT / f"{name}.pdf", metadata={"CreationDate": None, "ModDate": None})
    fig.savefig(OUT / f"{name}.png", dpi=300)
    plt.close(fig)


def node(ax, x, y):
    ax.add_patch(Circle((x, y), 1.6, color=INK))


def transistor(ax, y):
    # Simplified n-channel symbol, with the body tied to the source.
    line(ax, [(53, y + 13), (53, y + 9), (46, y + 9), (46, y + 5)])
    line(ax, [(46, y + 2), (46, y - 2)])
    line(ax, [(46, y - 5), (46, y - 9), (53, y - 9), (53, y - 13)])
    line(ax, [(53, y - 9), (53, y)])
    arrow(ax, (53, y), (46, y), INK, width=0.7)
    line(ax, [(41, y + 8), (41, y - 8)])
    line(ax, [(33, y), (41, y)])
    node(ax, 53, y - 9)


def circuit(ax):
    # Geometry follows the supplied synchronous buck schematic.
    line(ax, [(15, 173), (15, 243), (53, 243), (53, 241)])
    ax.add_patch(Circle((15, 165), 8, fill=False, edgecolor=INK, lw=0.85))
    line(ax, [(12.6, 168), (17.4, 168)])
    line(ax, [(15, 165.6), (15, 170.4)])
    line(ax, [(12.6, 162), (17.4, 162)])
    line(ax, [(15, 157), (15, 145), (179, 145)])
    line(ax, [(15, 145), (15, 140)])
    for y, width in [(140, 10), (137.5, 6.5), (135, 3)]:
        line(ax, [(15 - width / 2, y), (15 + width / 2, y)])
    transistor(ax, 228)
    transistor(ax, 175)
    line(ax, [(53, 215), (53, 188)])
    line(ax, [(53, 162), (53, 145)])
    line(ax, [(53, 201), (79, 201)])
    x = np.linspace(0, np.pi, 20)
    for start in [79, 86, 93, 100]:
        line(ax, zip(start + 7 * x / np.pi, 201 + 4.8 * np.sin(x)))
    line(ax, [(107, 201), (117, 201)])
    ax.add_patch(Rectangle((117, 198), 18, 6, fill=False, edgecolor=INK, lw=0.85))
    line(ax, [(135, 201), (179, 201), (179, 176)])
    ax.add_patch(Rectangle((176, 158), 6, 18, fill=False, edgecolor=INK, lw=0.85))
    line(ax, [(179, 158), (179, 145)])
    line(ax, [(148, 201), (148, 184)])
    line(ax, [(143, 184), (153, 184)])
    line(ax, [(143, 180), (153, 180)])
    line(ax, [(148, 180), (148, 167)])
    ax.add_patch(Rectangle((145, 154), 6, 13, fill=False, edgecolor=INK, lw=0.85))
    line(ax, [(148, 154), (148, 145)])
    for x, y in [(53, 201), (53, 145), (148, 201), (148, 145), (179, 201), (179, 145)]:
        node(ax, x, y)
    label(ax, 23, 155, r"$V_{\mathrm{in}}$", size=8.5)
    label(ax, 58, 232, r"$Q_1$", size=8.5)
    label(ax, 58, 176, r"$Q_2$", size=8.5)
    label(ax, 94, 211, r"$L_{\mathrm{out}}$", size=8.5, align="center")
    label(ax, 127, 211, r"$\mathrm{ESR}_L$", size=8.5, align="center")
    label(ax, 184, 211, r"$V_{\mathrm{out}}$", size=8.5, align="right")
    label(ax, 140, 181, r"$C_{\mathrm{out}}$", size=8.2, align="right")
    label(ax, 140, 160, r"$\mathrm{ESR}_C$", size=8.2, align="right")
    label(ax, 185, 168, r"$R_{\mathrm{out}}$", size=8.2)
    label(ax, 6, 125, r"FRA input $\delta d$  /  output $\delta v_{\mathrm{out}}$", size=8.0)
    label(ax, 6, 113, r"Load range $2$ to $8\,\Omega$ (nominal $4\,\Omega$)", size=8.0)


def draw_overview():
    fig, ax = page(279)
    panel(ax, 6, 265, "(a) Synchronous buck converter", 205)
    panel(ax, 221, 265, "(b) Spectral augmentation", 510)
    circuit(ax)

    block(ax, 221, 177, 79, 29, "Healthy sweep", r"$H_i(j\omega)$")
    line(ax, [(300, 191.5), (315, 191.5)])
    line(ax, [(315, 148), (315, 233)])
    node(ax, 315, 191.5)
    views = [
        (233, "Identity", r"$H_i$", "Anchor"),
        (191.5, "Small perturbation", r"$H_i^+$", "Positive view"),
        (148, r"Multiply by $\Gamma_{\boldsymbol{\alpha}}$",
         r"$H_i^-=H_i\Gamma_{\boldsymbol{\alpha}}$", "Synthetic fault view"),
    ]
    for y, operation, spectrum, role in views:
        arrow(ax, (315, y), (424, y))
        label(ax, 375, y + 8, operation, 8.3, align="center")
        label(ax, 431, y + 2, spectrum, 9.2)
        label(ax, 431, y - 10, role, 7.7, MUTED)
    label(ax, 221, 122, r"SSA ratio $\Gamma_{\boldsymbol{\alpha}}$ evaluated at the nominal $4\,\Omega$ load.",
          8.0)
    label(ax, 221, 108, "Standardize the real and imaginary parts of each view.", 8.0)

    panel(ax, 6, 89, "(c) Anomaly scoring and calibration", 510)
    block(ax, 6, 41, 73, 28, "Query spectrum", r"$\mathbf{X}$")
    arrow(ax, (79, 55), (94, 55))
    block(ax, 94, 41, 116, 28, "Encoder and projection",
          r"$\mathbf{z}=p(f(\mathbf{X}))$")
    arrow(ax, (210, 55), (225, 55))
    block(ax, 225, 41, 126, 28, r"5-NN score $a(\mathbf{X})$",
          r"Mean of five $\ell_2$ distances", accent=True)
    arrow(ax, (351, 55), (366, 55))
    block(ax, 366, 41, 144, 28, "Anomaly decision",
          r"Flag if $a(\mathbf{X})>\tau$")
    arrow(ax, (288, 27), (288, 41))
    label(ax, 288, 19, "Healthy training embeddings", 8.0, align="center")
    arrow(ax, (438, 29), (438, 41))
    label(ax, 438, 21, "Healthy validation scores", 8.0, align="center")
    label(ax, 438, 10, r"$\tau$ is their 97.5th percentile", 7.8, align="center")
    save(fig, "fig01_system_and_carla_framework")


def draw_architecture():
    fig, ax = page(222)
    panel(ax, 6, 209, "(a) Shared encoder", 156)
    panel(ax, 183, 209, "(b) Reconstruction", 330)
    panel(ax, 359, 209, "(c) Contrastive projection", 510)

    # The attention stack is drawn once and annotated with its two widths.
    label(ax, 81, 17, r"$\mathbf{X}_i,\;\mathbf{X}_i^+,\;\mathbf{X}_i^-\in\mathbb{R}^{101\times2}$",
          9, align="center")
    arrow(ax, (81, 26), (81, 33))
    block(ax, 6, 33, 150, 25, "Linear input projection", "Sinusoidal position encoding")
    arrow(ax, (81, 58), (81, 68))
    ax.add_patch(Rectangle((6, 64), 150, 77, fill=False, edgecolor=RULE, lw=0.7))
    block(ax, 14, 68, 134, 24, "Four-head self-attention", "Residual and layer norm", accent=True)
    arrow(ax, (81, 92), (81, 100))
    block(ax, 14, 100, 134, 24, "Position-wise feed-forward", "Residual and layer norm")
    label(ax, 81, 132, "Two blocks, widths 64 and 128", 7.9, align="center")
    arrow(ax, (81, 141), (81, 149))
    block(ax, 6, 149, 150, 22, "Mean pooling + linear projection")
    arrow(ax, (81, 171), (81, 180))
    block(ax, 45, 180, 72, 17, r"$\mathbf{h}\in\mathbb{R}^{128}$")

    # The decoder receives only the anchor representation. All views use p.
    line(ax, [(117, 188.5), (434.5, 188.5)])
    node(ax, 256.5, 188.5)
    arrow(ax, (256.5, 188.5), (256.5, 153))
    arrow(ax, (434.5, 188.5), (434.5, 153))
    label(ax, 263, 173, "Anchor only", 8)
    label(ax, 441, 173, "All views", 8)

    block(ax, 183, 123, 147, 30, "Self-attention decoder",
          "Two blocks, widths 128 and 64", accent=True)
    arrow(ax, (256.5, 123), (256.5, 105))
    block(ax, 183, 77, 147, 28, "Reconstructed spectrum",
          r"$\widehat{\mathbf{X}}_i\in\mathbb{R}^{101\times2}$")
    arrow(ax, (256.5, 77), (256.5, 56))
    label(ax, 256.5, 46, "Reconstruction loss", 8.4, weight="medium", align="center")
    label(ax, 256.5, 31, r"$\mathrm{MSE}(\mathbf{X}_i,\widehat{\mathbf{X}}_i)$",
          8.7, align="center")

    projection_layers = [
        (136, "Linear (128)", True),
        (109, "Batch normalization + ReLU", False),
        (82, "Linear (128)", True),
        (55, r"$\ell_2$ normalization", False),
    ]
    for bottom, title, accent in projection_layers:
        block(ax, 359, bottom, 151, 17, title, accent=accent)
        arrow(ax, (434.5, bottom), (434.5, bottom - 10))
    label(ax, 434.5, 37, r"$\mathbf{z}_i,\;\mathbf{z}_i^+,\;\mathbf{z}_i^-$",
          9.2, align="center")
    arrow(ax, (434.5, 28), (434.5, 21))
    label(ax, 434.5, 12, r"Contrastive loss $\mathcal{L}_{\mathrm{c}}$",
          8.4, weight="medium", align="center")
    save(fig, "fig03_carla_transformer_architecture")


if __name__ == "__main__":
    draw_overview()
    draw_architecture()
