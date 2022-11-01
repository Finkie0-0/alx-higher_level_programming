-- displays the top 3 cities' temperature
-- descending order
SELECT city, AVG(value) AS avg_temp
FROM tempearatures
WHERE month
BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

