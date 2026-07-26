class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
class Venta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        
    def mostrar(self):
        
        total = self.producto.precio * self.cantidad
        print("\n--- DETALLE DEL RECIBO ---")
        print("Nombre del producto:", self.producto.nombre)
        print("Precio unitario:   ", self.producto.precio)
        print("Cantidad:          ", self.cantidad)
        print("--------------------------")
        print("Total a pagar:     ", total)



print("Registro de Producto")
nombre_p = input("Ingrese el nombre del producto: ")
precio_p = float(input("Ingrese el precio: ")) 
p1 = Producto(nombre_p, precio_p)

print("\nRegistro de Venta")
cantidad_v = int(input("Cantidad de productos: "))


v1 = Venta(p1, cantidad_v)
v1.mostrar()