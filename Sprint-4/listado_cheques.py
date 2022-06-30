import sys
import datetime
sys.argv[1::] = ["text.txt","40134552","Pantalla","Emitido","pendiente","53"]

def search_check(lista, dni, types, status=False, date=False):

    #search_check recibe una lista donde cada elemento es un reglon del archivo csv.
    #devuelve una lista con los cheques filtrados.

    #Genero mi variable de output
    output_list = []

    for x in lista:

        x = x.replace("\n","").split(",")
        if dni in x and types in x and (not status or (status and status in x)):

            output_list.append(x)




def checkinput():
    
    #La funcion checkinput() se encarga de checkear los Input values.
    #La funcion devuelve True o False dependiendo en base del cumplimiento de condiciones.

    while len(sys.argv)<7:
        sys.argv.append(False)

    csvname, dni, output, type, status, date = sys.argv[1::]

    check_csv = csvname.split(".")[1] == "txt"
    check_dni = str(dni).isnumeric()
    check_output = output.upper() in ["PANTALLA", "SALIDA"]
    check_type = type.upper() in ["EMITIDO", "DEPOSITADO"]
    check_status = status.upper() in ["PENDIENTE", "APROBADO", "RECHAZADO"]
    check_date = True

    return all([check_csv, check_dni, check_output, check_type, check_status, check_date])


def init():
    
    # La funcion init() se encarga de inicializar el programa de busqueda.

    if (checkinput()):

        #Obtengo todas las variables de entrada
        csvname, dni, output, type, status, date = sys.argv[1::]

        #Genero apertura del archivo
        archivo = open(csvname)
        
        #Filtrado de la lista
        lista = archivo.readlines()
        cheques = search_check(lista, dni, type)

        #Genero Output de la funcion.
        
    else:
        print("Error de Ingreso")



init()

