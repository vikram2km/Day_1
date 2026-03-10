--Exercises
--Return numbers 1-20 sorted descending.
select generate_series(1,20) as series order by series desc;
--Return numbers 1-20 but only first 5 rows.
select generate_series(1,20) as series limit 5;
--Return numbers 1-20 but skip first 10 numbers and return next 5.
select generate_series(1,20) as series limit 5 offset 10;
--Show tables from pg_tables ordered by: schemaname , tablename.
select tablename from pg_tables order by schemaname , tablename ;

--Count how many numbers exist:generate_series(1,50)
select count(*) as count from generate_series(1,50);
--Find: SUM AVG MIN MAX for numbers 1-100.
select sum(series),avg(series),min(series),max(series) from generate_series(1,100) as series;
--Count how many tables exist in each schema.
select schemaname,count(tablename) as table_Count from pg_tables group by schemaname;
--Show schemas having more than 10 tables.
select schemaname,count(tablename) as table_Count from pg_tables group by schemaname having count(tablename)>10;


(SELECT generate_series(1,5) AS num)
UNION
(SELECT generate_series(1,5) as nums)
