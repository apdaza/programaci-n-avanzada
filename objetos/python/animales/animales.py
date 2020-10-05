class Animal:
    def despedirse(self):
        print("chao")

    def alimentar(self):
        pass


class Perro(Animal):

    def alimentar(self):
        print("Gracias por alimentarme, guau")


class Gato(Animal):

    def alimentar(self):
        print("Gracias por alimentarme, miau")


class PerroGato(Perro, Gato):
    pass

a = PerroGato()

a.alimentar()
a.despedirse()