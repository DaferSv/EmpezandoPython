#Ejercicio del interes anual de un activo
#Cantidad dinero a invertir
#Interes anual de esa inversion
#Numero de años de esa inversion
#Capital obtenido luego de esos años

inversion = float (input("Ingrese la cantidad a invertir: "))
interes = float (input("Ingrese el interés anual: "))
años = int (input("Ingrese el número de años: "))


for x in range(años):
    inversion = inversion * (1 + interes/100)
    print("El capital obtenido será $",inversion)