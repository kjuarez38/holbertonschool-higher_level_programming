-- 15. List the number of records with the same score in the `second_table` table, ordered by the number of records in descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;