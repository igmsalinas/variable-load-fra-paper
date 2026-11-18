"""Render the conceptual method figures as vector PDFs and 300 dpi PNGs."""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle

OUT = Path(__file__).resolve().parent.parent
INK = "#1e2c37"
MUTED = "#49606d"
RULE = "#b7c7d0"
PANEL = "#f2f6f8"
BLUE = "#1d547b"
TEAL = "#246e60"
AMBER = "#9a531b"
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


def arrow(ax, start, end, color=BLUE, style="-", width=0.9):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=7.5,
                                shrinkA=0, shrinkB=0, lw=width,
                                color=color, linestyle=style))


def panel(ax, x, y, title, right):
    label(ax, x, y, title, size=10.2, weight="bold")
    line(ax, [(x, y - 10), (right, y - 10)], RULE, 0.65)


def card(ax, x, y, w, h, title, body, *, color=BLUE, face=PANEL):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=face, edgecolor=RULE, lw=0.6))
    label(ax, x + w / 2, y + h / 2 + 6, title, 8.4, color, "bold", "center")
    label(ax, x + w / 2, y + h / 2 - 6.2, body, 7.8, INK, "normal", "center")


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


def spectra(ax, x, y, w, h, view):
    color, style, offset = {
        "anchor": (BLUE, "-", 0.0),
        "positive": (TEAL, "--", 0.07),
        "negative": (AMBER, "-.", 0.14),
    }[view]
    f = np.linspace(0, 1, 110)
    g = 0.51 + (0.36 - offset) * np.exp(-((f - 0.33 - offset) / 0.18) ** 2)
    g -= (0.38 + offset / 2) * f**1.8
    if view == "positive":
        g = 0.51 + 0.36 * np.exp(-((f - 0.33) / 0.18) ** 2) - 0.38 * f**1.8
        g += 0.022 * np.sin(41 * f)
    line(ax, [(x, y + h), (x, y), (x + w, y)], RULE, 0.65)
    line(ax, zip(x + w * f, y + h * g), color, 1.45, style)


def nearest_neighbors(ax):
    query = np.array((252, 54))
    near = [(223, 62), (229, 43), (237, 64), (241, 37), (267, 61)]
    far = [(210, 43), (212, 59), (227, 74), (255, 73), (271, 37), (213, 31)]
    for x, y in far:
        ax.plot(x, y, "o", color=RULE, ms=3)
    for x, y in near:
        line(ax, [(x, y), query], BLUE, 0.65, ":")
        ax.plot(x, y, "o", mfc="white", mec=BLUE, ms=3.8, mew=0.9)
    ax.plot(*query, "D", color=AMBER, ms=4.5)
    label(ax, 257, 47, r"$\mathbf{z}$", 8.0, AMBER)
    label(ax, 241, 22, "Five nearest healthy", 7.4, align="center")
    label(ax, 241, 12, "training embeddings", 7.4, align="center")


