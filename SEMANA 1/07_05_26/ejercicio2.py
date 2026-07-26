class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
        
class Venta:
    def __init__(self,producto,cantidad):
        self.producto=producto
        self.cantidad=cantidad
        
    def mostrar(self):
        total=self.producto.precio*self.cantidad
        print("Nombre del producto:",self.producto.nombre)
        print("Precio del producto: ",self.producto.precio)
        print("Cantidad: ",self.cantidad)
        print("Total a pagar: ",total)
        
p1=Producto("Mouse",50)
v1=Venta(p1,3)
v1.mostrar()
        
        