import math

a = int(input("Ingrese el area que desea halla \n 1-Areal del circulo \n 2-Area del triangulo \n 3-Area del cuadrado"))
if a==1:
    b = int(input("Ingrese el radio del circulo"))
    b= math.pi*b**2
    print("El areal del circulo es igual a: ")
    print(b)
if a==2:
    c=int(input("Ingrese el valor de la base del triangulo"))
    d=int(input("Ingrese el velor de la altura del triangulo"))
    d=(c*d)/2
    print("El area del triangulo es igual a: ")
    print(d)
if a==3:
    e=int(input("Ingrese el valor de uno de los lados del cuadrado"))
    e=e*e;
    print("El areal del cuadrado es igual a: ")
    print(e)