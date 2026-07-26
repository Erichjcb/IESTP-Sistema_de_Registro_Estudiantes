class tienda:
    def __init__(self,producto,precio):
        self.producto=producto
        self.precio=precio
        
    
    def mostrar_mensaje(self):
        if self.precio<500:
            print("El precio está por los suelos")
            
        elif self.precio<1000:
            print("El precio está cómodo")
           
        else:
            print("El precio está por las nubes")    
         
producto=input("Ingrese el producto: ")
precio=int(input("Ingrese el precio: "))

t1=tienda(producto,precio)
t1.mostrar_mensaje()