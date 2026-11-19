**Supplementary Table S1. Detection performance on the variable-load benchmark.**

**(a) Aggregate detection metrics**

| Detector | Use of fault labels | $\mathrm{F1}_{0.975}$ | $\mathrm{F1}_{0.95}$ | $\mathrm{AP}_{0.05}$ | ROC AUC |
| --- | --- | --- | --- | --- | --- |
| One-class SVM | None | 0.6892 | 0.6951 | 0.5434 | 0.7730 |
| Raw $k$-NN ($k=5$) | None | 0.7112 | 0.7087 | 0.6268 | 0.8716 |
| Mahalanobis (ridge) | None | 0.7638 | 0.8274 | 0.7086 | 0.9246 |
| Isolation forest | None | 0.8347 | 0.8962 | 0.7289 | 0.9293 |
| Mahalanobis (Ledoit–Wolf) | None | 0.8992 | 0.9196 | 0.7874 | 0.9582 |
| PCA (99\% variance, rank 4) | None | 0.7493 | 0.7608 | 0.6602 | 0.8993 |
| PCA (retrospective rank 10) | Rank selection | 0.9347 | 0.9453 | 0.8538 | 0.9703 |
| Transformer, SSA negatives | None | 0.9417 ± 0.0128 | 0.9433 ± 0.0095 | 0.9126 ± 0.0308 | 0.9740 ± 0.0064 |
| Supervised gradient boosting | Training (90 faults) | 0.9340 | — | 0.9322 | 0.9797 |

**(b) Recall by fault type at the 97.5th percentile (\%)**

| Detector | $C_{\mathrm{out}}$ | $\mathrm{ESR}_C$ | $L_{\mathrm{out}}$ | $\mathrm{ESR}_L$ | $R_{\mathrm{ds},1}$ | Compound |
| --- | --- | --- | --- | --- | --- | --- |
| One-class SVM | 91.3 | 3.6 | 90.9 | 4.8 | 0.0 | 71.1 |
| Raw $k$-NN ($k=5$) | 91.3 | 3.6 | 90.9 | 4.8 | 0.0 | 76.3 |
| Mahalanobis (ridge) | 91.3 | 21.4 | 90.9 | 4.8 | 5.3 | 84.5 |
| Isolation forest | 100.0 | 60.7 | 95.5 | 19.0 | 10.5 | 89.7 |
| Mahalanobis (Ledoit–Wolf) | 100.0 | 71.4 | 95.5 | 66.7 | 15.8 | 95.9 |
| PCA (99\% variance, rank 4) | 95.7 | 14.3 | 90.9 | 9.5 | 0.0 | 81.4 |
| PCA (retrospective rank 10) | 95.7 | 89.3 | 95.5 | 90.5 | 21.1 | 97.9 |
| Transformer, SSA negatives | 100.0 | 89.6 | 91.8 | 92.4 | 36.3 | 97.4 |
| Supervised gradient boosting | 87.0 | 100.0 | 90.9 | 81.0 | 15.8 | 99.0 |

Transformer values are means over ten runs. Panel (a) reports mean $\pm$ SD. The supervised F1 and recalls use its own decision rule.
