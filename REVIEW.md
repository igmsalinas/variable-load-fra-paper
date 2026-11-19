# Variable-load manuscript reproducibility review

The audit used the [experiment code at 9e13ccd](https://github.com/igmsalinas/fault-converters-code/tree/9e13ccdd263346e2eadd15102fe096393a64d38a) and [data at 4950ecf](https://github.com/igmsalinas/fault-converters-data/tree/4950ecf604fab8b63395201b2d4a28af88fae8e8). Dataset 02 provides the main evidence. The fixed-load archive supplies the comparison in Figure 2 and Section VI-A.

## Verified results

| Scope | Evidence |
| --- | --- |
| Variable-load data | The manifest contains 800 unique sweeps with 101 finite magnitude and phase measurements on a shared logarithmic 100 Hz–50 kHz grid. Regenerating the sampling plan from seed 102 recovered the manifest. The 500 healthy and 300 faulty sweeps split into 300 healthy training sweeps, 100 healthy and 90 faulty fit-validation sweeps, and 100 healthy and 210 faulty test sweeps. All six saved split arrays matched an independent reconstruction. The code and data repositories contain the same sweeps, manifest and metadata after line-ending normalization. |
| Converter model | The Table I bounds now follow the sampled parameter multipliers. The central 95% of the healthy peak response spans 8.47 dB. Recomputing the complex relative response error gave a median of 0.09525% at the true simulated loads and 14.874% when evaluating the model at 4 Ω. Those calculations compare plant responses. A matched-load fault-augmentation error analysis would require paired healthy and faulty sweeps. |
| Variable-load detector | The saved configurations use one single-component negative per anchor, positive jitter and scaling, matched initial weights, and healthy validation for checkpoint selection and threshold calibration. The saved preprocessor uses one mean and standard deviation per Cartesian channel over all training sweeps and frequencies. The final ten-seed table gives F1 0.94166 ± 0.01284 and average precision 0.91257 ± 0.03077 at an assumed 5% prevalence. Test false positives ranged from 0 to 6 out of 100 healthy sweeps. Replaying all ten archived checkpoints on CPU with the raw sweeps, frozen split and saved preprocessor yielded F1 0.94254 ± 0.01238 and adjusted AP 0.91417 ± 0.03015. The paper reports the original run. Ranking metrics calculated from the intermediate score cache were also close to the final table, with per-seed absolute differences of at most 0.00072 in ROC AUC and 0.00112 in adjusted AP across the three methods stored in that cache. |
| Fixed-load comparison | All eleven archived per-state prediction tables share the same ordered 1,268 physical states and labels (520 healthy, 748 faulty). The five-fault comparison excludes 82 low-side-switch-only cases, leaving 520 healthy and 666 faulty. The fixed-load comparison in the manuscript uses the saved evaluation records. The raw cohort is needed to regenerate the fixed-load model-error distribution in Figure 2 and independently reconstruct the comparison in Section VI-A. |
| Source checks | The variable-load source audit passed. The Python suite passed all 175 tests in the available environment. |

## Figures and tables

| Material | Review and regeneration source |
| --- | --- |
| IEEE Figs. 1 and 3 | The vector diagrams describe spectral augmentation, scoring and the shared encoder with reconstruction and projection branches. If model selection changes, regenerate from the editable diagram source and check widths, projection dimensions, and the distinction between training and scoring. |
| IEEE Fig. 2 and Table I | The visible fault examples were matched to held-out sweeps and their measured severities. Regenerate from the raw sweeps and parameter manifest if examples, intervals or the converter model change. Rebuild the fixed-load panel after recovering the exact Dataset 01 cohort. |
| IEEE Fig. 4 and Table II | Regenerate from the final calibrated runs and the corresponding test labels and scores. Keep the assumed 5% prevalence in the adjusted PR curve and distinguish the representative curve from the across-seed legend. The PCA curve uses the retrospectively selected rank 10. |
| IEEE Fig. 5 | Use the archived PCA-rank and noise-sweep records. The noisy Transformer uses clean weights and recalculates its reference embeddings and threshold on perturbed inputs. The rank and noise sweeps use different noise draws. |

The manuscript presents the benchmark, paired ablation, fault-level recall, and noise sensitivity in one document. The detailed numerical records, encoder and scorer comparisons, learning curves, held-out-mode tests, and attention analysis remain in the experimental archive.

## Before journal submission

1. Record the original evaluation environment and replay the reported variable-load analyses with the frozen split, preprocessor and weights. Exact training reproducibility requires the corresponding historical source revisions and simulator configuration.
2. Recover the exact raw fixed-load Dataset 01 cohort, simulator inputs and sweep identities to replay the fixed-load comparisons. The legacy ZIP documents a separate 161,051-sweep grid.
3. Measure the nominal-load augmentation error on paired healthy and faulty samples at controlled loads. The current results apply to one simulated split. Independent splits, hardware frequency-response measurements and changed operating conditions require separate validation.
4. Verify access and selective Git LFS retrieval from clean checkouts of the cited artifact releases. Update the [availability statement](DATA_CODE_AVAILABILITY.md) and verify the author metadata and reference style against the target journal's requirements.
