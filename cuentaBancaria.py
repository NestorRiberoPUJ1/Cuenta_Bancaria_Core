class cuentaBancaria:
    instances=[]

    def __init__(self, balance=0, interes=1):
        self.balance = 0
        self.interes = interes/100
        self.instances.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if(self.balance < amount):
            if(self.balance < 5):
                self.balance = 0
            else:
                self.balance -= 5
            print("Fondos insuficientes: cobrando una tarifa de $5")
        else:
            self.balance -=amount
        return self

    def mostrar_info_cuenta(self):
        print (f"Balance: ${self.balance}")
        return self

    def generar_interes(self):
        if(self.balance>0):
            self.balance += self.balance*self.interes
        return self

    @classmethod
    def imprimirInstancias(cls):
        for x in cls.instances:
            x.mostrar_info_cuenta()

