**Supplementary Table S4. Effects of representation and anomaly scoring on the variable-load benchmark.**

**$\mathrm{F1}_{0.975}$**

| Representation | $k$-NN | Ledoit–Wolf | PCA (rank 5) | PCA (rank 10) |
| --- | --- | --- | --- | --- |
| Reconstruction ($\mathbf h$) | 0.7090 ± 0.0067 | 0.7671 ± 0.0289 | 0.8293 ± 0.0597 | 0.9373 ± 0.0208 |
| Heuristic negatives ($\mathbf z$) | 0.6868 ± 0.0281 | 0.8042 ± 0.0247 | 0.6674 ± 0.0606 | 0.7343 ± 0.0425 |
| SSA negatives ($\mathbf h$) | 0.9296 ± 0.0203 | 0.9421 ± 0.0037 | 0.9502 ± 0.0036 | 0.9204 ± 0.0188 |
| SSA negatives ($\mathbf z$) | 0.9415 ± 0.0125 | 0.9504 ± 0.0109 | 0.9351 ± 0.0129 | 0.9474 ± 0.0121 |

**$\mathrm{AP}_{0.05}$**

| Representation | $k$-NN | Ledoit–Wolf |
| --- | --- | --- |
| Reconstruction ($\mathbf h$) | 0.6129 ± 0.0053 | 0.6662 ± 0.0324 |
| Heuristic negatives ($\mathbf z$) | 0.5271 ± 0.0530 | 0.6902 ± 0.0470 |
| SSA negatives ($\mathbf h$) | 0.8898 ± 0.0182 | 0.8620 ± 0.0064 |
| SSA negatives ($\mathbf z$) | 0.9126 ± 0.0304 | 0.9188 ± 0.0237 |

Values are mean $\pm$ SD over ten seeds. $\mathbf h$ denotes the encoder representation, and $\mathbf z$ denotes the normalized projection.
