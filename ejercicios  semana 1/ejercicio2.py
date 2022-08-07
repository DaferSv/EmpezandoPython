#Ejercicio de tienda 
from unicodedata import name


print("===================================")
print("Bienvenido al sistema de tienda ")
print("===================================")

# Se le piden los datos respectivos al usuario
NameProduct = input("Nombre del producto: ")
print("===================================")
cantidad = int(input("Cantidad del producto: "))
print("===================================")
precio = float(input("Precio del producto: "))
print("===================================")
Total = cantidad*precio
print("El total de su compra es: $",Total)




