from datetime import date

class usuario:
    def __init__(self,nombre):
        self.nombre=nombre
        
class libro:
    def __init__(self,nombre):
        self.nombre=nombre
        
class prestamo:
    def __init__(self,usuario,libro,fecha):
        self.usuario=usuario
        self.libro=libro
        self.fecha=fecha
        
    def mostrar(self):
        print("------ BOLETA DE IESTO ------")
        print("Nombre del Estudiante: ",self.usuario.nombre)
        print("Nombre del titulo: ",self.libro.nombre)
        print("Fecha de préstamo: ",self.fecha.strftime("%d/%m/%y"))
        
nom_usu=input("Ingrese el nombre del usuario: ")
nom_libro=input("Ingrese el nombre del libro: ")        
fec= date.today()

u1=usuario(nom_usu)
l1=libro(nom_libro)
p1=prestamo(u1,l1,fec)
p1.mostrar()

        