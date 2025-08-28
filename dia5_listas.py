# Se ingresaran 5 numeros y se guardarán en una lista para conocer las acciones basicas de la misma.

lista = []
acum = 0
for i in range(5):
	lista.append(int(input("Por favor ingrese un numero entero: ")))
	acum += lista[i]

numMayor = lista[0]
numMenor = lista[0]

for i in range(5):
	if lista[i] > numMayor:
		numMayor = lista[i]

	if lista[i] < numMenor:
		numMenor = lista[i]
	
	
print(f"\nLista de datos ingresados: {lista}")
print(f"\nEl numero mayor de la lista es: {numMayor}")
print(f"\nEl numero menor de la lista es: {numMenor}")
print(f"\nEl promedio de los numeros en la lista es igual a: {acum/len(lista)}")
