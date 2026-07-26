class REGISTRO:

    def __init__(self, placa, marca, modelo, color):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color


vehiculos = []

while True:
    print("\n=== SISTEMA DE VEHICULAR ===")
    print("1. Registrar vehículo")
    print("2. Mostrar vehículo")
    print("3. Buscar vehículo")
    print("4. Modificar vehículo")
    print("5. Eliminar vehículo")
    print("6. Salir")

    try:
        opcion = int(input("Ingrese la opción a elegir: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue

    if opcion == 1:
        try:
            placa = int(input("Ingresa la placa del vehículo: "))
        except ValueError:
            print("Error: La placa debe ser un número entero.")
            continue

        marca = input("Ingresa la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        color = input("Ingrese el color del vehículo: ")

        dato_nuevo = REGISTRO(placa, marca, modelo, color)
        vehiculos.append(dato_nuevo)
        print("El vehículo ha sido registrado correctamente.")

    elif opcion == 2:
        if len(vehiculos) == 0:
            print("No existen vehículos registrados.")
        else:
            print("\n=== LISTA DE VEHÍCULOS ===")
            for i in vehiculos:
                print(f"Placa: {i.placa}")
                print(f"Marca: {i.marca}")
                print(f"Modelo: {i.modelo}")
                print(f"Color: {i.color}")
                print("-" * 20)

    elif opcion == 3:
        try:
            buscar = int(
                input("Ingrese la placa del vehículo que quiere buscar: ")
            )
        except ValueError:
            print("Error: La placa de búsqueda debe ser numérico.")
            continue

        encontrado = False
        for i in vehiculos:
            if i.placa == buscar:
                print("==== Vehículo encontrado ====")
                print(f"Placa: {i.placa}")
                print(f"Marca: {i.marca}")
                print(f"Modelo: {i.modelo}")
                print(f"Color: {i.color}")
                encontrado = True
                break
        if not encontrado:
            print(
                f"El vehículo de placa '{buscar}' no se encuentra registrado."
            )

    elif opcion == 4:
        try:
            codigo_mod = int(
                input("Ingrese la placa del vehículo a modificar: ")
            )
        except ValueError:
            print(
                "Error: El vehículo a modificar debe tener placa de valor numérico."
            )
            continue

        encontrado = False
        for i in vehiculos:
            if i.placa == codigo_mod:
                print("\n=== Ingrese los nuevos datos ===")
                try:
                    i.placa = int(input("Ingresa el nuevo número de placa: "))
                except ValueError:
                    print("Error: La placa debe ser numérica.")
                    encontrado = True
                    break
                i.marca = input("Ingrese la nueva marca: ")
                i.modelo = input("Ingrese el modelo: ")
                i.color = input("Ingrese el nuevo color: ")
                print("El vehículo ha sido modificado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print(
                f"No se encontró el número de placa '{codigo_mod}' para modificar."
            )

    elif opcion == 5:
        try:
            codigo_delete = int(
                input("Ingrese la placa del vehículo a eliminar: ")
            )
        except ValueError:
            print("Error: La placa a eliminar debe ser numérico.")
            continue

        encontrado = False
        for i in vehiculos:
            if i.placa == codigo_delete:
                print(
                    f"Registro del número de placa '{i.placa}' eliminado correctamente."
                )
                vehiculos.remove(i)
                encontrado = True
                break
        if not encontrado:
            print(
                f"No se encontró la placa del vehículo '{codigo_delete}' para eliminar."
            )

    elif opcion == 6:
        print("\nGracias por utilizar el sistema")
        print("Programa finalizado")
        break

    else:
        print("\nOpción incorrecta: Intente nuevamente")