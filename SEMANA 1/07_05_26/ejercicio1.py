class cliente:
    def __init__(self,nombre, dni):
        self.nombre=nombre
        self.dni=dni

class producto:
    def __init__(self,nombre,marca):
        self.nombre=nombre
        self.marca=marca
        

class venta:
    def __init__(self,cliente,producto,precio):
        self.cliente=cliente
        self.producto=producto
        self.precio=precio
    
    def mostrar(self):
        print("Cliente: ",self.cliente.nombre)
        print("DNI: ", self.cliente.dni)
        print("Producto: ",self.producto.nombre)
        print("Marca: ",self.producto.marca)
        print("Precio: ",self.precio)

clie1=cliente("Angelo",74756022)
prod1=producto("Moto","Honda")
vent1=venta(clie1,prod1,7200)

vent1.mostrar()
        
