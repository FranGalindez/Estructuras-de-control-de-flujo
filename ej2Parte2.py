"""
Ejercicio 2
Crea una aplicación que pida un número y calcule su factorial
 (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa
  por el número seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120
"""
numero=int(input("\nIngrese un número:\n"))
def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(numero))
    
