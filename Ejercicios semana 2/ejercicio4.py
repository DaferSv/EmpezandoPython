'''Crear una lista con nombres de frutas, posteriormente hacer una función que pida 
al usuario el nombre de otra fruta y que esta sea agregada a la lista para luego 
imprimir en pantalla '''


frutas = ['papaya', 'manzana', 'guineo', 'fresa']
fruta = input("Digite el nombre de una fruta: ")
print (fruta)
frutas.append(fruta)

print("Frutas: ", frutas)