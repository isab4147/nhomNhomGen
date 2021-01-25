from random import *

nome = input("Qual o nome da sua gatinya? ")

alt = [(i.lower(), i.upper()) for i in "n h o m".split()]

alt.append(("", " ", "\n"))

for i in range(int(input("Quantos nhomnhom ela merece? "))):
    if i == 0:
        print(nome)
    print("".join(map(choice,alt)), end="")
