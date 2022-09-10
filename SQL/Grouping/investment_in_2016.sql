-- Link: https://leetcode.com/problems/investments-in-2016/

WITH location AS (
    SELECT 
        lat,
        lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(1) = 1
),
investment AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(1) > 1
)

SELECT ROUND(SUM(tiv_2016), 2) AS 'tiv_2016'
FROM Insurance
WHERE 
    tiv_2015 IN (SELECT * FROM investment) AND
    lat IN (SELECT lat FROM location) AND
    lon IN (SELECT lon FROM location)