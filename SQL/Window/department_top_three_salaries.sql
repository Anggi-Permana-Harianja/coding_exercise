-- https://leetcode.com/problems/department-top-three-salaries/

WITH cte AS 
(
    SELECT *,
        DENSE_RANK() OVER w AS row_num
    FROM Employee
    WINDOW w AS (PARTITION BY departmentID ORDER BY salary DESC)  
)

SELECT d.name AS 'Department', cte.name AS 'Employee', cte.salary AS 'Salary'
FROM cte INNER JOIN Department AS d
    ON cte.departmentId = d.id
WHERE cte.row_num <= 3