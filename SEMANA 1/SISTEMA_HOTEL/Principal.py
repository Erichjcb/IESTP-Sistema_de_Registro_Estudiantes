from Habitacion import Habitacion
from Huesped import Huesped
from Reserva import Reserva
l1=input("Ingrese el número de habitación: ")
a1=input("Ingrese el tipo de habitación: ")
u1=input("Ingrese el nombre del huesped: ")
habita=Habitacion(l1, a1)
huesp=Huesped(u1)
reser=Reserva(habita,huesp)
 
reser.mostrar()