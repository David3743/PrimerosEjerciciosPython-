import math

A = int(input("Ingrese el tipo de dato al que desea convertir:\n 1-radianes \n 2-Grados"))
if A==1:
    b  = float(input("Ingrese el numero que desea convertir a radianes"))
    g:float= math.radians(b)
    print("El numero ingresado en radianes es igual a: ")
    print(g)
else:
    c = float(input("Ingrese el numero que desea convertir a grados"))
    e = math.degrees(c)
    print("El  numero en grados es igual a: ")
    print(e)
