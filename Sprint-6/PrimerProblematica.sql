------ Clientes -----------------------------------------------
-- Tabla que contiene los tipos de Clientes segun consigna.
DROP TABLE IF EXISTS TipoCliente;

-- Creacion de Tabla --
CREATE TABLE IF NOT EXISTS TipoCliente(
    TCliente_id INTEGER PRIMARY KEY,
    TCliente_tipo TEXT NOT NULL,
    TCliente_descubrimiento INTEGER NOT NULL,
    TCliente_creditoLim INTEGER NOT NULL,
    TCliente_chequeraLim INTEGER NOT NULL,
    TCliente_Comision INTEGER NOT NULL,
    TCliente_Limite_Transferencia TEXT NOT NULL,
    TCliente_Crear_Tarjeta TEXT NOT NULL,
    TCliente_Crear_Chequera TEXT NOT NULL,
    TCliente_Comprar_Dolar TEXT NOT NULL,
    TCliente_Limite_Extraccion INTEGER NOT NULL
);

-- Inserto Valores --
INSERT INTO TipoCliente (
    TCliente_tipo,
    TCliente_descubrimiento,
    TCliente_creditoLim,
    TCliente_chequeraLim,
    TCliente_Comision,
    TCliente_Limite_Transferencia,
    TCliente_Crear_Tarjeta,
    TCliente_Crear_Chequera,
    TCliente_Comprar_Dolar,
    TCliente_Limite_Extraccion
)
VALUES 
    ("CLASSIC",0,0,0,1,"150000","FALSE","FALSE","FALSE",10000),
    ("GOLD",10000,1,1,0.5,"500000","TRUE","TRUE","TRUE",20000),
    ("BLACK",10000,5,2,0,"INF","TRUE","TRUE","TRUE",100000)
;

------ Cuenta --------------------------------------------------
-- Tabla que contiene los tipos de cuenta
DROP TABLE IF EXISTS TipoCuenta;

-- Creacion de Tabla --
CREATE TABLE IF NOT EXISTS TipoCuenta(
    TCuenta_id INTEGER PRIMARY KEY,
    TCuenta_tipo TEXT NOT NULL
);

-- Inserto Valores --
INSERT INTO TipoCuenta(
    TCuenta_tipo
)
VALUES
    ("Caja de ahorro en pesos"),
    ("Caja de ahorro en dólares"),
    ("Cuenta Corriente")
;

------ Marcas Tarjetas ----------------------------------------
-- Tabla que contiene los tipos de tarjetas
DROP TABLE IF EXISTS MarcasTarjetas;

-- Creacion de Tabla -- 
CREATE TABLE IF NOT EXISTS MarcasTarjetas(
    TTarjetas_id INTEGER PRIMARY KEY,
    TTarjetas_Marca TEXT NOT NULL
);

-- Inserto Valores --
INSERT INTO MarcasTarjetas(
    TTarjetas_Marca
)
VALUES 
    ("Master Card"),
    ("Brue Bank"),
    ("REBA Bank"),
    ("VISA")
;

------ Tarjetas -----------------------------------------------
-- Tabla que contiene un conjunto de tarjetas junto con 
--    sus atributos.
DROP TABLE IF EXISTS Tarjetas;

-- Creacion de Tabla --
CREATE TABLE IF NOT EXISTS Tarjetas(
    Tarjetas_id INTEGER PRIMARY KEY,
    Tarjeta_Numero TEXT UNIQUE NOT NULL CHECK(length(Tarjeta_Numero)<=20),
    Tarjeta_CVV INTEGER NOT NULL,
    Tarjeta_Fecha_Otorgamiento TEXT NOT NULL,
    Tarjeta_Fecha_Expiracion TEXT NOT NULL,
    Tarjeta_tipo TEXT NOT NULL CHECK (Tarjeta_tipo in ("CREDITO","DEBITO")),
    TTarjetas_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,

    FOREIGN KEY (TTarjetas_id) REFERENCES MarcasTarjetas(TTarjetas_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (customer_id) REFERENCES cliente(customer_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Inserto Valores --
INSERT INTO Tarjetas(
    Tarjeta_Numero,
    Tarjeta_CVV,
    Tarjeta_Fecha_Otorgamiento,
    Tarjeta_Fecha_Expiracion,
    Tarjeta_tipo,
    TTarjetas_id,
    customer_id
)
VALUES 
    ("1234116",1,"ASD","ASD","CREDITO",20,2546)
;












