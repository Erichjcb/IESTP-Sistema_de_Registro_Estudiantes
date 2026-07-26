from Producto import Producto

lista=[]


while True:

print("---SISTEMA DE PRODUCTO---")
print("1.Registrar Producto")
print("2.Mostrar Producto")
print("3.Salir")

opcion=input("Seleccione una opción")

if opcion==1:
    nom=input("Nombre del producto: ")
    pre=float(input("Precio: "))
    pro1=Producto(nom,pre)
    lista.append()
    
    print("Registro correctamente")

    lista.append(nom,pre)

elif opcion=="3":
    print("Gracias por utilizar el sistema")
    
elif:
    print("Elige otra opción")