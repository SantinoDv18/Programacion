# Imprimir serie de numeros Fibonacci hasta n

n = int(input("Digite un numero: "))  
a, b = 0, 1  

for _ in range(n):  
    print(a, end=" ")  
    a, b = b, a + b  
