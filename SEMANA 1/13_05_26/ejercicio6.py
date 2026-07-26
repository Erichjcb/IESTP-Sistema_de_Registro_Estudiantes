class cuenta:
    def __init__(self):
        self.__saldo=0
        
    def set_saldo(self,saldo):
        if saldo >=0:
            self.__saldo = saldo
        else:
            print("Saldo inválido")
            
    def get__saldo(self):
        return self.__saldo
    
cuenta=cuenta()

try:
    s = int(input("Ingrese saldo:"))
    cuenta.set_saldo(s)
    
    print("saldo", cuenta.get__saldo)
    
except:
    print("Error e")