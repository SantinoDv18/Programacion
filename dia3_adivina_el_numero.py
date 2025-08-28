#Generar un numero aleatorio del 1 al 10 y se validará un numero ingresado por el usuario. Si este es correcto el bucle (while) se romperá, de lo contrario seguirá hasta ser adivinado el numero
import random

num = random.randint(1,10)


valor = int(input("""
ADIVINA!

DIGITA UN NUMERO DEL 1 al 10

SI EL NUMERO ES CORRECTO TE GANARAS UN PREMIO, DE LO CONTRARIO PUEDES SEGUIR INTENTANDO INFINITAMENTE! :D 

Numero: """))

while valor != num :
	
	if num < valor :
		print("\nEl numero es menor")
	else :
		print("\nEl numero es mayor")
	
	print("\n Sigue intentando:", end= " ")
	
	valor = int(input())

print("\nEl numero es correcto!, haz roto el bucle")
