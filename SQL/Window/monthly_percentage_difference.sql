--Link: https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?python=

--Monthly Percentage Difference
--Given a table of purchases by date, calculate the month-over-month percentage change in revenue. 
--The output should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd decimal point, and sorted from the beginning of the year to the end of the year.
--The percentage change column will be populated from the 2nd month forward and can be calculated as ((this month's revenue - last month's revenue) / last month's revenue)*100.


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