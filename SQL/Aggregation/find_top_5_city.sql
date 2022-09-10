--Link:https://platform.stratascratch.com/coding/10148-find-the-top-10-cities-with-the-most-5-star-businesses?python=

--Find the top 5 cities with the most 5 star businesses

--Find the top 5 cities with the most 5 star businesses.
--Output the city name along with the number of 5-star businesses.
--Order records by the number of 5-star businesses in descending order.

SELECT 
    city, 
    COUNT(1) AS cnt
FROM yelp_business
WHERE stars = 5
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5