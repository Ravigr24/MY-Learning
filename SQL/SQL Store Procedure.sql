--- Stored procedure 

DELIMITER //
CREATE procedure first_procedure(IN p_id INT,IN p_name char(100), IN email char(100))
BEGIN
	INSERT into customers
    values
    (p_id,p_name,email);
END//

DELIMITER ;

call ecom.first_procedure(10, 'blabla', 'kcmasknk');


-- views 

create view dedup_view AS 
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


