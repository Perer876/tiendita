-- To set up the database
CREATE DATABASE IF NOT EXISTS tiendita;
CREATE USER IF NOT EXISTS 'app_conn'@'localhost' IDENTIFIED BY 'superstrongpassword123456';
GRANT ALL PRIVILEGES ON tiendita.* TO 'app_conn'@'localhost';
