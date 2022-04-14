-- Link: https://leetcode.com/problems/customer-order-frequency/

SELECT c.customer_id, c.name
FROM Orders JOIN Customers AS c USING(customer_id)
    JOIN Product USING(product_id)
GROUP BY 1
HAVING SUM(IF(LEFT(order_date, 7) = '2020-06', quantity, 0) * price) >= 100
    AND SUM(IF(LEFT(order_date, 7) = '2020-07', quantity, 0) * price) >= 100