'''Escribir una función que convierta un número decimal en hexadecimal y otra que 
convierta un número hexadecimal en decimal.                                                                                           '''
# Función que regresa el verdadero valor hexadecimal.
# Por ejemplo, si recibe un 15 devuelve f, y si recibe un número menor a 10, devuelve el número sin modificarlo
def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


decimal = int(
    input("Escribe un número decimal, y yo lo convertiré a hexadecimal por ti: "))
hexadecimal = decimal_a_hexadecimal(decimal)
print(f"El decimal {decimal} es {hexadecimal} en hexadecimal")