**Supplementary Table S2. Paired Transformer ablation on the variable-load benchmark over ten seeds.**

| Training and scoring | $\mathrm{F1}_{0.975}$ | $\mathrm{AP}_{0.05}$ | ROC AUC |
| --- | --- | --- | --- |
| Reconstruction error | 0.7540 ± 0.0111 | 0.6640 ± 0.0153 | 0.9033 ± 0.0129 |
| Reconstruction latent $k$-NN | 0.7090 ± 0.0067 | 0.6129 ± 0.0053 | 0.8190 ± 0.0114 |
| Heuristic negatives | 0.6868 ± 0.0281 | 0.5272 ± 0.0529 | 0.8344 ± 0.0224 |
| SSA negatives | 0.9417 ± 0.0128 | 0.9126 ± 0.0308 | 0.9740 ± 0.0064 |

**Recall at the 97.5th percentile (\%)**

| Training and scoring | Passive | $\mathrm{ESR}_C$ | $\mathrm{ESR}_L$ | $R_{\mathrm{ds},1}$ | $\Delta$F1 |
| --- | --- | --- | --- | --- | --- |
| Reconstruction error | 51.7 ± 2.0 | 13.2 ± 2.9 | 9.5 ± 6.3 | 3.2 ± 2.7 | $+0.1876$ |
| Reconstruction latent $k$-NN | 45.4 ± 0.7 | 3.6 ± 0.0 | 4.8 ± 0.0 | 1.1 ± 2.2 | $+0.2327$ |
| Heuristic negatives | 45.7 ± 3.8 | 17.1 ± 4.4 | 5.2 ± 3.5 | 6.8 ± 3.6 | $+0.2548$ |
| SSA negatives | 93.3 ± 2.2 | 89.6 ± 7.2 | 92.4 ± 4.0 | 36.3 ± 10.4 | — |

Values are mean $\pm$ SD. Passive recall pools the four passive single-fault strata. $\Delta$F1 is the mean paired improvement with SSA negatives. Each paired comparison gives $p=0.00195$ (unadjusted).
