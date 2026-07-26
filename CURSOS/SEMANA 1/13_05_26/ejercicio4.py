class Alumno:
    def __init__(self):
        self.__edad = 0
        
        
    def set_edad(self,edad):
        if edad >= 0:
            self.__edad = edad
            print("Edad correcta")
            
        else:
            print("Edad incorrecta")
            
            
a1=Alumno()
a1.set_edad(40)