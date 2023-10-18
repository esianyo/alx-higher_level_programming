-- Lists the number of records with the same scores in the table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;