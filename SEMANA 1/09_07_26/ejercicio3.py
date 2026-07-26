class alumno:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        

datos=[]

while True:

    print("---DATOS DEL ESTUDIANTE---")
    print("1.Registrar datos")
    print("2.Mostrar datos")
    print("3.Limpiar datos")
    print("4.Salir")
    
    opcion=int(input("Ingrese una opción: "))


    if opcion==1:
        nomb=input("Ingrese su nombre: ")
        age=int(input("Ingrese su edad: "))
        dato1=alumno(nomb,age)
        datos.append(dato1)
        
    elif opcion==2:
        if len(datos)==0:
            
            print('No hay datos registrados')
        else:
            for i in datos:
                print(f'Nombre: {i.nombre}')
                print(f'Edad: {i.edad}')
    elif opcion==3:
        datos.clear()
        print("Se limpiaron los datos registrados")

    elif opcion==4:
        print("Fin del programa")
        break
    
