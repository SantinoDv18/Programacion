"""Menú interactivo que permita: 

>>>Agregar nombres a una lista

>>>Ver todos los nombres

>>>Buscar un nombre

>>>Salir

Usando listas y funciones
"""

lista = []

while True:
	
	print("""
	Por favor digite una opcion:
	
	1 -> Agregar nombres a una lista

	2 -> Ver todos los nombres

	3 -> Buscar un nombre

	0 -> Salir
	
	""")
	
	op = int(input(">"))
	
	match op:
		case 1:
			lista.append(input("Digite un nombre para agregar a la lista: ").lower())
			
		case 2:
			
			print(lista)
			
		case 3:
			
			strbuscado = input("Digite el valor a buscar: ").lower()
			
			for i in lista:
				
				if strbuscado == i:
					print(f"Valor {strbuscado} encontrado")
					
					break
			else:
				print("El valor no esta en la lista")		
			
			
		case 0:
			break
