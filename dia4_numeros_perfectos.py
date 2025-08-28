# Calcular los numeros perfectos que hay hasta n

num = int(input("Digite un numero: "))
acum = 0

for i in range(num):
	
	for j in range(1,i):
		if (i%j==0):
			acum += j
			
	if (acum == i) and (acum !=0) :
		print(acum)
		acum=0
	else:
		acum=0
