# ############################
# Bucle For
# ############################

for i in [1,2,3]:
	print("Hola")

for i in ["primavera","otoño","verano","invierno"]:
	print(i)

for i in ["Pildoras", "Informáticas"]:
	# print("hola3 "+str(i))
	print("hola4 ", end="      ")

email=False

for i in "jcprada05@gmail.com":
	if(i=="@"):
		email=True

if email==True:
	print("Email es correcto")
else:
	print("Email NO es correcto")


email=False
miEmail=input("Introduce tu Email: ")

for i in miEmail:
	if(i=="@"):
		email=True

if email==True:
	print("Email2 es correcto")
else:
	print("Email2 NO es correcto")


contador=0

for i in miEmail:
	if(i=="@" or i=="."):
		contador= contador+1

if contador==2:
	print("Email2 es correcto")
else:
	print("Email2 NO es correcto")

# Range crea un array; una lista
for i in range(5):
	# print("Hello")
	print(i)

for i in range(5):
	print(f"valor de la variable {i}")

for i in range(5,10):
	print(f"valor de la variable 2 {i}")

for i in range(5,50,3):
	print(f"valor de la variable 3 {i}")

valido=False

email=input("Introduce tu Email: ")

for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido:
	print("Email Correcto")
else:
	print("Email NO Correcto")