-- Sorts and filters records in a database
-- lists all records with a score >= 10
SELECT score, name
    FROM second_table
    WHERE score >= 10
    ORDER BY score DESC;
