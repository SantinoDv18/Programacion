#Generar una piramide de asteriscos(*) hasta determinado numero que brinda el usuario.
num = int(input("Digite un número entero positivo: "))

for i in range(num):
	
    print(" " * (num - i -1) + "*" * (2*i + 1))
print("----------------------")
for j in range(num):
	print(" " * j + "*" * ((num*2) - (j*2) - 1))
