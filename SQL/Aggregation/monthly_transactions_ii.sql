-- https://leetcode.com/problems/monthly-transactions-ii/

-- Hint
--   - Use UNION ALL to unionize approved and chargebacks
--   - If it is just a one branch condition, use IF instead CASE WHEN for simplicity
--   - For simplicity, we can use column number for GROUP BY and ORDER BY instead use column name

WITH cte AS (
    SELECT
        t.id AS 'id',
        t.country AS 'country',
        t.state AS 'state',
        t.amount AS 'amount',
        LEFT(t.trans_date, 7) AS 'trans_date'
    FROM Transactions AS t
    WHERE t.state = 'approved'
    
    UNION ALL
    
    SELECT
        c.trans_id AS 'id',
        t.country AS 'country',
        'chargeback' AS 'state',
        LEFT(c.trans_date, 7) AS 'trans_date'
    FROM Chargebacks AS c
        INNER JOIN Transactions AS t ON c.trans_id = t.id
)

SELECT
    LEFT(cte.trans_date) AS 'month',
    cte.country AS 'country',
    SUM(IF(cte.state = 'approved', 1, 0)) AS 'approved_count',
    SUM(IF(cte.state = 'approved', cte.amount, 0)) AS 'approved_amount',
    SUM(IF(cte.state = 'chargebacks', 1, 0)) AS 'chargebacks_count',
    SUM(IF(cte.state = 'chargebacks', cte.amount, 0)) AS 'chargebacks_amount'
GROUP BY 1, 2
ORDER BY 1, 2