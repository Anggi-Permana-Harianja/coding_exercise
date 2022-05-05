--Link: https://leetcode.com/problems/trips-and-users/
--This question is Uber like question

--Hint: Use SUM and IF altogether

SELECT request_at AS 'Day', 
    ROUND(SUM(IF(status LIKE '%cancel', 1, 0)) / COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips 
WHERE client_id IN (SELECT users_id FROM Users WHERE banned = 'No')
    AND driver_id IN (SELECT users_id FROM Users WHERE banned = 'No')
    AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 1 
ORDER BY 1 ASC