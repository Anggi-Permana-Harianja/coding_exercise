--Link: https://leetcode.com/problems/second-highest-salary/submissions/

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee)