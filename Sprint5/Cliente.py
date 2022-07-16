<<<<<<< HEAD
import Cuenta


class Cliente():
    def __init__(self,id,name,sName,dni,tipe):
        id=self.id
        name=self.name
        sName=self.sName
        dni=self.dni
        self.debitCard = 1
        tipe = tipe if tipe != None else 'Classic'
        self.Cuenta = Cuenta.Cuenta.__init__()
    def puede_crear_chequera():
        return bool
    def puede_crear_tarjeta_credito():
        return bool
    def puede_comprar_dolar():
        return bool

class Gold (Cliente):
    def __init__(self, id, name, sName, dni):
            Cliente.__init__(self,id,name,sName, dni)
            self.tipe= "GOLD"
            self.creditCard = 1
            self.dolarAccount= True
            self.debit= 20000
            self.cheq= True
            self.comission= 0.5
            self.maxTransf= 500000
=======
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
>>>>>>> 4931365f2686738f745c5ae9df9d0c5854220735

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

