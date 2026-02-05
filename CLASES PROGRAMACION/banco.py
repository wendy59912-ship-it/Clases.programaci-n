class Cuentabancaria:
    def __init__(self, titular, saldo):
        self._titular=titular
        self.__saldo=saldo

    def obtenersaldo(self):
        return self.__saldo
    
    def depositar(self, newsaldo):
        self.__saldo += newsaldo

    def retiro(self,cant):
        if self.__saldo <= cant:
           print("No tienes dinero pobre")
        else:
            self.__saldo -= cant

cuenta1 = Cuentabancaria("Ami", 1000000)
print(cuenta1._titular)
print(cuenta1.obtenersaldo())
cuenta1.depositar(500000)
print(cuenta1.obtenersaldo())
cuenta1.retiro(400000000)