CREATE DATABASE marmotta WITH      
    OWNER = postgres     
    ENCODING = 'UTF8'     
    LC_COLLATE = 'en_US.utf8'     
    LC_CTYPE = 'en_US.utf8'     
    TABLESPACE = pg_default     
    CONNECTION LIMIT = -1; 
GRANT ALL ON DATABASE marmotta TO postgres; 
 
GRANT TEMPORARY, CONNECT ON DATABASE marmotta TO PUBLIC; 