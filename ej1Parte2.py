"""
Ejercicio 1
Pedir un número por teclado y mostrar la tabla de multiplicar
"""

a=int(input("\nIngrese un número\n"))
print("\nLa trabla de multiplicar del "+ str(a) , "es:\n")
for x in range(11):
    c=a*x
    print(str(a),"* "+str(x), " = " + str(c))

