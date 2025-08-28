#Calcular los numeros primos desde 1 hasta n
import sympy

num = int(input("Digite un numero entero: "))

print(f"\nNumeros primos de 1 hasta {num}:", end = ' ')

for i in range(1,num):
	
	if sympy.isprime(i):
		
		print(i , end = ' ')


