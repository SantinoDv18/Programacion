#Contar la suma acumulada de los numeros desde 1 hasta un numero ingresado por el usuario.

num = int(input("Digite un numero: "))

i = 1

suma = 0

while i < num:
	
	suma += i
	
	i += 1
	
print(f"La suma acumulada de 1 hasta {num} es igual a: {suma}")
