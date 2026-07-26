# Clase Empleados
class Empleado:
    # Constructor que recibe nombre y ventas
    def __init__(self, nombre, ventas):
        self.nombre = nombre
        self.ventas = ventas

    # Método para calcular el bono
    def bono(self):
        if self.ventas < 1000:
            return 100
        
        if self.ventas >= 1000 and self.ventas <2000:
            return 200
        
        else:
            return 300

    # Método para calcular el precio final
    
    def total_recibir(self):
        return self.ventas + self.bono()

    # Método para mostrar los datos del producto
    def mostrar(self):
        print("Empleado: ", self.nombre)
        print("Ventas: ", self.ventas)
        print("Bono:", self.bono())
        print("Total a recibir: ", self.total_recibir())
        print("-----------------------")


# Lista donde se almacenarán los productos
empleados = []

# Usamos for range para registrar los 6 productos
for i in range(4):
    print("\nIngrese los datos del empleado", i + 1)
    

    nombre = input("Ingrese el nombre: ")
    ventas = float(input("Ingrese sus ventas: "))

    # Crear el objeto y guardarlo en la lista
    e = Empleado(nombre, ventas)
    empleados.append(e)


# Pantalla de salida (Lista de productos)
print("\n======= LISTA DE EMPLEADOS =======")

# Recorremos la lista y mostramos los resultados
for e in empleados:
    e.mostrar()