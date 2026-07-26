class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


productos = []

while True:
    print("\n=== SISTEMA DE PRODUCTOS ===")
    print("1. Registrar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        nuevo_producto = Producto(nombre, precio)
        productos.append(nuevo_producto)
        print("Producto registrado correctamente.")

    elif opcion == 2:
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("\n=== LISTA DE PRODUCTOS ===")
            for p in productos:
                print(f"Nombre: {p.nombre}")
                print(f"Precio: {p.precio}")

    elif opcion == 3:
        buscar = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for p in productos:
            if p.nombre.lower() == buscar.lower():
                print("Producto encontrado:")
                print(f"Nombre: {p.nombre}")
                print(f"Precio: {p.precio}")
                encontrado = True
                break
        if not encontrado:
            print(f"El producto '{buscar}' no se encuentra registrado.")

    elif opcion == 4:
        print("Fin del programa.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
