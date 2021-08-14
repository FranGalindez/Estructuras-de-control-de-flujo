"""
Ejercicio 5
Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad.


"""
def es_primo(a):
    for x in range(2, a):
        if a % x == 0:
            print("No es primo porque", x, "lo divide")
            return False
    print("Es primo")
    return True

es_primo(a=int(input("\nIngrese un número y le diré si es primo\n")))
    