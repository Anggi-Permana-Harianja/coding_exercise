-- https://leetcode.com/problems/group-sold-products-by-the-date/

-- Hint:
--   - Use GROUP_CONCAT to concat values in same group

SELECT sell_date AS 'sell_date', 
    COUNT(DISTINCT product) AS 'num_sold',
    GROUP_CONCAT(DISTINCT product) AS 'products'
FROM Activities
GROUP BY 1
ORDER BY 1 ASC