from Cliente import Cliente
from Producto import Producto
from Ventas import Ventas
n1=input("Ingrese el nombre del cliente: ")
a1=input("Ingrese el nombre del producto: ")
p1=int(input("Ingrese el precio del producto: "))
c1=int(input("Ingrese la cantidad de productos: "))

prod=Producto(a1,p1,c1)
cli1=Cliente(n1)
boleto=Ventas(cli1,prod)
 
boleto.mostrar()