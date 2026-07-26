class Cliente:
    def __init__(self,nombre):
        self.nombre=nombre
        
    def Mostrar_nombre(self):
        print("Nombre:",self.nombre)
        
class Producto:
    def __init__(self,Pro,precio):
        self.Pro=Pro
        self.precio=precio
        
        
    def Mostrar_Pro(self):
        print("Producto:",self.Pro)
        print("Precio: ",self.precio)
        
 
        
c1=Cliente("Erich")
p1=Producto("TV",2000)

c1.Mostrar_nombre()
p1.Mostrar_Pro()
        
        