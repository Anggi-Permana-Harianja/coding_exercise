--Link: https://leetcode.com/problems/page-recommendations/

WITH user_table AS (
    SELECT 
        CASE WHEN user1_id = 1 THEN user2_id 
             WHEN user2_id = 1 THEN user1_id 
        END AS user_id
    FROM Friendship
)

SELECT DISTINCT page_id AS 'recommended_page'
FROM Likes AS l 
    INNER JOIN user_table AS ut ON l.user_id = ut.user_id
WHERE 
    ut.user_id IS NOT NULL AND
    ut.page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)