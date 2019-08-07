# ############################
# Excepciones 3
# ############################

# Lanzamiento de excepciones; no lanzadas por el programa sino por nosotros mismos
# Instrucción Raise
# Creación de excepciones propias

# def [nombre_funcion]([parámetro])
def evaluaEdad(edad):
	if edad<0:
		raise TypeError("No se permiten edades negativas")

	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres maduro"
	elif eda<100:
		return "Cuidate..."

print(evaluaEdad(-18))
