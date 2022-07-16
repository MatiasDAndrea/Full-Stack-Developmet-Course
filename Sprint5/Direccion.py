###########################################
#   Modulo: Direccion.py
#       Clases:
#           Dirreccion:
#               Crea un objeto con los 
#               datos de ubicacion del
#               usuario.
#
#       Funciones:
#           Empty
#
###########################################

class Direccion():
    def __init__(self, calle, numero, ciudad, provincia, pais):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais