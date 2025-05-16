CREATE USER 'admin'@'localhost' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON dreadthreads.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;

CREATE USER 'admin'@'%' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON dreadthreads.* TO 'admin'@'%';
FLUSH PRIVILEGES;


CREATE DATABASE dreadthreads;
USE dreadthreads;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (name, email, password) VALUES ('test', 'testing@test.com', 'testpassword');

SELECT * FROM users;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    image_url VARCHAR(255)
);