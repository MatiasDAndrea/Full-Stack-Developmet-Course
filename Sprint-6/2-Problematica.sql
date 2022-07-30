DROP VIEW IF EXISTS VISTA;
CREATE TEMP VIEW IF NOT EXISTS VISTA 
    AS  SELECT 
        customer_id as ID,
        branch_id as NumeroSucursal,
        customer_name as Nombre,
        customer_surname as Apellido,
        customer_DNI as DNI,
        ROUND((JULIANDAY(date()) - JULIANDAY(dob))/365) as Edad
    FROM cliente
;  

SELECT * FROM VISTA WHERE Edad > 40 ORDER BY DNI ASC;
Select * FROM VISTA where Nombre = 'Anne' OR Nombre = 'Tyler';

INSERT INTO cliente (
    customer_name,
    customer_surname,
    customer_DNI,
    branch_id,
    dob
)
VALUES 
    ("Lois","Stout","47730534",80,"1984-07-07"),
    ("Hall","Mcconnell","52055464",45,"1968-04-30"),
    ("Hilel","Mclean","43625213",77,"1993-03-28"),
    ("Jin","Cooley","21207908",96,"1959-08-24"),
    ("Gabriel","Harmon","57063950",27,"1976-04-01")
;

UPDATE cliente set branch_id = 10
WHERE customer_id IN (select customer_id from cliente order by customer_id desc limit 5 );


DELETE FROM cliente
WHERE customer_name = "David" and customer_surname = "Noel";

SELECT loan_type FROM prestamo ORDER BY loan_total DESC LIMIT 1;
