**Table 3. 10-seed paired ablation of objective formulation and negative-sampling physics on `dataset_02` under identical `Transformer` backbones and strict zero-label `p97.5` calibration ($p_{\min} = 0.00195$ for $n=10$).**

| Training & Scoring Regime | $\mathrm{F1}_{\mathrm{p97.5}}$ | $\mathrm{PR\text{-}AUC}_{\pi=0.05}$ | $\mathrm{ROC\text{-}AUC}$ | Passive Single Rec. | $\mathrm{ESR}_C$ Rec. | $\mathrm{ESR}_L$ Rec. | $R_{\mathrm{ds},1}$ Rec. | Paired $\Delta\mathrm{F1}$ ($p$-value) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `AE-Transformer (MSE, w_c=0)` | 0.7540 ± 0.0111 | 0.6640 ± 0.0153 | 0.9033 ± 0.0129 | 51.7% ± 2.0% | 13.2% ± 2.9% | 9.5% ± 6.3% | 3.2% ± 2.7% | $+0.1876$ ($p = 0.00195$) |
| `AE-Transformer (Latent kNN5)` | 0.7090 ± 0.0067 | 0.6129 ± 0.0053 | 0.8190 ± 0.0114 | 45.4% ± 0.7% | 3.6% ± 0.0% | 4.8% ± 0.0% | 1.1% ± 2.2% | $+0.2327$ ($p = 0.00195$) |
| `CARLA-Transformer (Heuristic)` | 0.6868 ± 0.0281 | 0.5272 ± 0.0529 | 0.8344 ± 0.0224 | 45.7% ± 3.8% | 17.1% ± 4.4% | 5.2% ± 3.5% | 6.8% ± 3.6% | $+0.2548$ ($p = 0.00195$) |
| **`CARLA-Transformer (SSA)`** | **0.9417 ± 0.0128** | **0.9126 ± 0.0308** | **0.9740 ± 0.0064** | **93.3% ± 2.2%** | **89.6% ± 7.2%** | **92.4% ± 4.0%** | **36.3% ± 10.4%** | — |
