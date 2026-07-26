class Prestamo:
    def __init__(self,libro,usuario):
        self.libro=libro
        self.usuario=usuario
        
    def mostrar(self):
        print("====PRÉSTAMO DE LIBRO====")
        print("Usuario: ", self.usuario.nombre)
        print("Libro: ",self.libro.titulo)
        print("Autor: ",self.libro.autor)
        