class notas:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def verificar (self):
        
        if self.nota>=13:
            print(f'{self.nombre}, usted está aprovado y su nota es de {self.nota}')
        else:
            print(f'{self.nombre}, usted está desaprovado y su nota es de {self.nota}')
nomb=input("Ingrese el nombre: ")
nota1=int(input("Ingrese la nota: "))       
n1=notas(nomb,nota1)
n1.verificar()
