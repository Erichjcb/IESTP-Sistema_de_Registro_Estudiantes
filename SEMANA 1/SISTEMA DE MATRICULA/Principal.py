from Curso import Curso
from Alumno import Alumno
from Matricula import Matricula
l1=input("Ingrese el nombre del curso: ")
a1=input("Ingrese los créditos del curso: ")
u1=input("Ingrese el nombre del alumno ")
curso=Curso(l1, a1)
alumno=Alumno(u1)
matri=Matricula(alumno,curso)
 
matri.mostrar()