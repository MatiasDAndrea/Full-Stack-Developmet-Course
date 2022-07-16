class Cuenta():
    def __init__(self,tipo):
        if(tipo == 'Classic'):
            self.total_tarjeta_debito = 1
            self.total_descubierto = 0
            self.total_tarjeta_credito = 0
            self.total_tarjeta_credito_limite = 0
            self.comision_por_transferencia= 1
            self.limite_extraccion_diario= 10000 
            self.total_chequera = 0
            self.total_chequera_limite = 0
            self.total_transferencia_limite = 150000
            self.monto_pesos = 0
            self.monto_dolares = 0
        if(tipo == 'Gold'):
            self.total_tarjeta_debito = 1
            self.total_descubierto = 10000
            self.total_tarjeta_credito = 0
            self.total_tarjeta_credito_limite = 1
            self.comision_por_transferencia= 0.5
            self.limite_extraccion_diario= 20000
            self.total_chequera = 0
            self.total_chequera_limite = 1
            self.total_transferencia_limite = 500000
            self.monto_pesos = 0
            self.monto_dolares = 0
        if(tipo == 'Black'):
            self.total_tarjeta_debito = 1
            self.total_descubierto = 10000
            self.total_tarjeta_credito = 0
            self.total_tarjeta_credito_limite = 5
            self.comision_por_transferencia= 0
            self.limite_extraccion_diario= 100000
            self.total_chequera = 0
            self.total_chequera_limite = 2
            self.total_transferencia_limite = 100000000000 # Hay que ponerle inf con numpy
            self.monto_pesos = 0
            self.monto_dolares = 0
        

