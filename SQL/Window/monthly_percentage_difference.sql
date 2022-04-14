--Link: https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?python=

WITH cte AS (
    SELECT TO_CHAR(CAST(created_at AS DATE), 'YYYY-MM') AS year_month,
        SUM(value) AS curr_revenue,
        LAG(SUM(value), 1) OVER w AS prev_revenue
    FROM sf_transactions
    GROUP BY 1
    WINDOW w AS (ORDER BY TO_CHAR(CAST(created_at AS DATE), 'YYYY-MM'))
)

SELECT year_month, 
    ROUND(100 * (curr_revenue - prev_revenue) / prev_revenue, 2) AS pct_change
FROM cte
ORDER BY 1 ASC;