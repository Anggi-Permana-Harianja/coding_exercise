-- Link: https://leetcode.com/problems/rank-scores/

SELECT 
    score AS 'score',
    DENSE_RANK() OVER w AS 'rank'
FROM Scores
WINDOW w AS (ORDER BY score DESC)
ORDER BY 2 ASC