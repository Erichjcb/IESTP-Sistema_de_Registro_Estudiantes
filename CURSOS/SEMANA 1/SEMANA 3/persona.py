class persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        return nombre
        return edad
    def mostrar_datos (self):
        print("Nombre",self.nombre)
        print("Edad",self.edad)
        
nombre=input("Ingrese el nombre: ")
edad=int(input("Ingrese la edad: "))       
p1=persona(nombre,edad)
p1.mostrar_datos()