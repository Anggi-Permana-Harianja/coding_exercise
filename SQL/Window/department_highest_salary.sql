--Link: https://leetcode.com/problems/department-highest-salary/

WITH rank_table AS (
    SELECT name, salary, departmentId,
        DENSE_RANK() OVER w as rank_
    FROM Employee
    WINDOW w AS (PARTITION BY departmentID ORDER BY salary DESC)
)

SELECT d.name AS 'Department',
    r.name AS 'Employee',
    r.salary AS 'Salary'
FROM Department AS d 
LEFT JOIN rank_table AS r 
    ON d.id = r.departmentId
WHERE r.rank_ = 1