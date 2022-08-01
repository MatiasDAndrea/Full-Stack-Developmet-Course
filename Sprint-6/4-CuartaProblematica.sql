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

SELECT 
    COUNT(*) as Cantidad,
    branch_name as NombreSucursal
FROM Tarjetas T 
    INNER JOIN cliente C on T.customer_id = C.customer_id
    INNER JOIN sucursal S on S.branch_id = C.branch_id
WHERE Tarjeta_tipo = "CREDITO"
GROUP BY NombreSucursal
ORDER BY Cantidad;

-- 4 
SELECT 
    avg(loan_total) as PromedioPrestamos,
    branch_name as NombreSucursal
FROM cliente C
    INNER JOIN sucursal S on S.branch_id = C.branch_id  
    INNER JOIN prestamo P on P.customer_id = C.customer_id
GROUP BY NombreSucursal
ORDER BY PromedioPrestamos;

-- 5
--DROP TABLE IF EXISTS auditoria_cuenta;
CREATE TABLE IF NOT EXISTS auditoria_cuenta(
    old_id INTEGER NOT NULL,
    new_id INTEGER NOT NULL,
    old_balance INTEGER NOT NULL,
    new_balance INTEGER NOT NULL,
    old_iban TEXT NOT NULL,
    new_iban TEXT NOT NULL,
    old_type INTEGER NOT NULL,
    new_type INTEGER NOT NULL,
    user_action TEXT NOT NULL,
    created_at date NOT NULL
);

CREATE TRIGGER IF NOT EXISTS CHANGE 
    AFTER UPDATE 
    ON cuenta
    new.customer_id != old.customer_id 
BEGIN
    INSERT INTO auditoria_cuenta(
        old_id,
        new_id,
        old_balance,
        new_balance,
        old_iban,
        new_iban,
        old_type,
        new_type,
        user_action,
        created_at
    )
    VALUES(
        old.customer_id,
        new.customer_id,
        old.balance,
        new.balance,
        old.iban,
        new.iban,
        old.TCuenta_id,
        new.TCuenta_id,
        "Cambio de ID",
        date()
    )              
END;

UPDATE cuenta
set customer_id = 600 where account_id = 1;

select * from cuenta;

select * from auditoria_cuenta;


