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


# ##### conversion en base 10
i = 0
valBase10 = 0
while i < len(valeur):
    # print("Valeur au rang", i, ":", int(valeur[i]))
    # print("    Calcul de", valeur[i], "*", base, "^", len(valeur)-i-1)
    valBase10 = valBase10 + int(valeur[i]) * (int(base)**(len(valeur)-i-1))
    
    i = i + 1

print("=== En base 10, la valeur vaut :", valBase10, "===")

# ##### conversion en base de destination
# on trouve l'exposant maximal avec lequel on peut diviser le nombre
expoMax = 0
while(True):
    if(baseDest**(expoMax+1)) > valBase10:
        # print("    Casse car", baseDest, "^", expoMax, "=", baseDest**expoMax)
        break
    else:
        expoMax += 1
# print(expoMax)

# avec des divisions euclidiennes on convertit maintenant le nombre dans la base de destination
"""
tmpNombre = valBase10
tmpExp = expoMax
res = []
reste = valBase10
while(reste > baseDest):
    reste = tmpNombre % (baseDest**tmpExp)
    quotient = 0
    while(tmpNombre >= (baseDest**tmpExp)):
        quotient += 1
        tmpNombre -= (baseDest**tmpExp)
    res.append(quotient)
    
    # if(baseDest**(tmpExp-1) < tmpNombre):
        # res.append(0)
    
    tmpNombre = reste
    tmpExp -= 1
    print("Le reste vaut", reste)
res.append(reste)

print("Le resultat vaut", res)
"""

tmpNombre = valBase10
tmpExp = expoMax
res = []
while(tmpExp >= 0):
    tmpQuotient = 0
    # if(baseDest**tmpExp < tmpNombre):
        # res.append(0)
    while(baseDest**tmpExp <= tmpNombre):
        tmpQuotient += 1
        tmpNombre -= baseDest**tmpExp
    res.append(tmpQuotient)
    tmpExp -= 1

print("=== En base", baseDest, ", la valeur vaut", res)