-- list number of records with the same score in second_table
-- display score and name of records
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;

