class Estudiante:
    def __init__(self,nombre,nota1,nota2):.
        self.nota1=nota1
        self.nota2=nota2
        
    lista=[]
    
    for i in range(2):
        nomb=input("Ingrese el nombre: ")
        n1=float(input("Ingrese la nota 1: "))
        n2=float(input("Ingrese la nota 2: "))
        
        variable = Estudiante(nomb,n1,n2)
        lista.append(variable)
        
    print("\nLISTA DE ESTUDIANTE")
    
    for i in lista:
        promedio=(i.nota1+i.nota2)/2
        
        if promedio>=13:
            estado="Aprobado"
            
        else:
            estado="Desaprobado"
            
        print("\n El promedio y el estado del alumno")
        
        
    def mostrar(self):
        print(f"El precio del producto {i}")