-- Link: https://leetcode.com/problems/customer-order-frequency/
-- Hint:
--    - Pay attention how USING can simplify JOIN ... ON ... especially in multiple join case
--    - USING is used like JOIN ... ON ... when the joined column has same name

-- using USING
SELECT c.customer_id, c.name
FROM Orders JOIN Customers USING(customer_id)
    JOIN Product USING(product_id)
GROUP BY 1
HAVING SUM(IF(LEFT(order_date, 7) = '2020-06', quantity, 0) * price) >= 100
    AND SUM(IF(LEFT(order_date, 7) = '2020-07', quantity, 0) * price) >= 100
    
-- using JOIN ... ON ...
SELECT c.customer_id, c.name
FROM Orders AS o JOIN Customers AS c ON o.customer_id = c.customer_id
    JOIN Product AS p ON o.product_id = p.product_id
GROUP BY 1
HAVING SUM(IF(LEFT(o.order_date, 7) = '2020-06', quantity, 0) * o.price) >= 100
    AND SUM(IF(LEFT(o.order_date, 7) = '2020-07', quantity, 0) * o.price) >= 100