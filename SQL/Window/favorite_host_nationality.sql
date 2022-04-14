--Link: https://platform.stratascratch.com/coding/10073-favorite-host-nationality?python=

WITH cte AS (
    SELECT ar.from_user AS user_id, ar.to_user, ar.review_store, 
        ah.nationality AS nationality,
        RANK() OVER w AS rank_
    FROM airbnb_reviews AS ar
    LEFT JOIN airbnb_hosts AS ah ON ar.to_user = ah.host_id
    WHERE from_type = 'guest'
    WINDOW w AS (PARTITION BY ar.from_user ORDER BY ar.review_score DESC)
)

SELECT DISTINCT user_id, nationality FROM cte WHERE rank_ = 1