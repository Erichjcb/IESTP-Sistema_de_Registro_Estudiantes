class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Carrera:", self.carrera)
        print("------------------")


e1 = Estudiante("Juan", "Sistemas")
e2 = Estudiante("Ana", "Contabilidad")

estudiantes = [e1, e2]

buscar = input("Ingrese nombre: ")

for e in estudiantes:
    if e.nombre == buscar:
        print("Encontrado:", e.nombre)
        print("Carrera:", e.carrera)