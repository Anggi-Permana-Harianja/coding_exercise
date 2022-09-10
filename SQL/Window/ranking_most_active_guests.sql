-- Link: https://platform.stratascratch.com/coding/10159-ranking-most-active-guests?python=

SELECT 
    DENSE_RANK() OVER w AS dense_rank,
    id_guest, SUM(n_messages) AS cnt
FROM airbnb_contacts
GROUP BY 2
WINDOW w AS (ORDER BY SUM(n_messages) DESC)
ORDER BY 3 DESC