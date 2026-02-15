DROP DATABASE IF EXISTS test;
CREATE DATABASE test;

USE test;

CREATE TABLE cstocks(
    date VARCHAR(10) NOT NULL,
    open FLOAT(10) NOT NULL,
    high FLOAT(10) NOT NULL,
    low FLOAT(10) NOT NULL,
    close FLOAT(10) NOT NULL,
    volume INT(10) NOT NULL
);

SHOW TABLES;
