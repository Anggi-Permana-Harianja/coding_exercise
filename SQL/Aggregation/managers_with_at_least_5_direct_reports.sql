-- Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

WITH manager AS (
    SELECT managerId
    FROM Employee
    GROUP BY 1
    HAVING COUNT(1) >= 5
)

SELECT e.name AS 'name'
FROM Employee AS e LEFT JOIN manager AS m on e.id = m.managerId
WHERE e.id = m.managerId