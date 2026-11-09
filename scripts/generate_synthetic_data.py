"""Generate a SYNTHETIC partner-pairing funnel dataset for the TwoSync A/B test demo.

All numbers here are simulated with a fixed seed. The treatment effect is planted so the
analysis scripts have something to detect. Nothing in this file is real user data.
"""
import numpy as np
import pandas as pd

SEED = 42
N_USERS = 6000

# Funnel step probabilities: (control, treatment)
P = {
    "invite_sent": (0.75, 0.85),
    "invite_opened": (0.65, 0.66),
    "partner_registered": (0.65, 0.66),
    "paired_d1": (0.96, 0.96),
}
UNINSTALL_D1 = (0.060, 0.062)  # guardrail

rng = np.random.default_rng(SEED)
variant = rng.choice(["control", "treatment"], size=N_USERS)
platform = rng.choice(["android", "ios"], size=N_USERS, p=[0.8, 0.2])
channel = rng.choice(["whatsapp", "sms", "link"], size=N_USERS, p=[0.55, 0.25, 0.20])
start = pd.Timestamp("2026-09-01")
registered_at = start + pd.to_timedelta(rng.integers(0, 14 * 24 * 60, N_USERS), unit="m")

idx = (variant == "treatment").astype(int)


def step(name, prev):
    p = np.where(idx == 1, P[name][1], P[name][0])
    return prev & (rng.random(N_USERS) < p)


sent = step("invite_sent", np.ones(N_USERS, bool))
opened = step("invite_opened", sent)
partner = step("partner_registered", opened)
paired = step("paired_d1", partner)
uninstall = rng.random(N_USERS) < np.where(idx == 1, UNINSTALL_D1[1], UNINSTALL_D1[0])

df = pd.DataFrame({
    "user_id": [f"u{100000 + i}" for i in range(N_USERS)],
    "variant": variant,
    "platform": platform,
    "invite_channel": channel,
    "registered_at": registered_at.strftime("%Y-%m-%d %H:%M:%S"),
    "invite_sent": sent.astype(int),
    "invite_opened": opened.astype(int),
    "partner_registered": partner.astype(int),
    "paired_d1": paired.astype(int),
    "uninstalled_d1": uninstall.astype(int),
})
df.to_csv("data/synthetic_pairing_funnel.csv", index=False)
print(df.shape)
print(df.groupby("variant")[["invite_sent", "invite_opened", "partner_registered", "paired_d1", "uninstalled_d1"]].mean().round(3))
