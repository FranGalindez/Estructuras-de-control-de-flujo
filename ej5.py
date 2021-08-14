"""
Ejercicio 5
Escribir un programa que lea un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
"""

año=int(input("\nIngrese un año:\n"))
if (año%4==0 or año%400==0) and año%100!=0:
    print("\nEl año " + str(año), "es bisiesto")
else:
    print("\nEl año " + str(año), "no es bisiesto")

