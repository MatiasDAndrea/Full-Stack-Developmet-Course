from abc import abstractclassmethod
import Cuenta

@abstractclassmethod
class Cliente():
    def __init__(self,id,name,sName,dni,tipe):
        id=self.id
        name=self.name
        sName=self.sName
        dni=self.dni
        self.debitCard = 1
        tipe = tipe if tipe != None else 'Classic'
        self.Cuenta = Cuenta.Cuenta.__init__()
    def puede_crear_chequera():
        return bool
    def puede_crear_tarjeta_credito():
        return bool
    def puede_comprar_dolar():
        return bool

class Gold (Cliente):
    def __init__(self, id, name, sName, dni,tipe):
            Cliente.__init__(self,id,name,sName, dni)
            self.tipe= "GOLD"
            self.creditCard = 1
            self.dolarAccount= True
            self.debit= 20000
            self.cheq= True
            self.comission= 0.5
            self.maxTransf= 500000

class Classic(Cliente):
    def __init__ (self,id,name,sName,dni,tipe):
        Cliente.__init__(self,id,name,sName,dni)
        self.tipe="CLASSIC"
        self.creditCard = 0
        self.dolarAccount= False
        self.debit= 10000
        self.cheq= False
        self.comission= 1
        self.maxTransf= 150000 

class Black (Cliente):
    def __init__(self, id, name, sName, dni):
        Cliente.__init__(self,id,name,sName, dni)
        self.tipe="BLACK"
        self.creditCard = 1
        self.dolarAccount= True
        self.debit= 100000
        self.cheq= 1
        self.comission= 0
        self.maxTransf= 0

