# ############################
# Generadores
# ############################

# Tradicional
def generaPares(limite):
	num=1
	miLista=[]

	while num<limite:
		miLista.append(num*2)
		num=num+1
	return miLista

print(generaPares(10))

# Con GENERADOR YIELD
def generaPares2(limite2):
	num2=1

	while num2<limite2:
		yield num2*2
		num2=num2+1

devuelvePares=generaPares2(10)

# Imprime Todos
# for i in devuelvePares:
# 	print(i)

#Imprime los tres primeros
# Más Eficiente, con el generador
print(next(devuelvePares))

print("Aquí podría ir más codigo...")

print(next(devuelvePares))

print("Aquí podría ir más codigo...")

print(next(devuelvePares))


# Con GENERADOR YIELD II
# * antes del parámetro significa que se le asignarán varios argumentos en forma de tupla
def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		# for subElemento in elemento:
			# yield subElemento
		yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Biblao","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))