'''Crear una función que devuelva
 el área de un círculo a partir de su radio. '''

 
import math

radio=float((input("ingrese el radio del circulo a calcaular:")))

def radiomifuncion (radio1):
    radio=(math.pi) *(radio1**2)

    return radio
print(radiomifuncion(radio))
