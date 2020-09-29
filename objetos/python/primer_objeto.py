class Persona():
    def __init__(self, nombre, apellido):
        self.__nombre__ = nombre
        self.__apellido__ = apellido

    def get_nombre(self):
        return self.__nombre__

    def get_apellido(self):
        return self.__apellido__

class Saludador():
    def __init__(self, persona):
        self.__persona__ = persona

    def saludar(self, msg):
        return msg + self.__persona__.get_nombre() + " " + self.__persona__.get_apellido()
        

p = Persona("Alejandro", "Daza")
s = Saludador(p)
print(s.saludar("Hola "))