class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info_vehiculo(self):
        
        print(f'El auto es de la marca {self.marca} y del modelo {self.modelo}')


a1 = Auto("Toyota","Tercel")

a1.info_vehiculo()