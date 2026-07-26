from Libro import Libro
from Usuario import Usuario
from Prestamo import Prestamo
l1=input("Ingrese el título del libro: ")
a1=input("Ingrese el nombre del autor: ")
u1=input("Ingrese el nombre del usuario: ")
libro=Libro(l1, a1)
usuario=Usuario(u1)
presta=Prestamo(libro,usuario)
 
presta.mostrar()