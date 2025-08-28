#Se solicitará al usuario ingresar una frase. Seguido de esto contará las vocales que contiene y las mostrará utilizando match.

frase = str(input("Ingrese una frase: ").lower())

acum_a = 0
acum_e = 0
acum_i = 0
acum_o = 0
acum_u = 0

for i in frase:
	match i:
		case "a":
			acum_a += 1
		case "e":
			acum_e += 1
		case "i":
			acum_i += 1
		case "o":
			acum_o += 1
		case "u":
			acum_u += 1


print(f"""
Frase: {frase}

Contador de vocales:
a : {acum_a}
e : {acum_e}
i : {acum_i}
o : {acum_o}
u : {acum_u}

""")
