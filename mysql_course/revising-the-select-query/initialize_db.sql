#!/bin/bash

mysql -u root -ppassword << QUERY_INPUT

USE hackerrank;

CREATE TABLE city (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(17) NOT NULL,
    countrycode varchar(3) NOT NULL,
    district varchar(20) NOT NULL,
    population int NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO city (name, countrycode, district, population) 
VALUES
    ("Rotterdam", "NLD",  "Zuid-Holland",593321),
    ("Scottsdale", "USA", "Arizona", 202705),
    ("Corona", "USA", "California",124966),
    ("Concord", "USA", "California", 121780),
    ("Cedar Rapids", "USA", "Iowa", 120758),
    ("Coral Springs", "USA", "Florida", 117549),
    ("Fairfield", "USA", "California", 92256),
    ("Boulder", "USA", "Colorado", 91238),
    ("Fall River", "USA", "Massachusetts", 90555)
    ;



SELECT *
FROM city

QUERY_INPUT
