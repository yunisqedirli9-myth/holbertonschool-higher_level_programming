-- verfy null
SELECT score,name
FROM second_table
WHERE name is not null
ORDER BY score DESC
