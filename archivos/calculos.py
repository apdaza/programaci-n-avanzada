from random import randint

f = open("calculos.txt", "w")

for i in range(5):
    a = randint(1,100)
    b = randint(1,100)
    c = input(str(a) + " + " + str(b) + " = ")
    f.write(str(a)+","+str(b)+","+str(c)+"\n")
f.close()

f = open("calculos.txt", "r")
for linea in f.readlines():
    elementos = [int(x) for x in linea.split(",")]
    if elementos[0] + elementos[1] == elementos[2]:
        print(str(elementos[0])+" + "+str(elementos[1])+" = "+str(elementos[2])+" ok ")
    else:
        print(str(elementos[0])+" + "+str(elementos[1])+" = "+str(elementos[2])+" no ")
