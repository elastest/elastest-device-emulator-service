
-- initialise an MySQL database

CREATE USER "openmtc"@"localhost" IDENTIFIED BY "openmtc";
CREATE DATABASE openmtc_nscl;
GRANT ALL ON openmtc_nscl.* TO 'openmtc'@'localhost';

