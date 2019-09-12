#coding: utf-8
import os
import platform

# effacement de l'ecran
if(platform.system() == 'Windows'):
    os.system("cls")
else:
    os.system("clear")

print("=== Conversion de bases ===")
valeur = input("Entrez une valeur : ")
base = int(input("Entrez la base : "))
baseDest = int(input("Entrez la base de conversion : "))

print("Chaine :", valeur)


# conversion en base 10
i = 0
res = 0
while i < len(valeur):
    # print("Valeur au rang", i, ":", int(valeur[i]))
    # print("    Calcul de", valeur[i], "*", base, "^", len(valeur)-i-1)
    res = res + int(valeur[i]) * (int(base)**(len(valeur)-i-1))
    
    i = i + 1

print("=== En base 10, la valeur vaut :", res, "===")

# conversion en base de destination
