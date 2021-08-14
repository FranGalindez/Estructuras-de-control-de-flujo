"""
Ejercicio 1
Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. 
Muestra el máximo de los números guardado en la lista, muestra los números pares.
"""

lista = []
pares =[]
a=1
c=1
b=0
while a==c:
    ingreso=int(input("\nIngrese un número\n"))
    if ingreso>=0:
        lista.append(ingreso)
    else:
        j=max(lista)
        print("\nEl número más grande de la lista es " , str(j))
        break
        
for x in range(len(lista)):
    if lista[x]%2==0:
        pares.append(lista[x])
    else:
        continue       

print("\nLos números pares de la lista son: " + str(pares))

