class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print("Empleado de la empresa")
        print(f"Nombre: {self.nombre}")

class Administrador(Empleado):
    def mostrar(self):
        super().mostrar()
        print("Cargo: Administrador del sistema")

class Vendedor(Empleado):
    def mostrar(self):
        super().mostrar()
        print("Cargo: Vendedor de productos")

empleado1 = Administrador("Shakira Alondra")
empleado2 = Vendedor("Fabiana Alejandra")

print("----- Datos del Empleado ------")
empleado1.mostrar()
empleado2.mostrar()
