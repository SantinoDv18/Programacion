# Luego de pedir al usuario ingresar una palabra el sistema determinara si es palindromo o no(se lee igual en ambas direcciones)

cadena = str(input("Ingrese una palabra: "))
nuevacadena = str("")



for i in range(1, len(cadena)+1):
	nuevacadena = nuevacadena + (cadena[len(cadena)-i])
	

if (cadena==nuevacadena):
	
	print(f"{cadena} es igual a: {nuevacadena}")
else:
	print(f"{cadena} no es igual a: {nuevacadena}")
	
