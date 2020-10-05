numero = int(input("ingrese un entero: "))

dicionario = {1: "muy bajo", 2: "aun muy bajo", 3: "ya casi"}

if numero in dicionario:
    print(dicionario[numero])
else:
    print("Muy bien")
