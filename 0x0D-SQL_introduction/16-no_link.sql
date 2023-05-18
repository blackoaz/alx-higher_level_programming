-- Lists all records of the table second_table having a name value
-- Records are ordered in descending order of score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
