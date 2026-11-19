**Leave-one-fault-out evaluation of the SSA-ratio Transformer over five seeds.**

| Omitted mode | $n$ | Held-out ROC AUC | Held-out recall (\%) | Included recall (\%) | Overall $\mathrm{F1}_{0.975}$ |
| --- | --- | --- | --- | --- | --- |
| $C_{\mathrm{out}}$ | 23 | 0.9989 ± 0.0008 [0.9991, 0.0009] | 99.1 ± 1.9 [100.0, 0.0] | 100.0 ± 0.0 | 0.9482 ± 0.0094 |
| $L_{\mathrm{out}}$ | 22 | 0.9911 ± 0.0027 [0.9905, 0.0014] | 93.6 ± 2.5 [95.5, 4.5] | 91.8 ± 2.0 | 0.9473 ± 0.0071 |
| $\mathrm{ESR}_C$ | 28 | 0.9715 ± 0.0525 [0.9939, 0.0079] | 82.9 ± 24.7 [92.9, 3.6] | 90.0 ± 9.2 | 0.9106 ± 0.0687 |
| $\mathrm{ESR}_L$ | 21 | 0.9470 ± 0.0717 [0.9705, 0.0214] | 75.2 ± 31.5 [90.5, 4.8] | 94.3 ± 2.1 | 0.9087 ± 0.0749 |
| $R_{\mathrm{ds},1}$ | 19 | 0.7466 ± 0.0563 [0.7684, 0.0442] | 30.5 ± 13.6 [31.6, 10.5] | 38.9 ± 8.0 | 0.9177 ± 0.0524 |

Values are mean $\pm$ SD, with [median, interquartile range] where indicated. Recall is measured at the healthy validation 97.5th percentile. Included recall is the reference obtained with all five modes in augmentation.
