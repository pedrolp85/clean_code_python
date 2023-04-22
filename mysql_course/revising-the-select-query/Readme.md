# https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true




table_name: city, described bellow

+----------+--------------+------+-----+-------------------+
| Field    | Type         | Null | Key | Default           |                       
+----------+--------------+------+-----+-------------------+
| id       | int          | NO   | PRI | NULL              |                             
| name     | varchar(17)  | NO   |     | NULL              |                             
| ctrycode | varchar(3)   | NO   |     |                   |                             
| district | varchar(20)  | YES  |     | NULL              |                             
|population| int          |      |     |                   |
+----------+--------------+------+-----+-------------------+

Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

mysql -uroot -ppassword -h127.0.0.1 -P3306

MySQL [hackerrank]> select * from city where countrycode = 'USA' and population > 100000;


Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

select name from city where countrycode = 'USA' and population > 120000;

Query all columns (attributes) for every row in the CITY table.
select * from city

Query all columns for a city in CITY with the ID 1661.
select * from city where id=1661;