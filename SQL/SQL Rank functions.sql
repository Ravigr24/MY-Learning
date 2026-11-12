-- window functions

select * from dim_product;
select 
	avg(unit_price)
from 
    dim_product;
    
select
	*,
	avg(unit_price) over (order by launch_date)
from 
    dim_product;
    
--- frames clause

select
	*,
	sum(unit_price) over (order by launch_date ROWS BETWEEN unbounded preceding AND current row)
from 
    dim_product;
    
select
	*,
	sum(unit_price) over (order by launch_date ROWS BETWEEN unbounded preceding AND unbounded following )
from 
    dim_product;    
    
    
--- Rank funtions 

select 
	unit_price,
    category,
    row_number() over (partition by category order by unit_price) as 'row_number',
    rank() over (partition by category order by unit_price) as 'rank',
    dense_rank() over (partition by category order by unit_price) as 'dense_rank'
from
	dim_product;
    