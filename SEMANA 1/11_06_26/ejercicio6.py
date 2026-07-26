# Sistema de Tienda de Tecnología

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"{self.nombre:<15} {self.precio:>6}")

# Lista para almacenar los productos
productos = []

# Pedir cuántos productos se van a registrar
n = int(input("¿Cuántos productos desea registrar? "))

# Bucle para ingresar los datos
for i in range(n):
    print(f"\nProducto {i+1}:")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    
    # Crear objeto y agregarlo a la lista
    producto = Producto(nombre, precio)
    productos.append(producto)

# Mostrar todos los productos registrados
print("\nProducto        Precio")
print("-----------------------")
for p in productos:
    p.mostrar()
