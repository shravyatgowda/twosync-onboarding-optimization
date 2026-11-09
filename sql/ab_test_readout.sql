-- Primary metric and guardrail by variant and platform. SQLite-compatible.
SELECT variant,
       platform,
       COUNT(*)                                          AS users,
       ROUND(100.0 * AVG(CAST(paired_d1 AS INT)), 2)     AS d1_pairing_pct,
       ROUND(100.0 * AVG(CAST(uninstalled_d1 AS INT)), 2) AS d1_uninstall_pct
FROM funnel
GROUP BY variant, platform
ORDER BY platform, variant;
