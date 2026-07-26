class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

class Producto:
    def __init__(self, nombre, marca):
        self.nombre = nombre
        self.marca = marca

class Venta:
    def __init__(self, cliente, producto, precio):
        self.cliente = cliente
        self.producto = producto
        self.precio = precio
    
    def mostrar(self):
        print("\n--- RESUMEN DE VENTA ---")
        print("Cliente: ", self.cliente.nombre)
        print("DNI: ", self.cliente.dni)
        print("Producto: ", self.producto.nombre)
        print("Marca: ", self.producto.marca)
        print("Precio: S/.", self.precio)

print("Ingrese los datos del Cliente:")
nom_clie = input("Nombre: ")
dni_clie = input("DNI: ")
clie1 = Cliente(nom_clie, dni_clie)

print("\nIngrese los datos del Producto:")
nom_prod = input("Nombre del producto: ")
marca_prod = input("Marca: ")
prod1 = Producto(nom_prod, marca_prod)


precio_prod = float(input("\nIngrese el precio: "))


vent1 = Venta(clie1, prod1, precio_prod)
vent1.mostrar()