#Se solicitará al usuario ingresar una frase. Seguido de esto contará las vocales que contiene y las mostrará utilizando Diccionario,.

frase = str(input("Ingrese una frase: ").lower())

d = { x : frase.count(x) for x in 'aeiou' }

print(d)
