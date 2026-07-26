class Inventario:
    def __init__(self):
        self.__stock = 0

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("El stock debe ser entero y mayor o igual que cero")

    def get_stock(self):
        return self.__stock


invent = Inventario()

try:
    i = int(input("Ingrese el stock: "))
    invent.set_stock(i)

    print("Nota del estudiante:", invent.get_stock())

except:
    print("Error al ingresar la cantidad del stock")