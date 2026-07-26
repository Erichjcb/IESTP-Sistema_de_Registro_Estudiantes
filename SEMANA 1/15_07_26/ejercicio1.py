class Agenda:
    def __init__(self, nombre, celular):
        self.nombre = nombre
        self.celular = celular


registros = []

while True:
    print("\n=== AGENDA ===")
    print("1. Registrar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Eliminar")
    print("5. Salir")

    try:
        opcion = int(input("Ingrese la opción a elegir: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue

    if opcion == 1:
        nombre = input("Ingresa tu nombre: ")
        celular = input("Ingrese su número de celular: ")
        dato_nuevo = Agenda(nombre, celular)
        registros.append(dato_nuevo)
        print("Se registró exitosamente los datos.")

    elif opcion == 2:
        if len(registros) == 0:
            print("No hay registros.")
        else:
            print("\n=== LISTA DE REGISTROS ===")
            for i in registros:
                print(f"Nombre: {i.nombre}")
                print(f"Celular: {i.celular}")

    elif opcion == 3:
        buscar = input("Ingrese el nombre que quiere buscar: ")
        encontrado = False
        for i in registros:
            if i.nombre.lower() == buscar.lower():
                print("Nombre encontrado.")
                print(f"El celular de {i.nombre} es {i.celular}.")
                encontrado = True
                break
        if not encontrado:
            print(f"El nombre '{buscar}' no se encuentra registrado.")

    elif opcion == 4:
        nombre_delete = input("Ingrese el nombre a eliminar: ")
        encontrado = False
        for i in registros:
            if i.nombre.lower() == nombre_delete.lower():
                registros.remove(i)
                print(f"Registro de '{i.nombre}' eliminado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró el nombre '{nombre_delete}' para eliminar.")

    elif opcion == 5:
        print        