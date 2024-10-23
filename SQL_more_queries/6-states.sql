-- script que crea una base de datos hbtn_0d_usa y la tabla states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);