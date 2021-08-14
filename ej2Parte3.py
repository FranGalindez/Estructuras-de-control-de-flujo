"""
Ejercicio 2
Realizar un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida.
 Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
"""

texto=input("Ingrese un texto:\n")
listita =texto.split()
listita.reverse()

print(listita)