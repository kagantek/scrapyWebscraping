CREATE DATABASE db;
USE db;
CREATE TABLE IF NOT EXISTS petlebi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_url VARCHAR(255),
    product_name VARCHAR(255),
    product_price VARCHAR(50),
    product_id VARCHAR(50),
    product_img VARCHAR(1000),
    barcode VARCHAR(50),
    brand VARCHAR(255),
    description TEXT
);