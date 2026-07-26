class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        
        print(f"Nombre: {self.nombre}")
        print("Empleado de la empresa")

class Administrador(Empleado):
    def mostrar(self):
        super().mostrar()
        print("Cargo: Administrador del sistema")

class Vendedor(Empleado):
    def mostrar(self):
        super().mostrar()
        print("Cargo: Vendedor de productos")

a1=str(input("Ingrese el nombre del administrador: "))
v1=str(input("Ingrese el nombre del vendedor: "))
empleado1 = Administrador(a1)
empleado2 = Vendedor(v1)

print("----- Datos del administrador ------")
empleado1.mostrar()
print("----- Datos del vendedor ------")
empleado2.mostrar()
