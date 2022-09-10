-- Link: https://platform.stratascratch.com/coding/2036-lowest-revenue-generated-restaurants

WITH cte AS (
    SELECT 
        restaurant_id, 
        SUM(order_total) AS revenue,
        NTILE(50) OVER w AS ntile_
    FROM doordash_delivery
    WHERE customer_placed_order_datetime BETWEEN '2020-05-01' AND '2020-05-31'
    GROUP BY 1
    WINDOW w AS (ORDER BY SUM(order_total) ASC)
)

SELECT 
    restaurant_id, 
    revenue 
FROM cte 
WHERE ntile_ = 1 ORDER BY 2 DESC