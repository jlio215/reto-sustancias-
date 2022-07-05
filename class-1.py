from math import floor


def brebaje(sustancia):
    if 0<sustancia<=20:
        print("uno")
    elif 20<sustancia<=40:
        print("dos")
    elif 40<sustancia<=80:
        print("tres")
    elif 80<sustancia:
        print("cuatro")
    else:
        print("No se puede elaborar brebaje sin sustancias")
A= int(input())
B= (2*A)+4
C= floor(((3*A)+4)/5)
print(A,B,C)
brebaje(C)

