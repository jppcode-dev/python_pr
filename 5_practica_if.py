# #####################
# Condicionales if
# #####################

print("Programa de Evaluación de Notas de Alumnos")

nota_alumno=input("Intorduce la Nota del Alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))

