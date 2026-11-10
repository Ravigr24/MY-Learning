--- conditonals

select * from dim_product;

-- 1
select
	*,
    case
    when unit_price <= 100 then 'affordable'
    when unit_price <= 200 then 'normal'
    else 'expensive (but not for you!)'
    end as price_category
from
	dim_product;
    

-- 2

select
	*,
    case
    when unit_price <= 100 and category = 'clothing' then 'affordable'
    when unit_price <= 200 and category = 'clothing' then 'normal'
    when unit_price > 200 and category = 'clothing' then 'expensive (but not for you!)'
    else concat('Not for ', category)
    end as price_category
from
	dim_product; 