def draw_overview():
    fig, ax = page(279)
    panel(ax, 6, 265, "(a) Synchronous buck and FRA", 206)
    panel(ax, 221, 265, "(b) Training views in the complex spectrum", 510)
    circuit(ax)
    label(ax, 247, 242, "Healthy anchor", 8.2, BLUE, "bold", "center")
    label(ax, 247, 228, r"$H_i$", 8.2, BLUE, align="center")
    spectra(ax, 224, 174, 45, 42, "anchor")
    label(ax, 271, 169, r"$f$", 7.5, MUTED, align="right")
    line(ax, [(271, 201), (278, 201), (278, 145)], BLUE, 0.8)
    line(ax, [(278, 201), (278, 238)], BLUE, 0.8)
    for y in [238, 196, 145]:
        arrow(ax, (278, y), (290, y))
    label(ax, 295, 238, "Unmodified", 8.2, BLUE)
    label(ax, 295, 196, "Small perturbation", 8.2, TEAL)
    label(ax, 295, 146, r"Multiply by $\Gamma_{\alpha}$", 8.2, AMBER)
    label(ax, 295, 135, "SSA fault-to-healthy ratio", 7.2, MUTED)
    label(ax, 295, 125, r"evaluated at $4\,\Omega$", 7.2, MUTED)
    for (y, name, view, color) in [
            (238, r"$H_i$", "anchor", BLUE),
            (196, r"$H_i^+$", "positive", TEAL),
            (145, r"$H_i^-=H_i\Gamma_{\alpha}$", "negative", AMBER)]:
        arrow(ax, (392, y), (410, y), color)
        spectra(ax, 417, y - 13, 42, 27, view)
        label(ax, 464, y, name, 8.5, color)
    label(ax, 221, 110, "Represent each view by standardized real and imaginary components.",
          7.7, MUTED)

    panel(ax, 6, 90, "(c) Anomaly scoring and healthy-only calibration", 510)
    card(ax, 6, 37, 75, 33, "Query sweep", "Complex FRA")
    arrow(ax, (81, 53.5), (93, 53.5))
    card(ax, 93, 37, 100, 33, "Frozen network", "Encoder and projection")
    arrow(ax, (193, 53.5), (205, 53.5))
    nearest_neighbors(ax)
    arrow(ax, (275, 53.5), (291, 53.5))
    card(ax, 291, 37, 93, 33, r"Score $a(\mathbf{X})$", "Mean distance")
    arrow(ax, (384, 53.5), (403, 53.5))
    card(ax, 403, 36, 107, 35, r"Flag if $a(\mathbf{X})>\tau$", "Anomaly decision",
         color=AMBER, face="#fbf5ed")
    arrow(ax, (456.5, 29), (456.5, 36), TEAL)
    label(ax, 456.5, 21, "Healthy validation scores", 7.6, TEAL, "bold", "center")
    label(ax, 456.5, 11, r"$\tau$: 97.5th percentile", 7.4, INK, align="center")
    save(fig, "fig01_system_and_carla_framework")


def layer(ax, x, y, width, height, fill, edge, cells=0):
    """Draw a thin feature plane with an isometric offset."""
    lift = 5
    ax.add_patch(Polygon([(x, y + height), (x + lift, y + height + lift),
                          (x + width + lift, y + height + lift),
                          (x + width, y + height)], facecolor="white",
                         edgecolor=edge, lw=0.65, zorder=3))
    ax.add_patch(Polygon([(x + width, y), (x + width + lift, y + lift),
                          (x + width + lift, y + height + lift),
                          (x + width, y + height)], facecolor=fill,
                         edgecolor=edge, lw=0.65, zorder=3, alpha=0.88))
    ax.add_patch(Rectangle((x, y), width, height, facecolor=fill,
                           edgecolor=edge, lw=0.75, zorder=3))
    for dy in np.linspace(0, height, cells + 1)[1:-1]:
        ax.plot([x, x + width], [y + dy, y + dy], color=edge, lw=0.35, zorder=4)


def feature_stack(ax, x, y, height, blocks, tint, edge):
    for i in reversed(range(blocks)):
        layer(ax, x + 5 * i, y + 3 * i, 21, height, tint, edge, cells=5)


def tokens(ax, x, y, edge, tint):
    layer(ax, x + 4, y + 3, 17, 44, tint, edge, cells=8)
    layer(ax, x, y, 17, 44, tint, edge, cells=8)


def embedding_geometry(ax):
    anchor, positive, negative = (442, 64), (455, 70), (488, 49)
    line(ax, [anchor, positive], TEAL, 1.2)
    line(ax, [anchor, negative], AMBER, 0.9, "--")
    ax.plot(*anchor, "o", color=BLUE, ms=5)
    ax.plot(*positive, "s", color=TEAL, ms=4.8)
    ax.plot(*negative, "^", color=AMBER, ms=5.3)
    label(ax, 440, 58, r"$\mathbf{z}_i$", 8.8, BLUE, align="right")
    label(ax, 461, 71, r"$\mathbf{z}_i^+$", 8.8, TEAL)
    label(ax, 498, 49, r"$\mathbf{z}_i^-$", 8.8, AMBER)
    label(ax, 468, 31, "Contrastive loss", 8.2, TEAL, "bold", "center")
    label(ax, 468, 18, "Positive close to anchor", 7.2, MUTED, align="center")
    label(ax, 468, 8, "Fault view separated", 7.2, MUTED, align="center")


