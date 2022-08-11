def creador_dict(cadena):
  '''Recibe una cadena de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)'''
  list_1= cadena.split()
  dict_1={}
  for i in list_1:
    if i in dict_1:
      dict_1[i] +=1
    else:
      dict_1[i]= 1
  return dict_1

def contador_dict(dictionario):
  '''Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece'''
  palabra_frecuente= ''
  cantidad=0
  for keys,values in dictionario.items():
    if values > cantidad:
      cantidad= values
      palabra_frecuente= keys
  return palabra_frecuente,cantidad
entrada=input('Ingrese su cadena de caracteres: ')
print(creador_dict(entrada))
print(contador_dict(creador_dict(entrada)))