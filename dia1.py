nombre = input("¿Cómo te llamas? ")
apellido = input("¿Como te apellidas?")
fecha_nacimiento = int(input("¿En que año naciste?"))
edad = int(input("¿Cuántos años tienes? "))
genero = input("¿Cual es tu sexo?")
ciudad = input("¿Donde vives?")
print(f"""Hola {nombre}, {apellido}, tu sexo es: {genero}. 
El año que viene tendrás {edad + 1} años. Porque naciste en el año {fecha_nacimiento}

""")
print("Vives en la ciudad de, " , ciudad)


#Prueba con diferentes entradas.

#Cambia el programa para que también pregunte ciudad y muestre un saludo completo.
