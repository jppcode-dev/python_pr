# ############################
# Excepciones 2
# ############################

# Excepción General, para cualquier tipo de error
def divide():
	
	try:
		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))
		print("La división es: "+str(op1/op2))
	
	except:
		print("El valor introducido es erróneo")

	print("Cálculo finalizado.")

divide()

# Excepciones según tipo de error específico
def divide():
	
	try:
		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))
		print("La división es: "+str(op1/op2))
	
	except ValueError:
		print("El valor introducido es erróneo")
	
	except ZeroDivisionError:
		print("No se puede dividir entre 0")

	print("Cálculo finalizado.")

divide()

# Excepciones introduciendo finally; ese finally siempre se va a ejecutar
def divide():
	
	try:
		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))
		print("La división es: "+str(op1/op2))
	
	except ValueError:
		print("El valor introducido es erróneo")
	
	except ZeroDivisionError:
		print("No se puede dividir entre 0")

	finally:
		print("Cálculo finalizado.")

divide()