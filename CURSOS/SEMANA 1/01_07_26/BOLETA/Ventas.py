class Ventas:
    def __init__(self,cliente,producto):
        self.cliente=cliente
        self.producto=producto
        
    def mostrar(self):
        print("====BOELTA====")
        print("Cliente: ", self.cliente.nombre)
        print("Producto: ",self.producto.nombre)
        print("Precio: ",self.producto.precio)
        print("Cantidad: ",self.producto.cantidad)
        print("Total a pagar: ", (self.producto.precio*self.producto.cantidad))
        