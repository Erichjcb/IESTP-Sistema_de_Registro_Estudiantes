# Sistema de trabajadores

class Empleado:
    def mostrar(self):
        print("Empleado de la empresa")

class Administrador(Empleado):
    def mostrar(self):
        super().mostrar()  # Llama al método de la clase padre
        print("Administrador del sistema")

class Vendedor(Empleado):
    def mostrar(self):
        super().mostrar()  # También puede llamar al método padre si se desea
        print("Vendedor de productos")

# Crear objetos y mostrar información
empleado1 = Empleado()
empleado1.mostrar()

admin1 = Administrador()
admin1.mostrar()

vendedor1 = Vendedor()
vendedor1.mostrar()
