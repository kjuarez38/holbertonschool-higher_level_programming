-- 0.privileges.sql lists all privileges of user_0d_1 and user_0d_2 on your server (in localhost)
SELECT * FROM mysql.user WHERE User='user_0d_1' AND Host='localhost';
SELECT * FROM mysql.user WHERE User='user_0d_2' AND Host='localhost';