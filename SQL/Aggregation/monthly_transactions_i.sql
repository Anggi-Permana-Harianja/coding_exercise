-- https://leetcode.com/problems/monthly-transactions-i/

SELECT
    LEFT(t.trans_date, 7) AS 'month',
    t.country AS 'country',
    COUNT(1) AS 'trans_count',
    SUM(t.state = 'approved') AS 'approved_count',
    SUM(t.amount) AS 'trans_total_amount',
    SUM(CASE
            WHEN t.state = 'approved' THEN t.amount
            ELSE 0
        END) AS 'approved_total_amount'
FROM Transactions AS t
GROUP BY month, t.country