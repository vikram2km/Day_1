SELECT * FROM pg_tables LIMIT 10;

SELECT schemaname, tablename
FROM pg_tables
LIMIT 5;

SELECT tablename,
       LENGTH(tablename) AS name_length
FROM pg_tables
LIMIT 5;

SELECT 100 / 5 AS result;

SELECT tablename AS name
FROM pg_tables
ORDER BY name
LIMIT 5;