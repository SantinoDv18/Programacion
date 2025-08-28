# Crear 2 matrices y luego sumar sus.
matriz = [
[1,2,3],
[4,5,6],
[7,8,9]
]

matriz_2 = [
[10,11,12],
[13,14,15],
[16,17,18]
]

matriz_result = [
[],
[],
[]
]

for i in range(len(matriz)):
	
	for j in range(len(matriz)):
		matriz_result[i].append(matriz[i][j] + matriz_2[i][j])

for i in matriz_result:
	print(i)

