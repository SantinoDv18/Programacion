# Pedir nombres al usuario y guardarlos en un archivo nombres.txt.


with open("dia6_archivo.txt", "a") as af:
	while True:
			print("""Digite una opcion:
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
			
		


