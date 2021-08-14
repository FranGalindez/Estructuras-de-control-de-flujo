"""
Ejercicio 3
Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
"""

meses = {
    "1": "Enero",
    "2": "Febrero",
    "3": "Marzo",
    "4": "Abril",
    "5": "Mayo" ,
    "6": "Junio" ,
    "7": "Julio" ,
    "8": "Agosto",
    "9": "Septiembre",
    "10": "Octubre",
    "11": "Noviembre",
    "12": "Diciembre"

}

a=int(input("Ingrese un número del 1 al 12\n"))

if a>=1 and a<=12:
        print("\nEl número " + str(a), "corresponde al mes: " + meses[str(a)])
