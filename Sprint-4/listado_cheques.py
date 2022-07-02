import sys
from datetime import datetime
import getopt
import re


def search_check(lista, diccionario):

    #-------------------------------------------------------------------------
    # search_check() se encarga de filtrar cheques segun los parametros
    #    que ingreso el usuario.
    #
    # Input:
    #   lista: Contiene todas las lineas del archivo leido.
    #   diccionario: contiene todos los campos ingresados por el usuario.
    #
    # Ouput: 
    #   cheques_filtrados: Lista conteniendo cada uno de los cheques filtrados.
    #--------------------------------------------------------------------------

    cheques_filtrados = []
    dni = diccionario["dni"]
    estado = diccionario.get("estado",False)
    fecha_desde = diccionario.get("fecha_desde",False)
    fecha_hasta = diccionario.get("fecha_hasta",False)

    for x in lista:

        
        x = x.replace("\n","").split(",")
        fecha_lista  = float(x[6])
        dni_lista    = x[8]

        filtro_dni = dni == dni_lista
        filtro_fecha =  (not fecha_desde) or (fecha_desde <= fecha_lista <= fecha_hasta)
        filtro_estado = (not estado) or (estado in x)

        if all([filtro_dni, filtro_fecha, filtro_estado]):

            cheques_filtrados.append(x)

    return cheques_filtrados


def checkinput():
    
    #---------------------------------------------------------------------------------
    # La funcion checkinput() se encarga de checkear el correcto ingreso de variables.
    #   por parte del usuario.
    #
    # Input:
    #   Empty.
    #
    # Ouput:
    #   booleano: True o False segun las condiciones establecidas de ingreso.
    #   diccionario: Contiene todos los campos ingresados por el usuario.
    #----------------------------------------------------------------------------------

    argv = sys.argv
    opts, args = getopt.getopt(argv[1:], "c:d:s:t:e:f:a")
    diccionario = {}

    for letter, value in opts:

        if letter == "-c":
            diccionario["csv_name"] = value
        
        elif letter == "-d":
            diccionario["dni"]      = value.upper()
        
        elif letter == "-s":
            diccionario["salida"]   = value.upper()
        
        elif letter == "-t":
            diccionario["tipo"]     = value.upper()
        
        elif letter == "-e":
            diccionario["estado"]   = value.upper()
        
        elif letter == "-f":

            inicio,fin = value.split(":")
            diccionario["fecha_desde"] = datetime.strptime(inicio, '%d-%m-%Y').timestamp()
            diccionario["fecha_hasta"] = datetime.strptime(fin, '%d-%m-%Y').timestamp()
    
    check_csv    = re.search(r".csv\b",diccionario.get("csv_name",""))
    check_dni    = diccionario.get("dni","").isnumeric()
    check_output = diccionario.get("salida","") in ["PANTALLA", "SALIDA"]
    check_type   = diccionario.get("tipo","") in ["EMITIDO", "DEPOSITADO"]
    check_status = diccionario.get("estado","") in ["PENDIENTE", "APROBADO", "RECHAZADO",""]
    
    if diccionario.get("fecha_hasta","")=="" and diccionario.get("fecha_desde","") == "":

        check_date = True
    
    elif diccionario.get("fecha_desde","") < diccionario.get("fecha_hasta",""):

        check_date = True

    else :
        check_date = False

    return all([check_csv, check_dni, check_output, check_type, check_status, check_date]), diccionario


def init():
    
    #-----------------------------------------------------------------------
    # La funcion init() se encarga de inicializar el programa de busqueda.
    #
    # Input:
    #   Empty.
    #
    # Ouput:
    #   Empty.
    #------------------------------------------------------------------------

    check, diccionario = checkinput()
    if (check):

        #Genero apertura del archivo
        archivo = open(diccionario["csv_name"])
        
        #Filtrado de la lista
        lista = archivo.readlines()

        #Funcion de checkeo del csv
        #Borrar las lineas que tienen algun defecto

        cheques_filtrados = search_check(lista, diccionario)

        #Para la lista filtrada, tenemos que filtrar por dos variables. Cuenta y por numero de cheque.
        #Funcion para punto 3

        #diccionario["salida"] Pantalla / CSV
        # si es pantalla print(cheques)
        # si es csv open("nombre que sea","w")
        # meten los cheques filtrados al csv que crearon

        
        print(cheques_filtrados)

        #Genero Output de la funcion.
        
    else:
        print("Error de Ingreso")

#Inicializa el Proceso de busqueda
init()


