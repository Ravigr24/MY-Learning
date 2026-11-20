-- Joins 

-- CREATE TABLE orders
-- (
-- 	o_Id INT,
--     cust_id INT,
--     price int
-- );
-- insert into orders
-- values
-- (1,101,1000),
-- (2,201,1100),
-- (3,501,1200);


-- Create Table customers
-- (
-- id INT,
-- name varchar(100),
-- email varchar(100));

-- insert into customers
-- values 
-- (101,'love', 'aa'),
-- (201, 'ansh','bb'),
-- (301,'lamba','cc')

---- inner join 

select *
from orders o
inner join customers c 
on o.cust_id = c.id;

--- left join

select *
from orders o
left join customers c 
on o.cust_id = c.id;


--- right join

select *
from orders o
right join customers c 
on o.cust_id = c.id;

--- full join (Not support )

select *
from orders o
full outer join customers c 
on o.cust_id = c.id;


--- Unions

select *
from orders o
left join customers c 
on o.cust_id = c.id 

union

select *
from orders o
right join customers c 
on o.cust_id = c.id;