-- Link: https://leetcode.com/problems/tree-node/

SELECT 
    id, 
    CASE WHEN p_id IS NULL THEN 'Root'
         WHEN p_id IN (SELECT p_id FROM Tree) THEN 'Inner'
         ELSE 'Leaf' 
    END AS type
FROM Tree