def draw_architecture():
    fig, ax = page(222)
    panel(ax, 6, 209, "(a) Shared spectral encoder", 273)
    panel(ax, 293, 209, "(b) Anchor reconstruction", 510)
    y = 155
    tokens(ax, 26, 133, BLUE, "#dce7f0")
    arrow(ax, (58, y), (99, y))
    feature_stack(ax, 104, 129, 47, 3, "#c6dbea", BLUE)
    arrow(ax, (142, y), (154, y))
    feature_stack(ax, 160, 134, 37, 4, "#c6dbea", BLUE)
    arrow(ax, (202, y), (232, y))
    layer(ax, 240, 141, 16, 27, "#9cbbd2", BLUE, cells=6)
    label(ax, 40, 116, "Spectral tokens", 8.5, BLUE, "bold", "center")
    label(ax, 40, 105, r"$101\times2$ (Re, Im)", 7.8, align="center")
    label(ax, 150, 116, "Two self-attention blocks", 8.4, BLUE, "bold", "center")
    label(ax, 150, 105, "Widths 64 and 128, 4 heads per block", 7.5, align="center")
    label(ax, 150, 94, "Input projection and position encoding", 7.3, MUTED, align="center")
    label(ax, 249, 185, "Mean pool + linear", 7.6, MUTED, align="center")
    label(ax, 250, 124, r"Latent $\mathbf{h}$", 8.5, BLUE, "bold", "center")
    label(ax, 250, 113, "128 features", 7.7, align="center")
    line(ax, [(260, y), (276, y)], BLUE, .9)
    arrow(ax, (276, y), (311, y), AMBER)
    feature_stack(ax, 316, 134, 37, 4, "#f2debd", AMBER)
    arrow(ax, (356, y), (370, y), AMBER)
    feature_stack(ax, 376, 130, 46, 3, "#f2debd", AMBER)
    arrow(ax, (414, y), (443, y), AMBER)
    tokens(ax, 450, 133, AMBER, "#f7e9d3")
    label(ax, 506, 190, "Healthy anchor only", 7.7, AMBER, align="right")
    label(ax, 364, 116, "Decoder blocks", 8.4, AMBER, "bold", "center")
    label(ax, 364, 105, "Widths 128 and 64", 7.6, align="center")
    label(ax, 461, 117, "Reconstruction", 8.3, AMBER, "bold", "center")
    label(ax, 461, 105, r"$101\times2$  /  MSE loss", 7.7, align="center")

    panel(ax, 293, 88, "(c) Contrastive projection", 510)
    line(ax, [(276, y), (276, 57)], TEAL, 0.9)
    ax.add_patch(Circle((276, y), 1.5, color=BLUE))
    arrow(ax, (276, 57), (298, 57), TEAL)
    layer(ax, 305, 43, 13, 26, "#cce5de", TEAL, cells=5)
    arrow(ax, (325, 57), (335, 57), TEAL)
    layer(ax, 340, 43, 13, 26, "#cce5de", TEAL, cells=5)
    arrow(ax, (359, 57), (375, 57), TEAL)
    layer(ax, 381, 44, 12, 24, "#9dcdbf", TEAL, cells=5)
    arrow(ax, (399, 57), (418, 57), TEAL)
    label(ax, 325, 31, "Projection head", 8.1, TEAL, "bold", "center")
    label(ax, 325, 19, r"Dense layers $2\times128$", 7.3, align="center")
    label(ax, 392, 32, r"$\mathbf{z}$ (128-D)", 8.1, TEAL, "bold", "center")
    label(ax, 392, 19, "Unit length", 7.5, align="center")
    embedding_geometry(ax)
    ax.add_patch(Rectangle((6, 17), 235, 49, edgecolor=RULE, facecolor=PANEL, lw=0.6))
    label(ax, 15, 54, "Inputs during training", 8.6, BLUE, "bold")
    label(ax, 17, 42, "Anchor, positive view, and synthetic fault share the encoder.", 7.05)
    label(ax, 17, 29, "At inference, the normalized embedding feeds the detector.", 7.05)
    save(fig, "fig03_carla_transformer_architecture")


if __name__ == "__main__":
    draw_overview()
    draw_architecture()
