class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def info(self):
        print(F'Nombre: {self.nombre}\nEdad: {self.edad}')
class estudiante(persona): pass
persona1 = persona('Jhosep', 18)
persona1.info()
estudiante1 = estudiante('Erich', 28)
estudiante1.info()
