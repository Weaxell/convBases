
#coding: utf-8
import os

os.system("clear")

print("=== Conversion de bases ===")
valeur = input("Entrez une valeur : ")
base = int(input("Entrez la base : "))
baseDest = int(input("Entrez la base de conversion : "))
print("Longueur :", len(valeur))

exposant = 1
res = 0
print("Chaine :", valeur)
# conversion en base 10
i = 0
while i < len(valeur):
    print("Valeur au rang", i, ":", valeur[int(i)-1])
    i = i + 1

