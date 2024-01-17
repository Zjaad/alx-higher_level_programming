-- show max temperature of states ordred by name.
SELECT state , MAX(value) AS max_temp
FROM temperatures GROUP BY state 
Order by state;
