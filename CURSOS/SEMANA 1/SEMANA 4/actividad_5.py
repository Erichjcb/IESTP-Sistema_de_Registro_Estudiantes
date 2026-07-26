class Videojuego:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

    def aumento_puntaje(self, puntos_extra):
       
        self.puntaje += puntos_extra
        print(f'El nuevo puntaje de {self.nombre} es: {self.puntaje}')

v1 = Videojuego("Super Mario", 20)

v1.aumento_puntaje(15)