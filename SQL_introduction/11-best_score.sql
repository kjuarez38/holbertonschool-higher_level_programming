-- 11. Find the best score of each student.
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;