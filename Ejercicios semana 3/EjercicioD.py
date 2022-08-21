
# creamos nuestra clase libreria
class Libreria:
	
	def __init__(self):
		# crearemos una lista donde guardaremos los datos de los libros a almacenar
		self.libros=[]
 
	# menu del programa
	def menu(self):
		print()
		menu=[
			['Agenda Personal'],
			['1. Añadir libro',"anadir"],
			['2. Lista libros existentes '],
			['3. Buscar libro'],
			['4. Editar libro'],
			['5. Cerrar libreria']
		]
 
		for x in range(6):
			print(menu[x][0])
 
		opcion=int(input("Introduzca la opción deseada: "))
		if opcion==1:
			self.anadir()
		elif opcion==2:
			self.lista()
		elif opcion==3:
			self.buscar()
		elif opcion==4:
			self.editar()
		elif opcion==5:
			print("Saliendo de la libreria ...")
			exit()
 
		# volvemos a llamar al menú
		self.menu()
 
 
	# función para libros
	def anadir(self):
		print("---------------------")
		print("Añadiendo  libro     ")
		print("---------------------")
		nom=input("Introduzca el nombre libro: ")
		edit=input("Nombre de la editorial: ")
		self.libros.append({'libro':nom,'editorial':edit})
		
 
	# función para imprimir la lista de los libros inscritos
	# Se imprimiran solo los nombres de los libros en biblioteca
	def lista(self):
		print("------------------")
		print("Lista de contactos")
		print("------------------")
		if len(self.libros) == 0:
			print("No hay ningún contacto en la agenda")
		else:
			for x in range(len(self.libros)):
				print(self.libros[x]['libro'])
		
 
	# función para buscar un libro mediante su nombre
	def buscar(self):
		print("---------------------")
		print("Buscador de contactos")
		print("---------------------")
		nom=input("Introduzca el nombre del contacto: ")
		for x in range(len(self.libros)):
			if nom == self.libros[x]['libro']:
				print("Datos del libro")
				print("Libro: ",self.libros[x]['libro'])
				print("Editorial: ",self.libros[x]['editorial'])
				return x
		
 
 
	# función para editar los datos del libro
	def editar(self):
		print("---------------")
		print("Editar info libro")
		print("---------------")
		data=self.buscar()
		condition=False
		while condition==False:
			print("Selecciona que quieres editar: ")
			print("1. Libro")
			print("3. Editorial")
			print("4. Volver menu")
			option=int(input("Introduzca la opción deseada: "))
			if option==1:
				nom=input("Introduzca el nuevo nombre: ")
				self.libros[data]['libro']=nom
			elif option==3:
				editorial=input("Introduzca la nueva editorial: ")
				self.libros[data]['editorial']=editorial
			elif option==4:
				condition=True
 
 
 
# bloque principal
lib=Libreria()
lib.menu()