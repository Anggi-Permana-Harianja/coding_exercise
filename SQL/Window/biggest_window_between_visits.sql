-- Link: https://leetcode.com/problems/biggest-window-between-visits/

--Hint:
-- LAG, LEAD can have default value
-- LAG, LEAD are windowing function so needs OVER

WITH cte AS (
    SELECT 
        user_id, 
        DATEDIFF(LEAD(visit_date, 1, '2021-01-01') OVER w, visit_date) AS date_diff
    FROM UserVisits
    WINDOW w AS (PARTITION BY user_id ORDER BY visit_date ASC)
)

SELECT 
    user_id, 
    MAX(date_diff) AS 'biggest_window'
FROM cte
GROUP BY 1
ORDER BY 1 ASC