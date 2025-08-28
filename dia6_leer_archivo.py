#Leer todo el contenido de un archivo. Mostrar todos los nombres. Permitir al usuario buscar un nombre dentro del archivo.

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
