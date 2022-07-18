############################################################
#   Modulo: main.py
#       Funciones:
#           __init__():
#           La funcion se encarga de inicializar el proceso
#       
#############################################################

import json
import Cliente
from Cuenta import Cuenta
from Razon import Razon
import sys

def __init__():

    try:
        f = open(sys.argv[1],"r")
        data = json.load(f)

        numero        = data.get("numero","")
        nombre        = data.get("nombre","")
        apellido      = data.get("apellido","")
        dni           = data.get("dni","")
        tipo          = data.get("tipo","")
        direccion     = data.get("direccion","")
        transacciones = data.get("transacciones","")

        diccionario = {"BLACK":Cliente.Black,"GOLD":Cliente.Gold,"CLASSIC":Cliente.Classic}
        cliente = diccionario.get(tipo)(numero, nombre, apellido, dni, tipo, direccion)
        
        reporte = {
            "nombre":f"{nombre} {apellido}",
            "numero":numero,
            "DNI":dni,
            "Direccion":direccion,
            "Transaccion": []
        }

        for x in transacciones:

            razon = Razon(x["tipo"])
            reporte_transaccion = {
                "fecha": x["fecha"] ,
                "Tipo Operacion": x["tipo"],
                "Estado": x["estado"],
                "Monto": x["monto"],
                "Razon": razon.resolver(cliente,x)
            }
            reporte["Transaccion"].append(reporte_transaccion)
        
        print(reporte)
    
        f.close()

    except (IndexError, FileNotFoundError):
        print("Error")
    
    except:
        print("Error")

__init__()

