-- shows all the cities of California that can be found in DB
USE hbtn_0d_usa;

SELECT * FROM cities 
	WHERE state_id = (SELECT id FROM states 
		WHERE name = 'California');
