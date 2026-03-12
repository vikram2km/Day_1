--Return unique schema names from pg_tables.
--Return unique numbers from generate_series(1,5) UNION ALL generate_series(1,5)
--Return unique pairs: schemaname, tablename from pg_tables.
--Find schemas having duplicate rows using GROUP BY.

select distinct(schemaname) as unq_schemaname from pg_tables;
select distinct(series_numbers) as unq_numbers from (select generate_series(1,5) UNION ALL select generate_series(1,5)) as series_numbers;
select schemaname,tablename from pg_tables group by 1,2;
--UNION ALL will keep duplicates while UNION will remove duplicates
select schemaname,count(schemaname) as schema_count from pg_tables group by 1 having count(schemaname)>1;