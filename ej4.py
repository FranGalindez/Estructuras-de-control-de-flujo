"""
Ejercicio 4
Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
"""

a=input("\nNombre de usuario:\n")
b=input("\nIngrese contraseña:\n")
usuario= "pepe"
contraseña = "asdasd"
if a==usuario and contraseña==b:
    print("\nHas entrado al sistema")
else:
    print("Error")