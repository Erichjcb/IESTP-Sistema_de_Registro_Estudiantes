class cliente:
    def __init__(self,nombre):
        self.nombre=nombre
        
class producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
        
class venta:
    def __init__(self,cliente,producto,cantidad):
        self.cliente=cliente
        self.producto=producto
        self.cantidad=cantidad
        
    def mostrar(self):
        total=self.producto.precio*self.cantidad
        print("Cliente: ",self.cliente.nombre)
        print("Producto y precio: ",self.producto.nombre, self.producto.precio)
        print("Total a pagar: ",total)
        
c1=cliente("Juanita Luna")
p1=producto("Olla - ", 188)
v1=venta(c1,p1,3)

v1.mostrar()
        
        