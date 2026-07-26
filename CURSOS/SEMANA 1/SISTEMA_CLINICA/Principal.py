from Paciente import Paciente
from Medico import Medico
from Cita import Cita
l1=input("Ingrese el nombre del médico: ")
a1=input("Ingrese la especialidad del médico: ")
u1=input("Ingrese el nombre del paciente: ")
med=Medico(l1, a1)
pac=Paciente(u1)
cita1=Cita(pac,med)
 
cita1.mostrar()