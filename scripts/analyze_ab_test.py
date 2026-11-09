"""Read out the synthetic A/B test: primary metric, guardrail, and a segment cut.

Primary metric : D1 partner-pairing completion rate (paired_d1 / users)
Guardrail      : D1 uninstall rate (must not rise by more than 1 pt)
Writes results/ab_readout.md
"""
from statistics import NormalDist

import pandas as pd

df = pd.read_csv("data/synthetic_pairing_funnel.csv")
nd = NormalDist()


def two_prop(a_succ, a_n, b_succ, b_n):
    p1, p2 = a_succ / a_n, b_succ / b_n
    diff = p2 - p1
    p_pool = (a_succ + b_succ) / (a_n + b_n)
    se_pool = (p_pool * (1 - p_pool) * (1 / a_n + 1 / b_n)) ** 0.5
    z = diff / se_pool
    p_val = 2 * (1 - nd.cdf(abs(z)))
    se = (p1 * (1 - p1) / a_n + p2 * (1 - p2) / b_n) ** 0.5
    return p1, p2, diff, diff - 1.96 * se, diff + 1.96 * se, p_val


def readout(frame, col):
    c = frame[frame.variant == "control"][col]
    t = frame[frame.variant == "treatment"][col]
    return two_prop(c.sum(), len(c), t.sum(), len(t)) + (len(c), len(t))


lines = ["# A/B readout (SYNTHETIC DATA)", ""]
lines.append("| Metric | Control | Treatment | Diff (pts) | 95% CI (pts) | p-value | n control | n treatment |")
lines.append("|---|---|---|---|---|---|---|---|")
for label, col in [("D1 pairing completion (primary)", "paired_d1"), ("D1 uninstall (guardrail)", "uninstalled_d1")]:
    p1, p2, d, lo, hi, pv, nc, nt = readout(df, col)
    lines.append(f"| {label} | {p1:.1%} | {p2:.1%} | {d*100:+.1f} | [{lo*100:+.1f}, {hi*100:+.1f}] | {pv:.4f} | {nc} | {nt} |")

lines += ["", "## Primary metric by platform", "", "| Platform | Control | Treatment | Diff (pts) | p-value |", "|---|---|---|---|---|"]
for plat, g in df.groupby("platform"):
    p1, p2, d, lo, hi, pv, nc, nt = readout(g, "paired_d1")
    lines.append(f"| {plat} | {p1:.1%} | {p2:.1%} | {d*100:+.1f} | {pv:.4f} |")

lines += ["", "## Funnel by variant", "", "| Step | Control | Treatment |", "|---|---|---|"]
for col in ["invite_sent", "invite_opened", "partner_registered", "paired_d1"]:
    c = df[df.variant == "control"][col].mean()
    t = df[df.variant == "treatment"][col].mean()
    lines.append(f"| {col} | {c:.1%} | {t:.1%} |")

lines += ["", "> Simulated data with a planted effect. This demonstrates the method, not a real result."]
open("results/ab_readout.md", "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
