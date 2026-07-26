class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
    
    def depositar_dinero(self,monto):
        self.saldo+=monto
        print(f'El saldo actual es de {self.saldo}')
    
    
    def retirar_dinero(self,monto):
        if monto<self.saldo:
            self.saldo-=monto
            print(f'Usted retiro {monto} y su saldo es {self.saldo}')
        else:
            print("Su saldo es insuficiente para retirar")
    
c1=CuentaBancaria("Roberto",100)
c2=CuentaBancaria("Lidia",20)

c1.depositar_dinero(100)
c1.retirar_dinero(200)
c2.depositar_dinero(10)
c2.retirar_dinero(2000)