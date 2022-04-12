-- Link: https://platform.stratascratch.com/coding/2036-lowest-revenue-generated-restaurants

-- Lowest Revenue Generated Restaurants
-- Write a query that returns a list of the bottom 2% revenue generating restaurants.
-- Return a list of restaurant IDs and their total revenue from when customers placed orders in May 2020.

-- You can calculate the total revenue by summing the order_total column.
-- And you should calculate the bottom 2% by partitioning the total revenue into evenly distributed buckets.

WITH cte AS (
    SELECT restaurant_id, 
        SUM(order_total) AS revenue,
        NTILE(50) OVER w AS ntile_
    FROM doordash_delivery
    WHERE customer_placed_order_datetime BETWEEN '2020-05-01' AND '2020-05-31'
    GROUP BY 1
    WINDOW w AS (ORDER BY SUM(order_total) ASC)
)

SELECT restaurant_id, revenue FROM cte WHERE ntile_ = 1 ORDER BY 2 DESC