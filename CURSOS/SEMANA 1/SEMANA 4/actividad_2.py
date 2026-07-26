class Empleado:
    def __init__(self,nombre,sueldo):
        self.nombre=nombre
        self.sueldo=sueldo
    
    def incremento_sueldo(self):
        self.sueldo+=self.sueldo*0.1
        print(f'El nuevo sueldo con un incremento del 10% es {self.sueldo}')
        

e1=Empleado("Jorge",2000)
e1.incremento_sueldo()
        