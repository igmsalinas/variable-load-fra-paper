**Table 6. Parametric FRA instrument-noise robustness sweep on `dataset_02` across seven polar jitter levels $(\sigma_{\mathrm{dB}},\, \sigma_{\mathrm{deg}} = 5\sigma_{\mathrm{dB}})$ under zero-label `p97.5` calibration.**

| Detector (Zero-Label `p97.5`) | $0.00\,\mathrm{dB}$ ($0.00^\circ$) | $0.05\,\mathrm{dB}$ ($0.25^\circ$) | $0.10\,\mathrm{dB}$ ($0.50^\circ$) | $0.15\,\mathrm{dB}$ ($0.75^\circ$) | $0.25\,\mathrm{dB}$ ($1.25^\circ$) | $0.40\,\mathrm{dB}$ ($2.00^\circ$) | $0.60\,\mathrm{dB}$ ($3.00^\circ$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`CARLA-Transformer (SSA)` (10 seeds)** | **0.9417 ± 0.0128** | **0.9414 ± 0.0117** | **0.9313 ± 0.0108** | **0.9160 ± 0.0138** | **0.9025 ± 0.0199** | **0.8304 ± 0.0375** | **0.7695 ± 0.0240** |
| `PCA Reconstruction (Oracle d=8)` | **0.9584** | 0.9417 | 0.8923 | 0.7967 | 0.6869 | 0.5245 | 0.4509 |
| `PCA Reconstruction (Oracle d=10)` | 0.9347 | 0.8682 | 0.7331 | 0.6478 | 0.5492 | 0.4328 | 0.3615 |
| `PCA (d=8, Re-fit on Noisy Train)` | 0.9584 | 0.9443 | 0.8951 | 0.8177 | 0.7337 | 0.6852 | 0.6770 |
| `Mahalanobis (Ledoit-Wolf)` | 0.8992 | 0.8783 | 0.8122 | 0.7240 | 0.6749 | 0.5646 | 0.4509 |
| `Raw k-NN (k=5)` | 0.7112 | 0.7112 | 0.7112 | 0.7112 | 0.7091 | 0.7073 | 0.6991 |

*On the primary matched 0.15 dB calibration realization (Fig. 7a), CARLA-Transformer (SSA) achieves F1 = 0.9284 ± 0.0154.*
