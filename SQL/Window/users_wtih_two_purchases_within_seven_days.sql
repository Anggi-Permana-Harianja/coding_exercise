-- Link: https://leetcode.com/problems/users-with-two-purchases-within-seven-days/

WITH cte AS (
    SELECT user_id, 
        DATEDIFF(LEAD(purchase_date, 1) OVER w, purchase_date) AS date_diff
    FROM Purchases
    WINDOW w AS (PARTITION BY user_id ORDER BY purchase_date ASC)
)

SELECT DISTINCT user_id FROM cte WHERE date_diff <= 7