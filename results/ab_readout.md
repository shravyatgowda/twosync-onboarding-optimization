# A/B readout (SYNTHETIC DATA)

| Metric | Control | Treatment | Diff (pts) | 95% CI (pts) | p-value | n control | n treatment |
|---|---|---|---|---|---|---|---|
| D1 pairing completion (primary) | 30.6% | 36.4% | +5.8 | [+3.4, +8.2] | 0.0000 | 3020 | 2980 |
| D1 uninstall (guardrail) | 5.4% | 6.4% | +1.0 | [-0.2, +2.2] | 0.0970 | 3020 | 2980 |

## Primary metric by platform

| Platform | Control | Treatment | Diff (pts) | p-value |
|---|---|---|---|---|
| android | 30.9% | 36.8% | +5.9 | 0.0000 |
| ios | 29.5% | 34.7% | +5.2 | 0.0577 |

## Funnel by variant

| Step | Control | Treatment |
|---|---|---|
| invite_sent | 74.8% | 85.4% |
| invite_opened | 47.7% | 56.5% |
| partner_registered | 31.9% | 38.0% |
| paired_d1 | 30.6% | 36.4% |

> Simulated data with a planted effect. This demonstrates the method, not a real result.
