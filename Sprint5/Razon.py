######################################################################
# Modulo : Razon.py
#
# Clase: Razon.
#   Metodos:
#       __init__()
#
#       resolver()
#           Inputs: cliente, evento     
#               cliente: Objeto creado de la clase Cliente
#               evento: array que contiene los datos de una transaccion.
#           Ouput: Justifica la razon por la que fue rechazada
#                  una operacion.
#
########################################################################

class Razon:


    def __init__(self,tipo):
        self.tipo = tipo


    def resolver(self,cliente,evento):
        
        estado          = evento["estado"]

        if estado == "RECHAZADA":
            dinero_actual   = evento["saldoEnCuenta"]
            dinero_retiro   = evento["monto"]
            cupo_diario     = evento["cupoDiarioRestante"]
            tarjetas_actual = evento["totalTarjetasDeCreditoActualmente"]
            chequera_actual = evento["totalChequerasActualmente"]
            
            descubrimiento  = cliente.cuenta.total_descubierto
            tarjetas_limite = cliente.cuenta.total_tarjeta_credito
            chequera_limite = cliente.cuenta.total_chequera_limite
            comsion         = cliente.cuenta.comision_por_transferencia
            limite          = cliente.cuenta.total_transferencia_limite

            dolar_bool          = cliente.puede_comprar_dolar
            crear_tarjeta_bool  = cliente.puede_crear_tarjeta_credito
            crear_chequera_bool = cliente.puede_crear_chequera

            if self.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":

                if dinero_actual+descubrimiento < dinero_retiro:
                    return f"Ustede no puede retirar ${dinero_retiro} de su cuenta!"

                elif dinero_retiro > cupo_diario:
                    return f"El cupo remanente es de: {cupo_diario}!"


            elif self.tipo == "ALTA_TARJETA_CREDITO":

                if crear_tarjeta_bool and tarjetas_actual >= tarjetas_limite:
                    return "Usted ha superado el numero maximo de tarjetas de credito disponibles!"
                
                elif not crear_tarjeta_bool:
                    return "Su Cuenta no tiene permitida la creacion de tarjetas de credito!"


            elif self.tipo == "ALTA_CHEQUERA":

                if crear_chequera_bool and chequera_actual >= chequera_limite:
                    return "Usted ha superado el numero maximo de chequeras disponibles!"
                
                elif not crear_chequera_bool:
                    return "Su Cuenta no tiene permitida la creacion de chequeras"
                

            elif self.tipo == "COMPRAR_DOLAR":

                if not dolar_bool:
                    return "Usted no Posee una cuenta en dolares"

                elif dinero_retiro > cupo_diario:
                    return f"El monto supera el cupo diario remanente de USD{cupo_diario}"

                elif dinero_retiro > dinero_actual:
                    return f"Usted no dispone de USD{dinero_retiro} en su cuenta!"


            elif self.tipo == "TRANSFERENCIA_ENVIADA":

                transferencia = transferencia*(1+comsion)
                if transferencia > dinero_actual:
                    return f"Usted no dispone de ${transferencia} para transferir"


            elif self.tipo == "TRANSFERENCIA_RECIBIDA":
            
                if dinero_retiro > limite:
                    return f"Usted no puede recibir transferencias mayores a ${limite}"
        
        else:
            return ""
            