# TwoSync Onboarding Optimization

A product teardown, A/B test proposal, event schema and working prototype for the partner-pairing step of a couples app.

**Question:** how do we get more new users to pair with their partner on day 1?

> **Data disclaimer.** `data/synthetic_pairing_funnel.csv` is simulated (fixed seed, planted effect). It exists so the SQL and the analysis code can run end to end. The results it produces demonstrate the method and are not real product results.

## What is in here

| Path | What it is |
|---|---|
| `docs/01-teardown.md` | Funnel teardown and friction hypotheses |
| `docs/02-ab-test-proposal.md` | Hypothesis, metrics, guardrails, sample size, decision rule |
| `docs/03-event-schema.md` | Funnel events and daily validation checks |
| `events/posthog_event_schema.json` | Machine-readable PostHog event schema |
| `prototype/index.html` | Single-screen invite prototype. Open it in a browser; it logs each event as you tap |
| `sql/` | Funnel drop-off, A/B readout and channel breakdown queries (SQLite-compatible) |
| `scripts/` | Data generator, sample-size calculator, A/B readout, SQL runner |
| `results/ab_readout.md` | Output of the A/B readout on the synthetic data |

## Run it

```bash
pip install -r requirements.txt
python scripts/generate_synthetic_data.py   # creates data/synthetic_pairing_funnel.csv
python scripts/sample_size.py --baseline 0.30 --mde 0.04
python scripts/analyze_ab_test.py           # writes results/ab_readout.md
python scripts/run_sql.py                   # runs every query in sql/
```

Then open `prototype/index.html` in any browser.

## Reading the synthetic result

The treatment arm shows a higher D1 pairing rate with a confidence interval above zero. The uninstall guardrail rises by about 1 point and its confidence interval includes zero, which under the decision rule means "investigate before shipping" rather than "ship". That is deliberate: it shows how a guardrail changes the call.

## Tools

Python (pandas, numpy), SQL (SQLite), PostHog event design, HTML/CSS/JavaScript prototype.

## License

MIT. See `LICENSE`.
