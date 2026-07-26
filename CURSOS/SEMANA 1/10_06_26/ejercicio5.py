class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Nombre: {self.nombre}")


class Docente(Persona):
    def __init__(self, nombre, DNI, TELEFONO):
        super().__init__(nombre)  
        self.DNI = DNI
        self.TELEFONO = TELEFONO

    def mostrar(self):
        
        super().mostrar()
        print(f"DNI: {self.DNI}")
        print(f"Teléfono: {self.TELEFONO}")


class Estudiante(Persona):
    def __init__(self, nombre, NOTA, CELULAR):
        super().__init__(nombre)
        self.NOTA = NOTA
        self.CELULAR = CELULAR

    def mostrar(self):
        super().mostrar()
        print(f"Nota: {self.NOTA}")
        print(f"Celular: {self.CELULAR}")


print("")

nd1 = input("Ingrese el nombre del docente: ")
dni1 = input("Ingrese el número de DNI: ")
telf1 = input("Ingrese el número de teléfono: ")

print("")
ne1 = input("Ingrese el nombre del estudiante: ")
nota1 = float(input("Ingrese la nota: "))
cel1 = input("Ingrese el número de celular: ")


docente1 = Docente(nd1, dni1, telf1)
estudiante1 = Estudiante(ne1, nota1, cel1)


print("\n----- Datos del docente ------")
docente1.mostrar()

print("\n----- Datos del estudiante ------")
estudiante1.mostrar()
