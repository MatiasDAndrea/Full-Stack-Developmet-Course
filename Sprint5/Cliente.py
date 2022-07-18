#######################################################
# Modulo: Cliente.py
#
#   Clases:
#       -Cliente()
#           -Classic()
#           -Gold()
#           -Black()
#       Se encarga de crear una cuenta en funcion
#       de los datos del cliente.
#
#   Funciones:
#       Empty
#
########################################################

from Cuenta import Cuenta
from Direccion import Direccion

class Cliente():
    def __init__(self, numero, nombre, apellido, dni, tipo, dir):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = Direccion(dir["calle"], dir["numero"], dir["ciudad"], dir["provincia"], dir["pais"])
        self.cuenta = Cuenta(tipo)
        self.puede_crear_chequera =  False
        self.puede_crear_tarjeta_credito = False
        self.puede_comprar_dolar = False

class Classic(Cliente):
    def __init__ (self, numero, nombre, apellido, dni, tipo, direccion):
        Cliente.__init__(self, numero, nombre, apellido, dni, tipo, direccion)
        self.puede_crear_chequera =  False
        self.puede_crear_tarjeta_credito = False
        self.puede_comprar_dolar = False        

class Gold (Cliente):
    def __init__(self, numero, nombre, apellido, dni, tipo, direccion):
        Cliente.__init__(self, numero, nombre, apellido, dni, tipo, direccion)
        self.puede_crear_chequera =  True
        self.puede_crear_tarjeta_credito = True
        self.puede_comprar_dolar = True

class Black (Cliente):
    def __init__(self, numero, nombre, apellido, dni, tipo, direccion):
        Cliente.__init__(self, numero, nombre, apellido, dni, tipo, direccion)
        self.puede_crear_chequera =  True
        self.puede_crear_tarjeta_credito = True
        self.puede_comprar_dolar = True

