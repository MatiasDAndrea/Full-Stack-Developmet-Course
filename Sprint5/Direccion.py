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
    def __init__(self, dir):
        
        
        self.calle = dir.get("calle","")
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais

        # Si algun elemento "" error, hay algo mal
        # checkear que todo sea tipo str
        


