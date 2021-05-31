class Calculadora:

    def __init__(self):
        self.__valor1__ = 0
        self.__valor2__ = 0
        self.__resultado__ = 0

    def set_valor1(self, valor):
        self.__valor1__ = valor

    def set_valor2(self, valor):
        self.__valor2__ = valor

    def get_resultado(self):
        return self.__resultado__

    def sumar(self, valor = None):
        if valor == None:
            self.__resultado__ = self.__valor1__ + self.__valor2__
        else:    
            self.__resultado__ = self.__valor1__ + self.__valor2__ + valor
    
    def restar(self):
        self.__resultado__ = self.__valor1__ - self.__valor2__

    def multiplicar(self):
        self.__resultado__ = self.__valor1__ + self.__valor2__

    def dividir(self):
        self.__resultado__ = self.__valor1__ + self.__valor2__