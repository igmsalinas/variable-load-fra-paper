# Detecting Component Degradation Under Variable Load From Buck Converter Frequency Responses

IEEE journal manuscript on physics-informed anomaly detection from simulated buck converter frequency responses.

- [main.tex](main.tex) is the IEEE manuscript source, with five figures and two tables.
- `manuscript.md` is the Markdown edition.
- `references.bib` contains the bibliography.
- The [figure source assets](figures) and [full tabular records](tables) also include assets used in earlier drafts.

Build the manuscript with the IEEEtran document class and BibTeX. The LaTeX source is also ready to build in Overleaf.

## Review and reproducibility

- [Cross-repository reproducibility review](REVIEW.md) records the verified results, manuscript corrections, and remaining gaps.
- [Experiment code](https://github.com/igmsalinas/fault-converters-code) hosts the training and evaluation code and the derived variable-load results.
- [Data and archived runs](https://github.com/igmsalinas/fault-converters-data) hosts the variable-load sweeps, split, checkpoints, and fixed-load evaluation records.
- [Data and code availability](DATA_CODE_AVAILABILITY.md) pins the audited snapshots and records the release requirements.

Figures 1 and 3 are vector schematics. Run `python3 figures/source/draw_method_figures.py` with Matplotlib and NumPy to regenerate their PDF and PNG versions.
