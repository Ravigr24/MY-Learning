-- FIRST SELECT 
select * from dim_customer;

SELECT customer_id,first_name, email, country  
from dim_customer
limit 15;


-- where [condtion]  clause
-- leavel 1
select * 
from dim_customer
where gender = 'F';

select * 
from dim_customer
where gender = 'm';

-- leavel 2 (AND/OR)
select * 
from dim_customer
where (gender = 'F') and (country = 'France') and (join_date> '2022-01-01');

select * 
from dim_customer
where (gender = 'F') and ( (country = 'France') OR (join_date> '2022-01-01'));

-- like topic
-- lv 1
select *
from dim_customer
where
	first_name LIKE 'T%';

-- lv 2
select *
from dim_customer
where
	first_name LIKE 'T%y';
    
select *
from dim_customer
where
	first_name LIKE 'T__f%y';
    
    
-- sorting

select * 
from dim_product
order by unit_price ASC;

select * 
from dim_product
order by unit_price DESC
LIMIT 3;


-- ALIAS
SELECT
	product_key,
    product_id,
    product_name AS 'Product name',
    category
from 
	dim_product;
    
    
-- GROUPING 
select * from dim_product;
-- Lv -1
select
	category,
    AVG(unit_price) AS AvgUnitPrice,
    SUM(unit_price) AS Totalprice
from dim_product
group by category;


-- lv 2
select
	category,
    AVG(unit_price) AS Avg_Price,
    SUM(unit_price) AS Total_price
from dim_product
group by category
HAVING Avg_Price > 500;

select
	category,
    AVG(unit_price) AS Avg_Price,
    SUM(unit_price) AS Total_price
from dim_product
group by category
HAVING Avg_Price > 500
order by Total_price DESC;
