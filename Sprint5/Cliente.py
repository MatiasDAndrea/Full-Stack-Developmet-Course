from Sprint5.Direccion import Direccion
from Cuenta import Cuenta
class Cliente():
    def __init__(self,numero,nombre,apellido,dni,tipo, Direccion):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.direccion = Direccion(tipo)
        self.cuenta = Cuenta(tipo)
        self.puede_crear_chequera =  False
        self.puede_crear_tarjeta_credito = False
        self.puede_comprar_dolar = False

class Classic(Cliente):
    def __init__ (self,id,name,sName,dni, Direccion):
        Cliente.__init__(self,id,name,sName,dni, "Classic", Direccion)
        self.puede_crear_chequera =  False
        self.puede_crear_tarjeta_credito = False
        self.puede_comprar_dolar = False        

class Gold (Cliente):
    def __init__(self, id, name, sName, dni,tipo, Direccion):
        Cliente.__init__(self,id,name,sName, dni, "Gold", Direccion)
        self.puede_crear_chequera =  True
        self.puede_crear_tarjeta_credito = True
        self.puede_comprar_dolar = True

class Black (Cliente):
    def __init__(self, id, name, sName, dni, Direccion):
        Cliente.__init__(self,id,name,sName, dni, Direccion)
        self.puede_crear_chequera =  True
        self.puede_crear_tarjeta_credito = True
        self.puede_comprar_dolar = True

