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
DROP TABLE IF EXISTS auditoria_cuenta;
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

-- Trigger id --
CREATE TRIGGER IF NOT EXISTS CHANGE1
    AFTER UPDATE 
    ON cuenta
    WHEN OLD.customer_id <> NEW.customer_id
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
        "Modificacion del ID",
        date()
    );
END;

-- Trigger Balance --
CREATE TRIGGER IF NOT EXISTS CHANGE2
    AFTER UPDATE 
    ON cuenta
    WHEN OLD.balance <> NEW.balance
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
        "Modificacion del Balance",
        date()
    );
END;

-- Trigger IBAN --
CREATE TRIGGER IF NOT EXISTS CHANGE3
    AFTER UPDATE 
    ON cuenta
    WHEN OLD.iban <> NEW.iban
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
        "Modificacion del IBAN",
        date()
    );
END;

-- Trigger Tipo Cuento --
CREATE TRIGGER IF NOT EXISTS CHANGE4
    AFTER UPDATE 
    ON cuenta
    WHEN OLD.TCuenta_id <> NEW.TCuenta_id
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
        "Modificacion de Tipo de Cuenta",
        date()
    );
END;

-- Update de Datos en Cuenta --
UPDATE cuenta
SET balance = balance-100
WHERE account_id in (10,11,12,13,14);


-- Creacion de Indices ----------------------------------------
DROP INDEX IF EXISTS index_dni;
CREATE INDEX index_dni
ON  cliente(customer_DNI);

-- Tabla Movimientos ------------------------------------------
DROP TABLE IF EXISTS Movimientos;

-- Creacion de Tabla --
CREATE TABLE IF NOT EXISTS Movimientos(
    Cuenta_id INTEGER PRIMARY KEY,
    NumCuenta INTEGER NOT NULL,
    Monto INTEGER NOT NULL,
    Tipo_Operacion TEXT NOT NULL,
    HORA TEXT NOT NULL
);

-- Transaccion --------------------------------------------------

-- Trigger para Transacciones --
DROP TRIGGER IF EXISTS Trans;
CREATE TRIGGER IF NOT EXISTS Trans
    AFTER UPDATE 
    ON cuenta
    WHEN old.balance >= new.balance
BEGIN
    INSERT INTO Movimientos(
    NumCuenta,
    Monto,
    Tipo_Operacion,
    HORA
    )
    VALUES
        (
        new.account_id,
        old.balance - new.balance,
        "Transferencia",
        TIME()
    );
END;

-- Trigger para Depositos --
DROP TRIGGER IF EXISTS Depo;
CREATE TRIGGER IF NOT EXISTS Depo
    AFTER UPDATE 
    ON cuenta
    WHEN old.balance <= new.balance
BEGIN
    INSERT INTO Movimientos(
    NumCuenta,
    Monto,
    Tipo_Operacion,
    HORA
    )
    VALUES
        (
        new.account_id,
        new.balance - old.balance,
        "Deposito",
        TIME()
    );
END;

BEGIN TRANSACTION;
    UPDATE cuenta
        SET balance = balance-1000 WHERE account_id = 200;
        
    UPDATE cuenta 
        set balance = balance+1000 WHERE account_id = 400;

COMMIT;
