
#[Cliente,]
class Razon:

    def __init__(self,tipo):
        self.tipo = tipo  ## Retiro, alta chequera etc 

    def resolver(self,cliente,evento):

        if self.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":

            dinero_actual = evento["saldoEnCuenta"]
            dinero_retiro = evento["monto"]
            cupo_diario   = evento["cupoDiarioRestante"]

            if dinero_actual < dinero_retiro:
                return "Usted no posee suficiente dinero!"

            elif dinero_retiro > cupo_diario:
                return f"El cupo disponible es de: {cupo_diario}!"

        elif self.tipo == "ALTA_TARJETA_CREDITO":

            tarjetas_actual  = evento["totalTarjetasDeCreditoActualmente"]
            tarjetas_limite = cliente.cuenta.total_tarjeta_credito

            if tarjetas_actual >= tarjetas_limite:
                return "Usted ha superado el numero maximo de tarjetas de credito disponibles!"

        elif self.tipo == "ALTA_CHEQUERA":

            chequera_limite  = cliente.cuenta.total_chequera_limite
            chequera_actual  = evento["totalChequerasActualmente"]

            if chequera_actual >= chequera_limite:
                return "Usted ha superado el numero maximo de chequeras disponibles!"
            
        elif self.tipo == "COMPRAR_DOLAR":

            dolar_actual = evento["saldoEnCuenta"]
            dolar_retiro = evento["monto"]
            cupo_diario  = evento["cupoDiarioRestante"]
            dolar_bool   = cliente.puede_comprar_dolar

            if not dolar_bool:
                return "Usted no Posee una cuenta en dolares"

            elif dolar_retiro > cupo_diario:
                return "El monto supera el cupo diario permitido"

            elif dolar_retiro > dolar_actual:
                return "Usted no dispone de ese monto a retirar"

        elif self.tipo == "TRANSFERENCIA_ENVIADA":

            monto_actual  = evento["saldoEnCuenta"]
            transferencia = evento["monto"]*(1+cliente.cuenta.comision_por_transferencia)

            if transferencia > monto_actual:
                return "Usted no dispone del monto a transferir"

        elif self.tipo == "TRANSFERENCIA_RECIBIDA":

            monto  = evento["monto"]
            limite = cliente.cuenta.total_transferencia_limite
            
            








        

        

    

        

            



#RETIRO_EFECTIVO_CAJERO_AUTOMATICO: check
#ALTA_TARJETA_CREDITO: Se solicito una nueva tarjeta de crédito
#ALTA_CHEQUERA: Se solicito una nueva chequera
#COMPRAR_DOLAR: Se solicito realizar la transacción para comprar
#TRANSFERENCIA_ENVIADA: Solo se puede en pesos y lo que tenga en caja
#TRANSFERENCIA_RECIBIDA:


