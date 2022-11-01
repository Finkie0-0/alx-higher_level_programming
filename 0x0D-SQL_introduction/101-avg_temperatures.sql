-- Imports in hbtn_0c_0 
-- display the average temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

