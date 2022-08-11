'''Ejercicio de calculadora basica'''
import math
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

#Procesos para realizar los diferentes operaciones matematicas propuestas por el ejercicio
if x == 1:
    result = a + b
    print ("El resultado de la operacion es: ",result)
if x == 2:
    result = a - b  
    print ("El resultado de la operacion es: ",result)
if x == 3:
    result  = a * b
    print ("El resultado de la operacion es: ",result)
if x == 4:
    result = a / b
    print ("El resultado de la operacion es: ",result)
if x == 5: 
    result = a**b
    print ("El resultado de la operacion es: ",result)
if x == 6:
    result = a % b
    print ("El resultado de la operacion es: ",result)


