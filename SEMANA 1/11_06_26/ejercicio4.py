class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"{self.nombre:<15} {self.precio:>6}")

# Crear objetos de productos
p1 = Producto("Celular", 3850)
p2 = Producto("Audífonos", 450)
p3 = Producto("Cargador", 120)

# Guardar los objetos en una lista
productos = [p1, p2, p3]

# Mostrar información de todos los productos
print("Producto        Precio")
print("-----------------------")
for p in productos:
    p.mostrar()
