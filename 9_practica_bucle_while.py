# ############################
# Bucle While
# ############################

import math

i=1

while i<=10:
	print("Ejecución "+str(i))
	# print(f"Ejecución {i}")
	i=i+1

print("Terminó la Ejecución")


edad = int(input("Introduce tu edad por favor: "))

while edad<5 or edad>100:
	print("Has introducido una edad incorrecta.  Vuelve a intentarlo")
	edad = int(input("Introduce tu edad por favor: "))

print(f"Tu edad es de {edad} años.")
print("Gracias por colaborar; puedes pasar.")


print("Hallar la raiz cuadrada")

numero=int(input("Introduce un número por favor: "))
intentos=0

while numero<0:
	print("No se pueda hallar la raiz de un número negativo")

	if intentos==2:
		print("Has consumido demasiados intentos.  El programa ha finalizado")
		break;

	numero=int(input("Introduce un número por favor"))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print(f"La raiz cuadradad de {numero} es {solucion}")