class Cliente():
    def __init__(self,id,name,sName,dni,tipe,debitCard):
        id=self.id
        name=self.name
        sName=self.sName
        dni=self.dni
        debitCard=self.debitCard
        def __str__(self):
            return (f"El cliente es")
            
    class Gold (Cliente):
        def __init__(self, id, name, sName, dni):
            self.tipe="Gold"
            Cliente.__init__(self,id,name,sName, dni,"Gold")
            self.creditCred = 1
            self.dolarAccount= True
            self.debit= 20000
            self.cheq= True
            self.comission= 0.5
            self.maxTransf= 500000
            class Classsic(Cliente):
                def __init__ (self,id,name,sName,dni)
                Cliente.__init__(self,id,name,sName,dni,"Classic")
                self.creditCred = 0
                self.dolarAccount= False
                self.debit= 10000
                self.cheq= False
                self.comission= 1
                self.maxTransf= 150000
                class Black (Cliente):
                    def __init__(self, id, name, sName, dni):
                        self.tipe="Gold"
                        Cliente.__init__(self,id,name,sName, dni,"Black")
                        self.creditCred = 1
                        self.dolarAccount= True
                        self.debit= 100000
                        self.cheq= 1
                        self.comission= 0
                        self.maxTransf= 0
                        class Transaction ():
                            def __init__ (self):
                                def RETIRO_EFECTIVO_CAJERO_AUTOMATICO():
                                    def ALTA_TARJETA_CREDITO():
                                        def ALTA_CHEQUERA():
                                            def COMPRAR_DOLAR():
                                                def TRANSFERENCIA_ENVIADA():
                                                    def TRANSFERENCIA_RECIBIDA():