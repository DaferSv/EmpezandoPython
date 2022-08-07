#Obteniendo las notas de un alumno
print("========================================")
print("|    Programa para saber mis notas     |")
print("========================================")

print("")
nombre  = input("Digite su nombre: ")
print("========================================")
lab1    = float(input("Digite la nota del primer laboratorio: "))
print("========================================")
lab2    = float(input("Digite la nota del segundo laboratorio: "))
print("========================================")
parcial = float(input("Digite la nota del parcial: "))
print("========================================")

lab1    = lab1*0.3
lab2    = lab2*0.3
parcial = parcial*0.4

notaTotal = lab1+lab2+parcial

print("La nota total del estudiante "+nombre+" es: ",notaTotal)
