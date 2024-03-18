# SQL - Introduction

**Level:** Novice  
**By:** Guillaume  
**Weight:** 1  
**Score:** Your score will be updated as you progress.

## Concepts
For this project, you should familiarize yourself with the following concept:
- Databases

## Resources
**Read or watch:**
- What is Database & SQL?
- Install MySQL (MySQL Server)
- A Basic MySQL Tutorial
- Basic SQL statements: DDL and DML (No need to read the chapter "Privileges")
- Basic queries: SQL and RA
- SQL technique: functions
- SQL technique: subqueries
- What makes the big difference between a backtick and an apostrophe?
- MySQL Cheat Sheet
- MySQL 8.0 SQL Statement Syntax

## Learning Objectives
By the end of this project, you should be able to explain, without the help of Google:

**General:**
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements
**General:**
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE...)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info
**Comments for your SQL file:**
```sql
-- 3 first students in Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

Install MySQL 8.0 on Ubuntu 20.04 LTS:

sudo apt update
sudo apt install mysql-server
mysql --version

Connect to your MySQL server:

sudo mysql

Use the sandbox to run MySQL:

In the container, credentials are root/root.
Ask for container Ubuntu 20.04.
Connect via SSH or the Web terminal.
Start MySQL before using it:
service mysql start
cat 0-list_databases.sql | mysql -uroot -p


This `README.md` provides a structured overview of the project, including learning objectives, resources, and setup instructions. Modify the links in the resources section to point to the actual content you wish the students to read or watch.