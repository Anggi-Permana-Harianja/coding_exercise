-- https://leetcode.com/problems/the-most-recent-three-orders/

WITH cte AS (
    SELECT
        c.name AS 'customer_name',
        c.customer_id AS 'customer_id',
        o.order_id AS 'order_id',
        o.order_date AS 'order_date',
        DENSE_RANK() OVER W AS 'rank'
    FROM Customers AS c
        INNER JOIN Orders AS o USING (customer_id)
    WINDOW W AS (PARTITION BY c.customer_id ORDER BY o.order_date DESC)
)

SELECT 
    cte.customer_name AS 'customer_name',
    cte.customer_id AS 'customer_id',
    cte.order_id AS 'order_id',
    cte.order_date AS 'order_date'
FROM cte
WHERE cte.rank <= 3
ORDER BY cte.customer_name, cte.customer_id, cte.order_date DESC