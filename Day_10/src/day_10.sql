/*Exercise 1
Create join of two series:*/
SELECT *
FROM generate_series(1,5) a
inner JOIN generate_series(3,7) b
ON a = b; 

/*Exercise 2
Join two tables but keep only numbers > 3 using WHERE.*/
SELECT *
FROM generate_series(1,5) a
inner JOIN generate_series(3,7) b
ON a = b  and a>3;

SELECT *
FROM generate_series(1,5) a
inner JOIN generate_series(3,7) b
ON a = b  where a>3;


/*Exercise 3
Create duplicate rows in one side and see join explosion.*/
SELECT *
FROM (
    SELECT generate_series AS n FROM generate_series(1,3)
    UNION ALL
    SELECT generate_series FROM generate_series(1,3)
) a
INNER JOIN generate_series(1,3) b(n)
ON a.n = b.n;

select * from chk;
inner join generate series(1,4) b 
on a=b;

SELECT *
FROM (SELECT 1 AS x UNION ALL SELECT 1 UNION ALL SELECT 1) a
JOIN (SELECT 1 AS x UNION ALL SELECT 1) b
ON a.x = b.x;

SELECT *
FROM generate_series(1,5) a
CROSS JOIN generate_series(1,4) b;

SELECT *
FROM (VALUES (1),(2),(NULL)) a(x)
join (values (1),(3),(NULL)) b(x)
on a.x=b.x


--Show difference between ON and WHERE.
select * from generate_series(1,5) a(x)
inner join generate_series(3,5) b(x)
on a.x=b.x;
select * from generate_series(1,5) a(x)
inner join generate_series(3,5) b(x)
on a.x=b.x where a.x>3;

--Create join explosion.
select * from (values (1),(1),(1)) a(x)
inner join (values (1),(2),(1)) b(x)
on a.x=b.x

--Create Cartesian join with (1,3) (1,4)
select * from generate_series(1,3) a(x)
cross join generate_series(1,4) b(x)

--Join with NULL values.
SELECT *
FROM (VALUES (1),(2),(NULL)) a(x)
join (values (1),(3),(NULL)) b(x)
on a.x=b.x

