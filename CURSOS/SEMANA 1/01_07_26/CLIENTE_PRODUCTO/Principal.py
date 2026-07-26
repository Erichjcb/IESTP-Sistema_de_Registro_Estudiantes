from Cliente import Cliente
from Producto import Producto
from Ventas import Ventas
nom=input("DIME EL NOMBRE:")
pro=input("DIME EL PRODUCTO:")
pre=input("DIME EL precio:")
a=Cliente(nom)
b=Producto(pro,pre)
vent=Ventas(a,b)
vent.mostrar()