while True:

    print("---MENÚ---")
    print("1.Registrar")
    print("2.Mostrar nombre")
    print("3.Mostrar carrera")
    print("4.Salir")

    opcion=int(input("Ingrese una opción: "))


    if opcion==1:
        
        print('Bienvenido al sistema')
        nom=input("Ingrese su nombre: ")
        
    elif opcion==2:
        
        print(F'Su nombre es {nom}')
        break
        
    elif opcion==3:
        carrera=input("Ingresar el nombre de la carrera: ")
        print(f'La carrera es : {carrera}')
        break
        

    elif opcion==4:
        print("Fin del programa")
        break