class Matricula:
    def __init__(self,alumno,curso):
        self.alumno=alumno
        self.curso=curso
        
    def mostrar(self):
        print("====MATRICULA====")
        print("Alumno: ", self.alumno.nombre)
        print("Curso: ",self.curso.nombre)
        print("Créditos: ",self.curso.creditos)
        