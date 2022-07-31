--1

SELECT * FROM CLIENTE ;
SELECT * FROM sucursaL;
SELECT COUNT(*) as Cantidad,branch_name as NombreSucursal
FROM cliente C
    INNER JOIN sucursal S ON C.branch_id=S.branch_id
    GROUP BY branch_name order by Cantidad  desc;

--2

SELECT 
    COUNT(*) as CantidadEmpleados,
    customer_name||" "||customer_surname as NombreCliente,
    branch_name as NombreSucursal
from cliente C
    INNER JOIN sucursal S ON C.branch_id=S.branch_id
    INNER JOIN Empleado E ON S.branch_id=E.branch_id
    GROUP by NombreSucursal,NombreCliente ;

--3 
