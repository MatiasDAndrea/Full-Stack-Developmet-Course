
-- 1
select * from cuenta where balance < 0;

-- 2
select 
    customer_name as Nombre, 
    customer_surname as Apellido,
    ROUND((JULIANDAY(date()) - JULIANDAY(dob))/365) as Edad
from cliente
where
    Apellido like "%Z%";

-- 3

select 
    customer_name as Nombre, 
    customer_surname as Apellido,
    ROUND((JULIANDAY(date()) - JULIANDAY(dob))/365) as Edad,
    S.branch_name as 'Nombre Sucursal'

from cliente C
    inner join sucursal S on C.branch_id = S.branch_id
WHERE
    customer_name LIKE "Brendan"
ORDER BY S.branch_name;

-- 4

Select * 
from prestamo P
where P.loan_total > 80000
Union
Select * 
from prestamo P2
where P2.loan_type = "PRENDARIO"
ORDER by loan_type;

-- 5

SELECT *
FROM prestamo
where loan_total > (select AVG(loan_total) from prestamo)
order by loan_total ASC;

-- 6

SELECT COUNT(*) as Cantidad
from cliente
where ROUND((JULIANDAY(date()) - JULIANDAY(dob))/365) < 50;

-- 7 

SELECT * 
from cuenta 
where balance > 8000
limit 5;

-- 8

select * from prestamo
where loan_date like "____-04-__"
    or loan_date like "____-06-__"
    or loan_date like "____-08-__"
order by loan_total;

-- 9

select sum(loan_total) as loan_total_accu, loan_type as type
from prestamo
group by loan_type;



