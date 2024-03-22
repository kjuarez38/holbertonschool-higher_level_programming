-- 7.cities.sql creates the database hbtn_0d_usa and the table cities
CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    `id` INT(11) DEFAULT UNIQUE NOT NULL AUTO_INCREMENT,
    `state_id` INT(11) NOT NULL FOREIGN KEY REFERENCES states(`id`),
    `name` VARCHAR(256) NOT NULL, 
    PRIMARY KEY (`id`)
);