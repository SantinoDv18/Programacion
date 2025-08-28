# Calcular el factorial de un numero manualmente

num = int(input("Digite un numero entero: "))
factorial = 1

for i in range(1,num+1):
	
	factorial *= i
	
	
print(f"\n{num}! = {factorial}")

