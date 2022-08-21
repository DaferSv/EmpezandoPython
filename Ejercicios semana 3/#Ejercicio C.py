#Ejercicio C
'''
Crear un programa que funcione como el cajero de un supermercado, donde vaya
leyendo el código, nombre, cantidad y precio del producto al final de cada producto
pregunte al usuario si desea ingresar otro producto, si es así deberá pedir otra vez los
datos y si se indica que no en pantalla se escribirá una factura con los detalles de la
compra. Ej

Codigo------Nombre--------Cantidad-----Total
Codigo------Nombre--------Cantidad-----Total
Codigo------Nombre--------Cantidad-----Total
                                1. Total Final
                                
Se deberá preguntar al usuario si va a pagar en tarjeta o en efectivo.
Si paga en efectivo:
Si el usuario excede de $50 se le hará un descuento del 10%, si excede del
$100 se le hará un descuento del 30%.
Si paga con tarjeta:
Si el usuario excede de $50 se le hará un descuento del 20%, si excede del
$100 se le hará un descuento del 40%.
Mostrar el total descontado de la compra al final de la ejecución.
'''
total = 0
productos={}
while True:
    print("================================================================")
    codigo= input("Codigo: ")
    producto = input("Nombre producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    subtotal=round(cantidad * precio, 2)
    total += subtotal
    productos[producto]=(codigo,cantidad,precio,subtotal)
    continuar = input("Presionar 0 para calcular o enter para ingresar otro producto: ")
    if continuar == "0":
        print("================================================================")
        print("Productos: ")
        print("================================================================")
        print("==CODIGO=====NOMBRE======CANTIDAD=====PRECIO U====PRECIO TOTAL")
        print("================================================================")
        [print("-",productos[p][0],"-->:","-",p,"--> Cantidad:",productos[p][1],"unidades --> Precio c/u:",productos[p][2],"dolares --> Subtotal:",productos[p][3],"dolares") for p in productos]
        print("================================================================")
        print("Pagara con tarjeta o efectivo? ")
        metodo_pago= input("tarjeta escriba 1 o efectivo 2: ")
        
        print("================================================================")
        print("Precio total:", round(total, 2), "dolares")
        if metodo_pago == "1":
            if total <= 49.99 and total >= 99.99:
                total = total-(total*0.20)
                print("Precio final:", round(total, 2), "dolares, menos el 20%")
            elif total > 9.99:
                total= total-(total*0.40)
                print("Precio final:", round(total, 2), "dolares, menos el 40%")
            else:
                print("Precio final:", round(total, 2), "dolares, sin descuento")
        elif metodo_pago == "2":
            if total <= 49.99 and total >= 99.99:
                total = total-(total*0.10)
                print("Precio final:", round(total, 2), "dolares, menos el 10%")
            elif total > 9.99:
                total= total-(total*0.30)
                print("Precio final:", round(total, 2), "dolares, menos el 30%")
            else:
                print("Precio final:", round(total, 2), "dolares, sin descuento")
        else:
            print("Precio total:", round(total, 2), "dolares")
        iva= total*0.13
        total = total+iva
        print("IVA: ",round(iva,2))
        print("================================================================")
        print("Precio final de la compra mas IVA: ", total)
        print("================================================================")
        break
