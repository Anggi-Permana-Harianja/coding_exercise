--Link: https://platform.stratascratch.com/coding/9637-growth-of-airbnb?python

--Growth of Airbnb
--Estimate the growth of Airbnb each year using the number of hosts registered as the growth metric. The rate of growth is calculated by taking ((number of hosts registered in the current year - number of hosts registered in the previous year) / the number of hosts registered in the previous year) * 100.
--Output the year, number of hosts in the current year, number of hosts in the previous year, and the rate of growth. Round the rate of growth to the nearest percent and order the result in the ascending order based on the year.
--Assume that the dataset consists only of unique hosts, meaning there are no duplicate hosts listed.

WITH cte AS (
    SELECT EXTRACT(YEAR FROM host_since::DATE) AS curr_year,
        COUNT(id) AS curr_year_count
    FROM airbnb_search_details
    GROUP BY 1
    ORDER BY 1 ASC
)

SELECT curr_year AS current_year, curr_year - 1 AS previous_year,
    COALESCE(100 * curr_year_count - LAG(curr_year_count, 1) OVER w / LAG(curr_year_count, 1) OVER w, 0) AS growth_pct
FROM cte
WINDOW w AS (ORDER BY curr_year ASC)