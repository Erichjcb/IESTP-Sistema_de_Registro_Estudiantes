class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

# Lista de estudiantes
lista = []



for i in range(4):
    nombre = input("Nombre: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    lista.append(Estudiante(nombre, nota1, nota2))

# Variables para el mayor promedio
mayor = 0
mejor = ""

print("\nNombre\t\tPromedio\tEstado")

# Mostrar datos y buscar el mejor estudiante
for e in lista:
    promedio = (e.nota1 + e.nota2) / 2
    
    if promedio > mayor:
        mayor = promedio
        mejor = e.nombre

    if promedio >= 13:
        print(e.nombre, "\t\t", promedio, "\tAprobado")
    else:
        print(e.nombre, "\t\t", promedio, "\tDesaprobado")

# Mostrar estudiante con mayor promedio
print("\nEstudiante con mayor promedio:")
print("Nombre:", mejor)
print("Promedio:", mayor)