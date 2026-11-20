-- Realtime scenarios

-- sceanario 1 [finding the Nth value]

SELECT
	subquery.*
FROM (
SELECT 
	*,
    dense_rank() over (partition by category order by unit_price DESC) as ranking
FROM dim_product
) as subquery
where 
ranking = 3;

-- SCENARIO 2 [REMOVE DUPLICATE}
SELECT * from customers;

insert into customers
values 
(201,'ansh','bb'),
(301,'lamba','cc');


SELECT 
	subquery.*
FROM (
SELECT 
	*,
    ROW_NUMBER() over(partition by id order by id) as dedup
FROM 
	customers
    ) AS subquery
where dedup = 1 ; 


--- SCENARIO 3 [Lag & Lead]

CREATE TABLE weather
	( id INT,
    temp float
)
INSERT into weather
values
(1,10),
(2,12),
(3,9),
(4,15),
(5,20),
(6,15),
(7,12);


SELECT * from weather;

SELECT 
	*,
    lag(temp,1,0) over (order by id ASC) AS prev_day_temp,
    lag(temp,2,0) over (order by id ASC) AS prev_day_temp,
    lead(temp,1,0) over (order by id ASC) AS next_day_temp
FROM 
	weather