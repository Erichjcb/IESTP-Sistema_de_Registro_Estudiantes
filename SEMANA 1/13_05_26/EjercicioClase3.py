class Notas:
    def __init__(self):
        self.__nota = 0

    def set_nota(self, nota):
        if nota >= 0 and nota <= 20:
            self.__nota = nota
        else:
            print("La nota debe estar entre 0 y 20")

    def get_nota(self):
        return self.__nota


registro = Notas()

try:
    n = float(input("Ingrese la nota: "))
    registro.set_nota(n)

    print("Nota del estudiante:", registro.get_nota())

except:
    print("Error en el ingreso de datos")