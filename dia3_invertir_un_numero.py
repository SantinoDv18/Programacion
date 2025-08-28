# invertir un numero ingresado por el usuario, ejemplo: "123456" , "654321"

num = int(input("Digite un numero entero: "))

print(f"Numero ingresado: {num}")

numStr = str(abs(num))
for i in range(len((numStr))):
	print(numStr[len(numStr)-i-1], end= '')
