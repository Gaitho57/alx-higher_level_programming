-- Lists number of records with same score in the table
-- displays score & the number of records with the score
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
