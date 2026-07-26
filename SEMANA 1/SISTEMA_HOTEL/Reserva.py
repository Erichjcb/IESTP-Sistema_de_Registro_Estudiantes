class Reserva:
    def __init__(self,habitacion,huesped):
        self.habitacion=habitacion
        self.huesped=huesped
        
    def mostrar(self):
        print("====RESERVA====")
        print("Huesped: ", self.huesped.nombre)
        print("Habitacion: ",self.habitacion.numero)
        print("Tipo: ",self.habitacion.tipo)
        