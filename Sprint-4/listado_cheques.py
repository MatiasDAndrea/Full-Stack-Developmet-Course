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
    tipo = diccionario["tipo"]
    estado = diccionario.get("estado",False)
    fecha_desde = diccionario.get("fecha_desde",False)
    fecha_hasta = diccionario.get("fecha_hasta",False)

    for x in lista:

        
        x = x.replace("\n","").split(",")
        fecha_lista  = float(x[6])
        dni_lista    = x[8]
        tipo_lista   = x[9]

        filtro_dni = dni == dni_lista
        filtro_tipo = tipo == tipo_lista
        filtro_fecha =  (not fecha_desde) or (fecha_desde <= fecha_lista <= fecha_hasta)
        filtro_estado = (not estado) or (estado in x)

        if all([filtro_dni, filtro_fecha, filtro_estado, filtro_tipo]):

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
    check_output = diccionario.get("salida","") in ["PANTALLA", "CSV"]
    check_type   = diccionario.get("tipo","") in ["EMITIDO", "DEPOSITADO"]
    check_status = diccionario.get("estado","") in ["PENDIENTE", "APROBADO", "RECHAZADO",""]
    
    if diccionario.get("fecha_hasta","")=="" and diccionario.get("fecha_desde","") == "":

        check_date = True
    
    elif diccionario.get("fecha_desde","") < diccionario.get("fecha_hasta",""):

        check_date = True

    else :
        check_date = False

    return all([check_csv, check_dni, check_output, check_type, check_status, check_date]), diccionario


def cheques_repetidos(lista):

    #------------------------------------------------------------------------------------------------
    # La funcion cheques_repetidos(lista) se encarga de chequear que los cheques
    #   filtrados no sean repetidos.
    # 
    # Input:
    #   lista: Contiene todos los cheques filtrados por dni.
    #
    # Output:
    #   booleano: Entrega True si no hay cheques repetidos.
    #             Entrega False si se repite un mismo numero de cheque con un mismo numero de cuenta.
    #------------------------------------------------------------------------------------------------
    
    order_lista = []
    clones_lista = []

    #numero de cuenta origen (3) y numero de cheque (0)
    for x in lista:

        x = x.replace("\n","").split(",")
        # x[3] Cuenta Origen
        # x[0] Numero de cheque
        order_lista.append([x[3],x[0]])

    for x in order_lista:

        if x not in clones_lista:

            clones_lista.append(x)

    return len(order_lista) == len(clones_lista)        


def imprimir_valores(lista):

    #-----------------------------------------------------------------------------------
    # imprimi_valores(lista) imprime en pantalla valores relevantes del cheque filtrado.
    #
    # Input:
    #   lista: Lista de cheques filtrados.
    # 
    # Output:
    #   Salida por pantalla.
    #------------------------------------------------------------------------------------
    
    for x in lista:

        print("************************\n"+"NroCheque:"+x[0]+"\n"+ "Cuenta:"+x[3]+"\n"+ "Valor:"+x[5]+"\n"+ "Cuenta Destino:"+x[4]+"\n"+ "Estado:"+x[10]+"\n"+ "Tipo:"+x[9]+"\n"+"************************\n")


def crear_csv(diccionario,lista):

    #---------------------------------------------------------------------------
    # crear_csv() se encarga de crear un archivo csv con los cheques filtrados.
    #
    # Input:
    #   Empty.
    #
    # Output:
    #   Empty.
    #----------------------------------------------------------------------------

    dni = diccionario["dni"]
    fecha = str(datetime.now()).replace(":"," ")
    nombre_archivo = dni+" "+fecha+".csv"
    archivo = open(nombre_archivo,"w")

    for x in lista:

        linea = x[3]+","+",".join(x[5:8])+"\n"
        archivo.writelines(linea)
    
    archivo.close()


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
        check = cheques_repetidos(lista)

        if (check):

            cheques_filtrados = search_check(lista, diccionario)
            if diccionario["salida"] == "PANTALLA":

                imprimir_valores(cheques_filtrados)

            elif diccionario["salida"] == "CSV":

                crear_csv(diccionario, cheques_filtrados)
                
        else:
            print("Cheque Repetido")
        

        archivo.close()

        
    else:
        print("Error de Ingreso")

#Inicializa el Proceso de busqueda
init()


