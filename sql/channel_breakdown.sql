-- Which invite channel converts best, per variant? SQLite-compatible.
SELECT variant,
       invite_channel,
       COUNT(*)                                     AS users,
       ROUND(100.0 * AVG(CAST(paired_d1 AS INT)), 2) AS d1_pairing_pct
FROM funnel
GROUP BY variant, invite_channel
ORDER BY invite_channel, variant;
