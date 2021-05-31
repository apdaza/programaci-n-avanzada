f = open("archivos2.txt", "w")
f.write("Una linea de escritura de ejemplo \n")
f.close()

f = open("archivos2.txt", "a")
f.write("Otra linea de escritura de ejemplo \n")
f.write(input("Ingrese una linea al archivo"))
f.close()

f = open("archivos2.txt", "r")
for l in f.readlines():
    print(l)

f.close()

