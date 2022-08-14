alter table Cliente 


insert into tarjetas(
    Tarjeta_Numero,
    Tarjeta_CVV,
    Tarjeta_Fecha_Otorgamiento,
    Tarjeta_Fecha_Expiracion,
    TTarjetas_id,
    Asignacion,
    Tarjeta_tipo,
    customer_id
)VALUES
("525725 4433349365","267","2016-06-03","2028-07-07",390,"1","CREDITO",1),
("455627 5447684867","361","2020-10-07","2030-06-12",209,"0","DEBITO",1),
("455624 4486527270","356","2016-01-18","2030-04-13",491,"1","DEBITO",2),
("542675 5838384746","288","2021-03-12","2030-01-04",235,"1","CREDITO",2),
("521255 3168574558","489","2020-02-28","2031-10-24",278,"0","CREDITO",3),
("453222 6666828353","523","2014-11-03","2029-04-29",101,"0","DEBITO",3)
;
UPDATE Tarjetas
SET    TTarjetas_id = 4
WHERE  Tarjetas_id = 6;

INSERT INTO TipoCuenta(
    TCuenta_tipo
)
VALUES
    ("Caja de ahorro en pesos"),
    ("Caja de ahorro en dólares"),
    ("Cuenta Corriente")
;

insert into Movimientos(
    NumCuenta,
    Monto,
    Tipo_Operacion,
    HORA
)VALUES
    (1,10000,"Transferencia Inmediata","03-01"),
    (1,10000,"Estacion YPF","03-01"),
    (1,10000,"MC Donalds","03-01"),
    (2,10000,"Transferencia Inmediata","03-01"),
    (2,10000,"Estacion YPF","03-01"),
    (2,10000,"MC Donalds","03-01"),
    (3,10000,"Transferencia Inmediata","03-01"),
    (3,10000,"Estacion YPF","03-01"),
    (3,10000,"MC Donalds","03-01")
;