-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS cv_me_test_db;
CREATE USER IF NOT EXISTS 'cv_me_test'@'localhost' IDENTIFIED BY 'cv_me_test_pswd';
GRANT ALL PRIVILEGES ON `cv_me_test_db`.* TO 'cv_me_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'cv_me_test'@'localhost';
FLUSH PRIVILEGES;
