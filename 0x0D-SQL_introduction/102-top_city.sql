-- display cities with the highest avg temperatures
SELECT `city`, AVG(`temperature`) AS `avg_temp`
FROM `temperatures`
WHERE MONTH(`date`) = 7 OR MONTH(`date`) = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
