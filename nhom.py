from random import *
import time

gender = input("Qual o pronome do seu catto? ").lower()

if gender in "ele dele e".split():
    genderNoun = "do seu gatinyo? "
    pronoun = "ele"
elif gender in "ela dela a".split():
    genderNoun = "da sua gatinya? "
    pronoun = "ela"
else:
    genderNoun = "de seu gatinye? "
    pronoun = "elx"

nome = input("Qual o nome " + genderNoun)

alt = [(i.lower(), i.upper()) for i in "n h o m".split()]

alt.append(("", " ", "\n"))

nhomCount = int(input("Quantos nhomnhom " + pronoun + " merece? "))

start_time = time.time()
for i in range(nhomCount):
    if i == 0:
        print(nome)
    print("".join(map(choice,alt)), end="")

print("--- %s seconds ---" % (time.time() - start_time))
