# Detecting Component Degradation Under Variable Load From Buck Converter Frequency Responses

IEEE journal manuscript on physics-informed anomaly detection from simulated buck converter frequency responses.

- [main.tex](main.tex) is the IEEE manuscript source, with six figures and two summary tables.
- `manuscript.md` is the Markdown edition.
- `references.bib` contains the bibliography.
- [supplement.tex](supplement.tex) contains the six detailed tables and the attention and score-sensitivity figure.
- The [figure source assets](figures) and [full tabular records](tables) also include assets used in earlier drafts.

Build the manuscript and supplement separately with the IEEEtran document class. The manuscript uses BibTeX. In Overleaf, select the corresponding primary document to build each PDF.

## Review and reproducibility

- [Cross-repository reproducibility review](REVIEW.md) records the verified results, manuscript corrections, and remaining gaps.
- [Experiment code](https://github.com/igmsalinas/fault-converters-code) hosts the training and evaluation code and the derived variable-load results.
- [Data and archived runs](https://github.com/igmsalinas/fault-converters-data) hosts the variable-load sweeps, split, checkpoints, and fixed-load evaluation records.
- [Data and code availability](DATA_CODE_AVAILABILITY.md) pins the audited snapshots and records the release requirements.

Figures 1 and 3 are vector schematics. Run `python3 figures/source/draw_method_figures.py` with Matplotlib and NumPy to regenerate their PDF and PNG versions.
