-- sub query 

SELECT AVG(unit_price) FROM dim_product;
-- 495.790060

SELECT *
from dim_product
WHERE unit_price > 495.790060;

SELECT *
from dim_product
WHERE unit_price > (SELECT AVG(unit_price) FROM dim_product);

-- 2

SELECT 
	*
FROM 
	( SELECT *
from dim_product
WHERE unit_price > (SELECT AVG(unit_price) FROM dim_product)) AS sub_query
where 
	product_name = 'Figure Method';
    
    
    
--   CTE 
WITH cte_table AS(
	SELECT *
from dim_product
WHERE unit_price > (SELECT AVG(unit_price) FROM dim_product)),
cte_table_2 AS (
select *
FROM cte_table
where product_name IN( 'Figure Method','Huge Change','Film Finally'))
select * 
from cte_table_2
where product_name ='Figure Method';

