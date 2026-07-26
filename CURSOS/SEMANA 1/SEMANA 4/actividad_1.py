        
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total_pagar(self):
        
        total_pagar = self.precio * self.cantidad
        
        print(f'El total a pagar por {self.nombre} es: {total_pagar}')


p1 = Producto("Pelota", 50, 1)

p1.calcular_total_pagar()