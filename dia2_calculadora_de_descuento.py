print("""
-----------------------------
| --Bienvenido a la tienda--|
|  -MAS POR MENOS ES MENOS-	|
-----------------------------
""")
precio = float(input("Digite el precio de su compra: "))

validacion_tarjeta = input("""
¿Tiene usted tarjeta de cliente
V: SI
F: NO
""").lower()

print (validacion_tarjeta)
if validacion_tarjeta == "v":
	print(f"El precio de su compra tiene un descuento gracias a su tarjeta de cliente, el nuevo monto es: ${precio*0.90}")

else:
	print("El precio de su compra no tiene un descuento, adquiera su tarjeta de cliente para obtener un descuento del 10% en todas sus compras")


