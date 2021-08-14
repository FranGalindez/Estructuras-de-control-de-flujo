"""
Ejercicio 4¶
Dado una lista, hacer un programa que indique si está ordenada o no.
"""

lista = []


a=1
c=1
while a==c:
    ingreso=(input("\nIngrese los números de la lista, cuando no quiera ingresar más númeors, ingrese la letra t\n"))
    if ingreso !="t":
        lista.append(ingreso)
    else:
        break

lista1 = lista.copy()
lista1.sort()
if lista!=lista1:
    print("\nLa lista no está ordenada\n")
else:
    print("\nLa lista está ordenada\n")




