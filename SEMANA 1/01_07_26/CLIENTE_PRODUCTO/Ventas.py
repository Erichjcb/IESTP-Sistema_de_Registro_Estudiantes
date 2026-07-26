class Ventas:
    
    def _init_(self,cliente,producto):
        self.producto=producto
        self.cliente=cliente
    def mostrar(self):
        print("Cliente:",self.cliente.nombre)
        print("Producto:",self.producto.nombre)
        print("Precio:","/s",self.producto.precio)