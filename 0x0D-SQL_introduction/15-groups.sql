-- script for listing the number of records with the same score
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`i
GROUP BY `score`
ORDER BY `number` DESC;
