# ############################
# Condicionales and or in
# ############################

edad=7

if 0<edad<100:
	print("Edad es correcta")
else:
	print("Edad es incorrecta")


salario_presidente=int(input("Introduce salario presidente: "))
print("Salario presidente es: "+str(salario_presidente))

salario_director=int(input("Introduce salario director: "))
print("Salario director es: "+str(salario_director))

salario_jefe_area=int(input("Introduce salario jefe de area: "))
print("Salario jefe de area es: "+str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario administrativo: "))
print("Salario administrativo es: "+str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")


print("Programa de Becas 2019")

distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el número de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
	print("Tienes derecho a beca")
else:
	print("NO Tienes derecho a beca")

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tienes derecho a beca")
else:
	print("NO Tienes derecho a beca")


print("Asignaturas optativas Año 2019")

print("Asignaturas Optativas: Informatica Grafixa - Pruebas de software - Usabilidad y accesibilidad")
asignatura=input("Introduce la asignatura escogida: ")

if asignatura in ("Informática gráfica", "Pruebas de software", "Usabilidad y accesibilidad"):
	print("Asignatura Elegida: "+asignatura)
else:
	print("La asignatura escogida no existe")

opcion = "Hola Cómo Estás"
minuscula=opcion.lower()
mayuscula=opcion.upper()

print(minuscula)
print(mayuscula)	