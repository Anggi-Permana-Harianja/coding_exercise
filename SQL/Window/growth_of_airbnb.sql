--Link: https://platform.stratascratch.com/coding/9637-growth-of-airbnb?python

WITH cte AS (
    SELECT 
        EXTRACT(YEAR FROM host_since::DATE) AS curr_year,
        COUNT(id) AS curr_year_count
    FROM airbnb_search_details
    GROUP BY 1
    ORDER BY 1 ASC
)

SELECT 
    curr_year AS current_year, 
    curr_year - 1 AS previous_year,
    COALESCE(100 * curr_year_count - LAG(curr_year_count, 1) OVER w / LAG(curr_year_count, 1) OVER w, 0) AS growth_pct
FROM cte
WINDOW w AS (ORDER BY curr_year ASC)