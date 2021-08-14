"""
Ejercicio 1
Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero.
"""

a=int(input("Ingrese dos números: \n"))
b=int(input())
c=a+b
if c<0:
    print("\nLa suma de los dos números es negativa")
elif c==0:
    print("\nLa suma de los dos números es igual a 0")
else:
    print("\nLa suma de los dos números es positiva")

    