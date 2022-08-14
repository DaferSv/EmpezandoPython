'''Escribir las funciones que permitan calcular la suma, resta, multiplicación, división, 
exponente y módulo. Las funciones recibirán como parámetros dos números y 
mostrará por pantalla el resultado con un mensaje. '''

'''Ejercicio de calculadora basica'''
import math
from unittest import result
#Informacion para el usuario para que se ubique que operaciones matematicas puede realizar
print("Bienvenidos al programa de calculadora")
print("1-Suma")
print("2-Resta")
print("3-Multiplicacion")
print("4-Division")
print("5-Exponente")
print("6-Modulo")

#Escoger una opcion de X operacion matematica disponible
x = int(input("Escoga una de las opciones de calculo disponible: "))\

#Pedirle que digite 2 numeros se le pide en float porque puede digitar algun decimal para alguna operacion
a = float(input("Digite el primer numero: "))
b = float(input("Digite el segundo numero: "))
def funcionMath (a1,b1,x1):
#Procesos para realizar los diferentes operaciones matematicas propuestas por el ejercicio
    if x1 == 1:
        result = a1 + b1
    if x1 == 2:
        result = a1 - b1  
    if x1 == 3:
        result  = a1 * b1
    if x1 == 4:
        result = a1 / b1
    if x1 == 5: 
        result = a1**b1
    if x1 == 6:
        result = a1 % b1
    return  (result)
print(funcionMath(a,b,x))


