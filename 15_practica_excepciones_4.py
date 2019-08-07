# ############################
# Excepciones 4
# ############################

# Lanzamiento de excepciones; no lanzadas por el programa sino por nosotros mismos
# Instrucción Raise
# Creación de excepciones propias

# def [nombre_funcion]([parámetro])
import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError("El número no puede ser negatio")
	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un número: ")))

try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)

print("Programa terminado")
