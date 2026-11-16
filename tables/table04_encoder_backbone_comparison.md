**Table 4. 5-architecture encoder backbone comparison under identical `CARLA (SSA)` nominal-load physics training and strict zero-label `p97.5` calibration on `dataset_02` (5 paired seeds, mean ± SD; median in brackets for bimodal `GRU`).**

| Encoder Backbone | $\mathrm{F1}_{\mathrm{p97.5}}$ (Clean) | $\mathrm{PR\text{-}AUC}_{\pi=0.05}$ | $\mathrm{ROC\text{-}AUC}$ | $\mathrm{F1}_{\mathrm{p97.5}}$ ($0.15\,\mathrm{dB}$ FRA) | $\mathrm{ESR}_C$ Rec. | $\mathrm{ESR}_L$ Rec. | $R_{\mathrm{ds},1}$ Rec. |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Transformer` (Self-Attention)** | **0.9447 ± 0.0133** | **0.9195 ± 0.0283** | **0.9733 ± 0.0069** | **0.9303 ± 0.0087** | **90.0% ± 9.2%** | **94.3% ± 2.1%** | **38.9% ± 8.0%** |
| `LSTM` (Recurrent) | 0.8611 ± 0.0144 | 0.8053 ± 0.0100 | 0.9254 ± 0.0033 | 0.8557 ± 0.0165 | 84.3% ± 11.5% | 24.8% ± 4.0% | 7.4% ± 4.7% |
| `Conv1D` (Local Kernel) | 0.8426 ± 0.0238 | 0.7440 ± 0.0099 | 0.9188 ± 0.0083 | 0.7451 ± 0.0165 | 53.6% ± 13.4% | 50.5% ± 19.2% | 3.2% ± 4.7% |
| `MLP` (Dense Flattened) | 0.7739 ± 0.0210 | 0.7227 ± 0.0322 | 0.9095 ± 0.0118 | 0.7506 ± 0.0207 | 30.0% ± 10.6% | 17.1% ± 12.0% | 6.3% ± 6.9% |
| `GRU` (Gated Recurrent) | 0.5988 ± 0.3207 [0.8164] | 0.5147 ± 0.3052 [0.6958] | 0.7904 ± 0.1128 [0.8632] | 0.6021 ± 0.2965 [0.7910] | 60.7% ± 52.2% | 7.6% ± 5.4% | 3.2% ± 4.7% |
