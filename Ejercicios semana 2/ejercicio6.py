'''Crear un código donde una función reciba una lista de números ya hecha y 
devuelva el promedio '''


#este ejercico esta echo para poder devolver un promedio de un alisat atraves de un array 

lista=[54, 48, 47, 46, 56, 37, 64, 46, 8, 58, 67, 14, 85, 73, 67, 43, 89, 30, 67, 82]
 


def promedio_std(lista):
    x = 0

    x = sum(lista) /len(lista)
    total = 0.0
    return x
 
print(promedio_std(lista))
