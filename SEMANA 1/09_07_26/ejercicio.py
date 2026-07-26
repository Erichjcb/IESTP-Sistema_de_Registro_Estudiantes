while True:

    print("---OPERACIONES---")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("4.Salir")

    opcion=int(input("Ingrese una opción: "))


    if opcion==1:
        n1=float(input("Ingrese el primer número: "))
        n2=float(input("Ingrese el segundo número: "))
        suma=n1+n2
        print(f'La suma de los dos números es: {suma}')
        
    elif opcion==2:
        n1=float(input("Ingrese el primer número: "))
        n2=float(input("Ingrese el segundo número: "))
        resta=n1-n2
        print(f'La resta de los dos números es: {resta}')
    elif opcion==3:
        n1=float(input("Ingrese el primer número: "))
        n2=float(input("Ingrese el segundo número: "))
        multiplicar=n1*n2
        print(f'La resta de los dos números es: {multiplicar}')
    elif opcion==4:
        n1=float(input("Ingrese el primer número: "))
        n2=float(input("Ingrese el segundo número: "))
        division=n1/n2
        print(f'La división de los dos números es: {division}')
    elif opcion==5:
        print("Fin del programa")
        break