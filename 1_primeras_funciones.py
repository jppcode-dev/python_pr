# Función sun parámetros
# Declaramos la función
def mensaje():
	print("Hola , estamos aprendiendo Python")
	print("Estamos parendiendo instrucciones")
	print("Poco a poco iremos avanzando")

# #####################
# Llamamos la función
mensaje()

mensaje()

print("Ejecutando código fuera de función")

mensaje()

# #####################
# Función con más instrucciones sin parámetros o argumentos
def suma():
	num1 = 5
	num2 = 7
	print(num1 + num2)

suma()

# #####################
# Función con parámetros o argumentos
def suma(num1, num2):
	print (num1 + num2)

suma(5,7)
suma(2,3)
suma(35,358)

# #####################
# Función declarando una variable y Obteniendo un resultado
def suma(num1, num2):
	resultado = num1 + num2
	return resultado

print(suma(65,71))

almacena_resultado = suma(45, 89)

print(almacena_resultado)

