from Sprint5.Direccion import Direccion
from Cuenta import Cuenta
class Cliente():
    def __init__(self,numero,nombre,apellido,dni,tipo, direccion):
        self.numero = numero
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.direccion = Direccion(tipo)
        self.cuenta = Cuenta(tipo)
        self.puede_crear_chequera =  False
        self.puede_crear_tarjeta_credito = False
        self.puede_comprar_dolar = False

class Classic(Cliente):
    def __init__ (self,id,name,sName,dni):
        Cliente.__init__(self,id,name,sName,dni, "Classic")
        self.puede_crear_chequera =  False
        self.puede_crear_tarjeta_credito = False
        self.puede_comprar_dolar = False        

class Gold (Cliente):
    def __init__(self, id, name, sName, dni,tipo):
        Cliente.__init__(self,id,name,sName, dni, "Gold")
        self.puede_crear_chequera =  True
        self.puede_crear_tarjeta_credito = True
        self.puede_comprar_dolar = True

class Black (Cliente):
    def __init__(self, id, name, sName, dni):
        Cliente.__init__(self,id,name,sName, dni)
        self.puede_crear_chequera =  True
        self.puede_crear_tarjeta_credito = True
        self.puede_comprar_dolar = True

