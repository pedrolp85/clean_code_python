# https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true




table_name: city, described bellow

+----+---------------+-------------+---------------+------------+
| id | name          | countrycode | district      | population |
+----+---------------+-------------+---------------+------------+
|  1 | Rotterdam     | NLD         | Zuid-Holland  |     593321 |
|  2 | Scottsdale    | USA         | Arizona       |     202705 |
|  3 | Corona        | USA         | California    |     124966 |
|  4 | Concord       | USA         | California    |     121780 |
|  5 | Cedar Rapids  | USA         | Iowa          |     120758 |
|  6 | Coral Springs | USA         | Florida       |     117549 |
|  7 | Fairfield     | USA         | California    |      92256 |
|  8 | Boulder       | USA         | Colorado      |      91238 |
|  9 | Fall River    | USA         | Massachusetts |      90555 |
+----+---------------+-------------+---------------+------------+


Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

mysql -uroot -ppassword -h127.0.0.1 -P3306

MySQL [hackerrank]> select * from city where countrycode = 'USA' and population > 100000;


Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

select name from city where countrycode = 'USA' and population > 120000;

Query all columns (attributes) for every row in the CITY table.
select * from city

Query all columns for a city in CITY with the ID 1661.
select * from city where id=1661;

