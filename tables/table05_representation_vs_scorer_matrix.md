**Table 5. Representation-versus-scorer control matrix on `dataset_02` (10 seeds, zero-label `p97.5` F1 and $\mathrm{PR\text{-}AUC}_{\pi=0.05}$).**

| Learned Representation (10 Seeds) | `k-NN (k=5)` $\mathrm{F1}_{\mathrm{p97.5}}$ | `Ledoit-Wolf` $\mathrm{F1}_{\mathrm{p97.5}}$ | `PCA (d=5)` $\mathrm{F1}_{\mathrm{p97.5}}$ | `PCA (d=10)` $\mathrm{F1}_{\mathrm{p97.5}}$ | `k-NN (k=5)` $\mathrm{PR\text{-}AUC}_{\pi=0.05}$ | `Ledoit-Wolf` $\mathrm{PR\text{-}AUC}_{\pi=0.05}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AE-Transformer` ($\mathbf{h}$, $w_c=0$) | 0.7090 ± 0.0067 | 0.7671 ± 0.0289 | 0.8293 ± 0.0597 | 0.9373 ± 0.0208 | 0.6129 ± 0.0053 | 0.6662 ± 0.0324 |
| `CARLA (Heuristic)` ($\mathbf{z}$) | 0.6868 ± 0.0281 | 0.8042 ± 0.0247 | 0.6674 ± 0.0606 | 0.7343 ± 0.0425 | 0.5271 ± 0.0530 | 0.6902 ± 0.0470 |
| **`CARLA (SSA)` Latent ($\mathbf{h}$)** | **0.9296 ± 0.0203** | **0.9421 ± 0.0037** | **0.9502 ± 0.0036** | **0.9204 ± 0.0188** | **0.8898 ± 0.0182** | **0.8620 ± 0.0064** |
| **`CARLA (SSA)` Projection ($\mathbf{z}$)** | **0.9415 ± 0.0125** | **0.9504 ± 0.0109** | **0.9351 ± 0.0129** | **0.9474 ± 0.0121** | **0.9126 ± 0.0304** | **0.9188 ± 0.0237** |
