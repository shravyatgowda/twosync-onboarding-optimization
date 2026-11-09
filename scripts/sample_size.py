"""Sample size for a two-sided, two-proportion test (normal approximation).

Usage: python scripts/sample_size.py --baseline 0.30 --mde 0.04
"""
import argparse
from math import ceil
from statistics import NormalDist


def sample_size_per_arm(p1: float, p2: float, alpha: float = 0.05, power: float = 0.80) -> int:
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    z_b = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    num = (z_a * (2 * p_bar * (1 - p_bar)) ** 0.5 + z_b * (p1 * (1 - p1) + p2 * (1 - p2)) ** 0.5) ** 2
    return ceil(num / (p2 - p1) ** 2)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", type=float, default=0.30, help="control D1 pairing rate")
    ap.add_argument("--mde", type=float, default=0.04, help="absolute minimum detectable effect")
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--power", type=float, default=0.80)
    a = ap.parse_args()
    n = sample_size_per_arm(a.baseline, a.baseline + a.mde, a.alpha, a.power)
    print(f"Baseline {a.baseline:.1%}, MDE +{a.mde*100:.1f} pts, alpha {a.alpha}, power {a.power}")
    print(f"Required users per arm: {n:,}  (total {2*n:,})")
