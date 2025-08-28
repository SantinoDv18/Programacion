# Hacer una función llamada es_primo(n) que reciba un número y devuelva True si es primo y False si no lo es.
# También mostrará todos los numeros primos de 1 a 100

def es_primo(n):
	raiz = round(n ** 0.5)
	acum = 0
	
	if (n<=1):
		return False
		
	for i in range(2, raiz+1):
		

		
		if (n % i == 0):
			acum += 1

	if acum > 0:
		return False
	else:
		return True

num = int(input("Ingrese un numero entero para comprobar si es primo o no: "))

if (es_primo(num) == False):
	
	print("\nEl numero no es primo")
	
else:
	
	print("\nEl numero es primo")

print("\n Numeros primos del 1 al 100:\n ")
for i in range(2,101):
	
	if es_primo(i) == True:
		print(f"[{i}] ", end= ' ')

	
