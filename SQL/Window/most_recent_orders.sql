-- https://leetcode.com/problems/the-most-recent-orders-for-each-product/

WITH cte AS (
    SELECT
        p.product_name AS 'product_name',
        p.product_id AS 'product_id',
        o.order_id AS 'order_id',
        o.order_date AS 'order_date', 
        DENSE_RANK() OVER W AS 'rank'
    FROM Products AS p
        INNER JOIN Orders AS o USING (product_id)
    WINDOW W AS (PARTITION BY p.product_name ORDER BY o.order_date DESC)
)

SELECT
    cte.product_name AS 'product_name',
    cte.product_id AS 'product_id',
    cte.order_id AS 'order_id',
    cte.order_date AS 'order_date'
FROM cte
WHERE cte.rank = 1
ORDER BY cte.product_name, cte.order_id DESC