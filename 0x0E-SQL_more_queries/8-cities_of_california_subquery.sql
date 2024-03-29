-- Lists all cities in the database hbtn_0d_usa
-- Results are ordered by ascending cities.id order
SELECT `id`, `name`
	FROM `cities`
	WHERE `state_id` IN
		(SELECT `id`
			FROM `states`
			WHERE `name` = "California")
ORDER BY `id`;
