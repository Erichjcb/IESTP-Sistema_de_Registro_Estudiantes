class Animal:
    def sonido(self):
        print("El animal emite un sonido")

class Perro(Animal):
    def sonido(self):
        super().sonido()
        print("GUAU GUAU")

class Gato(Animal):
    def sonido(self):
        super().sonido()
        print("Miau Miau")

g1 = Gato()
g1.sonido()

a1 = Perro()
a1.sonido()


