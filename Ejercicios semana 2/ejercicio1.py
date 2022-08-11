import math
print("Bienvenidos al programa de calculadora")
print("1-Suma")
print("2-Resta")
print("3-Multiplicacion")
print("4-Division")
print("5-Exponente")
print("6-Modulo")
x = int(input("Escoga una de las opciones de calculo disponible: "))
a = float(input("Digite el primer numero: "))
b = float(input("Digite el segundo numero: "))
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


