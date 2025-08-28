# Generar numero aleatorio y luego el usuario debera adivinarlo. El programa contara los intentos fallidos

import random

num = random.randint(1,100)

print("Adivina el numero del 1 al 100\n")

intentos = int(0)
while True:
	
	numIngresado = int(input(">>>"))
	
	if (numIngresado == num):
		print(f"""\nADIVINASTE!
Numero de intentos: {intentos}""")
		break
	else:
		if numIngresado < num:
			print("\nEl número es mayor\n")
		elif numIngresado > num:
			print("El número es menor\n")
			
		print("Intenta nuevamente\n")
		print(f"\nintentos: {intentos}\n")
		
		intentos += 1
