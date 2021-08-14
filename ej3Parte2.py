"""
Ejercicio 3
Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número entero por teclado.
 A continuación va pidiendo números y va respondiendo
 si el número a adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número.
"""

numero_adivinar=int(input("\nIngrese el número que quiere que adivine\n"))
aproximacion=int(input("\nIngrese un nuevo número\n"))
a=1
c=1
while a==c:
    if aproximacion==numero_adivinar:
        print("\n¡Adivinaste el número!\n")
        c+=1
    elif aproximacion<numero_adivinar:
        print("\nEl número que ingresaste es menor, ingrese otro:\n")
        aproximacion=int(input())
    else:
        print("\nEl número que ingresaste es mayor, ingrese otro número:\n")
        aproximacion=int(input())

        
