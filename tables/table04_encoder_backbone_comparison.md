**Encoder comparisons with the same SSA-ratio augmentation on the variable-load benchmark.**

| Encoder | Clean $\mathrm{F1}_{0.975}$ | Noisy $\mathrm{F1}_{0.975}$ | $\mathrm{AP}_{0.05}$ | ROC AUC |
| --- | --- | --- | --- | --- |
| Transformer | 0.9447 ± 0.0133 | 0.9303 ± 0.0087 | 0.9195 ± 0.0283 | 0.9733 ± 0.0069 |
| LSTM | 0.8611 ± 0.0144 | 0.8557 ± 0.0165 | 0.8053 ± 0.0100 | 0.9254 ± 0.0033 |
| 1-D convolution | 0.8426 ± 0.0238 | 0.7451 ± 0.0165 | 0.7440 ± 0.0099 | 0.9188 ± 0.0083 |
| MLP | 0.7739 ± 0.0210 | 0.7506 ± 0.0207 | 0.7227 ± 0.0322 | 0.9095 ± 0.0118 |
| GRU | 0.5988 ± 0.3207 [0.8164] | 0.6021 ± 0.2965 [0.7910] | 0.5147 ± 0.3052 [0.6958] | 0.7904 ± 0.1128 [0.8632] |

**Clean recall at the 97.5th percentile (\%)**

| Encoder | $\mathrm{ESR}_C$ | $\mathrm{ESR}_L$ | $R_{\mathrm{ds},1}$ |
| --- | --- | --- | --- |
| Transformer | 90.0 ± 9.2 | 94.3 ± 2.1 | 38.9 ± 8.0 |
| LSTM | 84.3 ± 11.5 | 24.8 ± 4.0 | 7.4 ± 4.7 |
| 1-D convolution | 53.6 ± 13.4 | 50.5 ± 19.2 | 3.2 ± 4.7 |
| MLP | 30.0 ± 10.6 | 17.1 ± 12.0 | 6.3 ± 6.9 |
| GRU | 60.7 ± 52.2 | 7.6 ± 5.4 | 3.2 ± 4.7 |

Values are mean $\pm$ SD over five seeds. Brackets give the GRU medians. The noisy condition uses $0.15\,\mathrm{dB}$ magnitude and $0.75^\circ$ phase jitter.
