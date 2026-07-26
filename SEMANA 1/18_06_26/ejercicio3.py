# Clase Producto
class Producto:
    # Constructor que recibe nombre y precio
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Método para calcular el descuento
    def descuento(self):
        if self.precio > 100:
            return self.precio * 0.10
        else:
            return 0

    # Método para calcular el precio final
    def precio_final(self):
        return self.precio - self.descuento()

    # Método para mostrar los datos del producto
    def mostrar(self):
        print("Producto:", self.nombre)
        print("Precio:", self.precio)
        print("Descuento:", self.descuento())
        print("Precio Final:", self.precio_final())
        print("-----------------------")


# Lista donde se almacenarán los productos
productos = []

# Usamos for range para registrar los 6 productos
for i in range(6):
    print("\nIngrese los datos del producto", i + 1)
    print(f"Ingrese los datos del producto {i+1}")

    nombre = input("Ingrese el producto: ")
    precio = float(input("Ingrese el precio: "))

    # Crear el objeto y guardarlo en la lista
    p = Producto(nombre, precio)
    productos.append(p)


# Pantalla de salida (Lista de productos)
print("\n======= LISTA DE PRODUCTOS =======")

# Recorremos la lista y mostramos los resultados
for p in productos:
    p.mostrar()