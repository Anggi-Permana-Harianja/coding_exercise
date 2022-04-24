-- Link: https://leetcode.com/problems/tournament-winners/

--Hint:
---- using CASE WHEN
---- using INNER JOIN ... ON ... IN (...)

WITH score_table AS (
    SELECT player_id,
        SUM(CASE WHEN p.player_id = m.first_player THEN first_score 
                 ELSE second_score END) AS score
    FROM Players AS p INNER JOIN Matches m ON p.player_id IN (m.first_player, m.second_player)
    GROUP BY 1
),
rank_table AS (
    SELECT st.*, p.group_id,
        RANK() OVER(PARTITITON BY p.group_id ORDER BY st.score DESC, st.player_id ASC) AS rank_
    FROM score_table AS st INNER JOIN Players AS p On st.player_id = p.player_id
)

SELECT group_id AS 'GROUP_ID', player_id AS 'player_id'
FROM rank_table 
WHERE rank_ = 1