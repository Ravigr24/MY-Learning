--- TRANSFORMATIONS 

-- Numeric Transfermations
SELECT 
	unit_price * 0.90 AS discounted_price,
    unit_price + 10 AS taxed_price,
    unit_price / 10 AS fractioned_price,
    ROUND(unit_price ,1) AS rounded_price,
    unit_price * unit_price as multiplies_rice
from
	dim_product;
    
    
-- DATE Transfromations (IMP ****)

SELECT * from dim_date;
--- module 1

select
	date,
    now() as 'current_timestamp',
    utc_date(),
    utc_time(),
    utc_timestamp()
    from dim_date;


--  module 2

SELECT 
	date,
    YEAR(date),
    month(date),
    day(date),
    weekday(date),
    dayname(date),
    date(utc_timestamp()),
    datediff(date(utc_timestamp()),date) AS date_diff,
    adddate(date,2),
    subdate(date,2),
    cast('2026-01-01' AS datetime) 
from 
	dim_date;

-- module 3

select 
	date,
    date_format(date, '%W %M %e %Y') as converted_date
from
	dim_date;

 -- type casting
 
 select * from dim_customer;
 
 select
	customer_key,
    cast(customer_key as char(100))
from dim_customer; 
 

--- STRING functions

select * from dim_customer;



select
	*,
	concat(first_name,' ',last_name) AS full_name,
    concat_ws(' ',first_name,last_name,country,email),
    country,
    length(country) as country_size,
    lower(city) as city,
    upper(city),
    substring(email,1,6),
    replace(email,'@','%'),
    left(country,3),
    right(country,3),
    reverse(country),
    repeat(first_name,2) 
    
from 
	dim_customer;


