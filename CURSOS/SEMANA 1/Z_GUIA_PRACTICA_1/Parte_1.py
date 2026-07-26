class REGISTRO:

    def __init__(self, codigo, nombre, programa, ciclo):
        self.codigo = codigo
        self.nombre = nombre
        self.programa = programa
        self.ciclo = ciclo


estudiantes = []

while True:
    print("\n=== SISTEMA DE ESTUDIANTES ===")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Modificar estudiante")
    print("5. Eliminar estudiante")
    print("6. Salir")

    try:
        opcion = int(input("Ingrese la opción a elegir: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue

    if opcion == 1:
        try:
            codigo = int(input("Ingresa tu código de estudiante: "))
        except ValueError:
            print("Error: El código debe ser un número entero.")
            continue

        nombre = input("Ingresa tu nombre: ")
        programa = input("Ingrese tu programa de estudios: ")
        ciclo = input("Ingrese el ciclo que cursas: ")

        dato_nuevo = REGISTRO(codigo, nombre, programa, ciclo)
        estudiantes.append(dato_nuevo)
        print("Estudiante registrado correctamente.")

    elif opcion == 2:
        if len(estudiantes) == 0:
            print("No existen estudiantes registrados.")
        else:
            print("\n=== LISTA DE ESTUDIANTES ===")
            for i in estudiantes:
                print(f"Código: {i.codigo}")
                print(f"Nombre: {i.nombre}")
                print(f"Programa: {i.programa}")
                print(f"Ciclo: {i.ciclo}")
                print("-" * 20)

    elif opcion == 3:
        try:
            buscar = int(
                input("Ingrese el código del estudiante que quiere buscar: ")
            )
        except ValueError:
            print("Error: El código de búsqueda debe ser numérico.")
            continue

        encontrado = False
        for i in estudiantes:
            if i.codigo == buscar:
                print("==== Estudiante encontrado ====")
                print(f"Código: {i.codigo}")
                print(f"Nombre: {i.nombre}")
                print(f"Programa: {i.programa}")
                print(f"Ciclo: {i.ciclo}")
                encontrado = True
                break
        if not encontrado:
            print(f"El código '{buscar}' no se encuentra registrado.")

    elif opcion == 4:
        try:
            codigo_mod = int(
                input("Ingrese el código del estudiante a modificar: ")
            )
        except ValueError:
            print("Error: El código a modificar debe ser numérico.")
            continue

        encontrado = False
        for i in estudiantes:
            if i.codigo == codigo_mod:
                print("\n=== Ingrese los nuevos datos ===")
                i.nombre = input("Ingresa el nuevo nombre: ")
                i.programa = input("Ingrese el nuevo programa de estudios: ")
                i.ciclo = input("Ingrese el nuevo ciclo: ")
                print("Estudiante modificado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró el código '{codigo_mod}' para modificar.")

    elif opcion == 5:
        try:
            codigo_delete = int(input("Ingrese el código a eliminar: "))
        except ValueError:
            print("Error: El código a eliminar debe ser numérico.")
            continue

        encontrado = False
        for i in estudiantes:
            if i.codigo == codigo_delete:
                estudiantes.remove(i)
                print(f"Registro de '{i.codigo}' eliminado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró el código '{codigo_delete}' para eliminar.")

    elif opcion == 6:
        print("\nGracias por utilizar el sistema")
        print("Programa finalizado")
        break

    else:
        print("\nOpción incorrecta: Intente nuevamente")