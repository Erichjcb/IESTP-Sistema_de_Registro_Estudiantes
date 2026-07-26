class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def calcular_area_rectangulo(self):
        area=self.base*self.altura
        print(f'El área del rectangulo es: {area}')
        
        
    
r1=Rectangulo(10,12)
r1.calcular_area_rectangulo()    