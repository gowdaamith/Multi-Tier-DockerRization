CREATE DATABASE IF NOT EXISTS employee_db;

USE employee_db;

CREATE TABLE IF NOT EXISTS employee (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) NOT NULL
);

INSERT INTO employee (name, salary)
VALUES
('Rahul', 50000),
('Priya', 60000),
('Amith', 70000);
