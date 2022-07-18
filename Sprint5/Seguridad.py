import json

class Seguridad:

    def check_JSON(self, data):

        ##########################################################
        #Checkeo que todos los campos buscados en el JSON existan.
        numero        = data.get("numero","")
        nombre        = data.get("nombre","")
        apellido      = data.get("apellido","")
        dni           = data.get("dni","")
        tipo          = data.get("tipo","")
        direccion     = data.get("direccion","")
        transacciones = data.get("transacciones","")

        data_entry = [numero, nombre, apellido, dni, tipo, direccion, transacciones]

        if "" in data_entry:
            return False

        #################################################################
        #Checkeo el tipo de Informacion Ingresada en los campos del JSON.
        data_type = {
            "numero": int,
            "nombre": str,
            "apellido": str,
            "dni": str,
            "tipo": str,
            "direccion": dict,
            "transacciones": list
        }

        for key in data:
            
            check = isinstance(data[key],data_type[key])

            if not check:
                return False

        ##########################################################
        #Checkeo que el tipo de usuario se encuentre bien escrito.
        if tipo not in ["BLACK","GOLD","CLASSIC"]:
            return False

        #############
        #Checkeo DNI.
        if not dni.isnumeric():
            return False

        #####################################
        #Fin Check, JSON es valido.
        return True

    
    def check_transacciones(self, transaccion):


        estado = transaccion.get("estado","")
        tipo = transaccion.get("tipo","")
        cuentaNumero = transaccion.get("cuentaNumero","")
        cupoDiarioRestante = transaccion.get("cupoDiarioRestante","")
        cantidadExtraccionesHechas = transaccion.get("cantidadExtraccionesHechas","")
        monto = transaccion.get("monto","")
        fecha = transaccion.get("fecha","")
        numero = transaccion.get("numero","")
        saldoEnCuenta = transaccion.get("saldoEnCuenta","")
        totalTarjetasDeCreditoActualmente = transaccion.get("totalTarjetasDeCreditoActualmente","")
        totalChequerasActualmente = transaccion.get("totalChequerasActualmente","")

        check_list = [
            estado,
            tipo,
            cuentaNumero,
            cupoDiarioRestante,
            cantidadExtraccionesHechas,
            monto,
            fecha,
            numero,
            saldoEnCuenta,
            totalTarjetasDeCreditoActualmente,
            totalChequerasActualmente
        ]

        #############################################################
        #Checkeo la Existencia de todos los campos en la transaccion.
        if "" in check_list:
            return False

        #####################################################
        #Checkeo que todos los campos sean del tipo correcto.
        data_type = {
            "estado":str,
            "tipo":str,
            "cuentaNumero":int,
            "cupoDiarioRestante":int,
            "cantidadExtraccionesHechas":int,
            "monto":int,
            "fecha":str,
            "numero":int,
            "saldoEnCuenta":int,
            "totalTarjetasDeCreditoActualmente":int,
            "totalChequerasActualmente":int
        }

        for key in transaccion:

            check = isinstance(data[key],data_type[key])
            if not check:
                return False

        ###################
        #Checkeo el estado. 
        if estado not in ["ACEPTADA","RECHAZADA"]:
            return False

        ##############
        #Checkeo tipo.
        tipos = [
            "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
            "ALTA_TARJETA_CREDITO",
            "ALTA_CHEQUERA",
            "COMPRAR_DOLAR",
            "TRANSFERENCIA_ENVIADA",
            "TRANSFERENCIA_RECIBIDA"
        ]
        if tipo not in tipos:
            return False

        #############################################
        #Checkeo valores de la transaccion ingresada.
        cuentaNumero
        cupoDiarioRestante
        cantidadExtraccionesHechas
        monto
        numero
        saldoEnCuenta
        totalTarjetasDeCreditoActualmente
        totalChequerasActualmente

        #####################################
        #Fin Check, la transaccion es valida.
        return True




    
            

f = open("userData.json")
data = json.load(f)["transacciones"][0]
#data = json.load(f)
seguridad = Seguridad()

print(seguridad.check_transacciones(data))