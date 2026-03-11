-- Lists all cities of California from the database hbtn_0d_usa.
-- Uses a subquery to find California's id, no JOIN.
-- Results sorted by cities.id in ascending order.
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
