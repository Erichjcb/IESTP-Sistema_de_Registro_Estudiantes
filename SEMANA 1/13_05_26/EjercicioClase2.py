class Producto:
    def __init__(self):
        self.__precio = 0

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo")

    def get_precio(self):
        return self.__precio


registro = Producto()

try:
    p = float(input("Ingrese el precio del producto: "))
    registro.set_precio(p)

    print("Precio del producto:", registro.get_precio())

except:
    print("Error en el ingreso de datos")