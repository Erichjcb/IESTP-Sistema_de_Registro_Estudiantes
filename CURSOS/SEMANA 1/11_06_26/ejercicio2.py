class estudiante:
    def __init__(self,nombre,carrera):
        self.nombre=nombre
        self.carrera=carrera
        
e1=estudiante("Juan","Sistemas")
e2=estudiante("Ana","Contabilidad")

estudiantes=[e1,e2]

for estudiante in estudiantes:
    print(estudiante.nombre,"-",estudiante.carrera)

        