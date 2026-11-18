# Detecting Component Degradation Under Variable Load From Buck Converter Frequency Responses

IEEE journal manuscript on physics-informed anomaly detection from simulated buck converter frequency responses.

- `main.tex` is the IEEE manuscript source.
- `manuscript.md` is the Markdown edition.
- `references.bib` contains the bibliography.
- `figures/` contains nine figures in vector PDF and 300 dpi PNG.
- `tables/` contains seven tables in LaTeX, Markdown, and CSV.

Build `main.tex` with the IEEEtran document class and BibTeX bibliography style. The repository can also be opened as an Overleaf project.

## Review and reproducibility

- [Manuscript review and figure verification](REVIEW.md)
- [GitHub and Git LFS availability template](DATA_CODE_AVAILABILITY.md)

Figures 1 and 3 are vector schematics. Run `python3 figures/source/draw_method_figures.py` with Matplotlib and NumPy to regenerate their PDF and PNG versions.
