class numero:
    def __init__(self,valor):
        self.valor=valor
    
    def par_o_impar(self):
        if self.valor%2==0:
            print("El valor es par")
            
           
        else:
            print("El valor es impar")    
         
valor=int(input("Ingrese el valor: "))


v1=numero(valor)
v1.par_o_impar()