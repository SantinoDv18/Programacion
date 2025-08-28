# Ingresar valores a una matriz y luego mostrar los valores.

matriz = [

]

matrix_size = int(input("Digite el tamaño de la matriz: "))

fila = 0
columna = 0

for i in range(matrix_size):
	matriz.append([])


for i in matriz:
	
	for j in range(matrix_size):
		
		val_ingresado = int(input(f"Digite el valor de [{fila}] [{columna}]: "))
		
		columna +=1
		
		i.append(val_ingresado)
		
	columna = 0
	
	fila += 1
	
for i in matriz :
	print(i)
