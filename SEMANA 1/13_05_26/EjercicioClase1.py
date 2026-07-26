class Alumno:
    def __init__(self):
        self.__edad = 0

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("Edad no puede ser negativa")

    def get_edad(self):
        return self.__edad


registro = Alumno()

try:
    e = int(input("Ingrese su edad: "))
    registro.set_edad(e)

    print("Edad:", registro.get_edad())

except:
    print("Error")
