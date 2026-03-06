SELECT tablename
FROM pg_tables
WHERE schemaname = 'public';

SELECT tablename
FROM pg_tables
WHERE schemaname != 'pg_catalog';

SELECT tablename
FROM pg_tables
WHERE schemaname = 'public'
AND tablename LIKE 'pg%';

SELECT tablename
FROM pg_tables
WHERE schemaname = 'public'
OR schemaname = 'pg_catalog';

SELECT *
FROM generate_series(1,10) AS num
WHERE num BETWEEN 3 AND 7;

SELECT tablename
FROM pg_tables
WHERE schemaname like 'publi_';
SELECT tablename,schemaname
FROM pg_tables
WHERE schemaname like 'pu%';


--Exercises
--Show tables only from schema public
select tablename from pg_tables where schemaname='public';

--Return tables from either:public/pg_catalog
select tablename from pg_tables where schemaname in ('public','pg_catalog');

--Return tables starting with pg
select tablename from pg_tables where tablename like 'pg%';

--generate numbers and filter them
select * from generate_series(1,10) as series where series%2=0;

SELECT *
FROM generate_series(1,10) AS num
WHERE num % 2 = 0;


-----------------------------------------------------------------------------------------------


