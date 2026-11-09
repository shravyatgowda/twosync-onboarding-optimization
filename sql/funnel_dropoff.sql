-- Step-by-step funnel with drop-off, by variant. SQLite-compatible.
-- Load the CSV first: sqlite3 :memory: ".mode csv" ".import data/synthetic_pairing_funnel.csv funnel"
WITH totals AS (
  SELECT variant,
         COUNT(*)                      AS registered,
         SUM(CAST(invite_sent AS INT))        AS invite_sent,
         SUM(CAST(invite_opened AS INT))      AS invite_opened,
         SUM(CAST(partner_registered AS INT)) AS partner_registered,
         SUM(CAST(paired_d1 AS INT))          AS paired_d1
  FROM funnel
  GROUP BY variant
)
SELECT variant,
       registered,
       invite_sent,
       ROUND(100.0 * invite_sent / registered, 1)            AS pct_sent,
       ROUND(100.0 * invite_opened / invite_sent, 1)         AS pct_opened_of_sent,
       ROUND(100.0 * partner_registered / invite_opened, 1)  AS pct_registered_of_opened,
       ROUND(100.0 * paired_d1 / partner_registered, 1)      AS pct_paired_of_registered,
       ROUND(100.0 * paired_d1 / registered, 1)              AS pct_paired_overall
FROM totals
ORDER BY variant;
