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
        print("------ BOLETA DE VENTA ------")
        total=self.producto.precio*self.cantidad
        print("Cliente: ",self.cliente.nombre)
        print("Producto y precio: ",self.producto.nombre, self.producto.precio)
        print("Total a pagar: ",total)
        
nom_cli=input("Ingrese el nombre del cliente: ")
nom_prod=input("Ingrese el nombre del producto")        
pre_prod=float("Ingreso de precio: ")
cant=int(input("Ingrese la cantidad"))

c1=cliente(nom_cli)
p1=producto(nom_prod, pre_prod)
v1=venta(c1,p1,cant)

v1.mostrar()
        