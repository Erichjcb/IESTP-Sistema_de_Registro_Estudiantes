class persona:
    def __init__(self):
        self.__edad = 0
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self,edad):
        self.__edad=edad
        
        
        
pers1= persona()
pers1.set_edad(18) # El set modifica al valor de la variable
print(pers1.get_edad())


        