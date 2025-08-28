#Todos los ejercicios del dia 6 en un menu interactivo
def crear_matriz():
	
	matriz = [

	]

	matrix_size = int(input("\nDigite el tamaño de la matriz: "))

	fila = 0
	columna = 0

	for i in range(matrix_size):
		matriz.append([])


	for i in matriz:
		
		for j in range(matrix_size):
			
			val_ingresado = int(input(f"Digite el valor de [{fila}] [{columna}]: "))
			
			columna +=1
			
			i.append(val_ingresado)
			
		columna = 0
		fila += 1
			

	return matriz

def sumar_matrices(matriz, matriz_2):
	
	matriz_result = [

	]
	
	for i in range(len(matriz)):
		matriz_result.append([])


	for i in range(len(matriz)):
		
		for j in range(len(matriz)):
			matriz_result[i].append(matriz[i][j] + matriz_2[i][j])

	for i in matriz_result:
		print(i)

	return matriz_result

def guardar_usuario():
	
	with open("dia6_archivo.txt", "a") as af:
				while True:
						print("""
Digite una opcion:
1 > Agg nuevo usuario
0 > Salir
						""")
						
						op = int(input(">"))
						
						match op:
							case 1:
								val = input("Digite el nombre de usuario a agregar: ").lower()
								af.write(f"{val} \n")
							case 0:
								break

def buscar_usuario():
	
	with open("dia6_archivo.txt", "r") as rf:
				val_buscado = input("Digite un nombre de usuario a buscar: ").lower()
				encontrado = False
				for i in rf:
					if (val_buscado == i.strip()):
						print("\nEl valor fue encontrado\n")
						encontrado = True
						break
				if not encontrado:
					print("\nEl valor no fue encontrado\n")
				rf.seek(0)
				print(f"Nombres de usuarios guardados: \n\n{rf.read()}")

while True:
	
	print("""
	Por favor digite una opcion:
	
	1 -> Crear matrices

	2 -> Sumar matrices

	3 -> Guardar un nombre en un archivo

	4 -> Buscar un nombre en el archivo
	
	0 -> Salir
	
	""")
	
	op = int(input(">"))
	
	match op:
		
		case 1:
			matriz = crear_matriz()
			
			print("\n Matriz Generada: \n")
			
			for i in matriz :
				print(i)
			
		case 2:
			
			matriz = crear_matriz()
			
			print("\n Matriz 1 Generada: \n")
			
			for i in matriz :
				print(i)
			
			matriz_2 = crear_matriz()
			
			print("\n Matriz 2 Generada: \n")
			
			for i in matriz_2 :
				print(i)
				
			
			print(f"La suma de las 2 matrices es igual a = \n" )
			
			sumar_matrices(matriz, matriz_2)
			
		case 3:
			
			guardar_usuario()
		
		case 4:
			
			buscar_usuario()
		
		case 0:
			break
