from logica.calculadora import Calculadora

c = Calculadora()
c.set_valor1(int(input("Ingrese un entero: ")))
c.set_valor2(int(input("Ingrese un entero: ")))
c.sumar(5)
print(c.get_resultado())