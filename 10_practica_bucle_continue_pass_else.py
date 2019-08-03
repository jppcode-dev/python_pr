# ############################
# Bucles Continue Pass Else
# ############################

for letra in "Python":
	if letra=="h":
		continue
	print("Viendo la letra: " + letra)


nombre = "Pildoras Informáticas"
contador=0
for i in nombre:
	if i==" ":
		continue
	contador+=1
print(contador)


email=input("Introduce tu email por favor: ")

for i in email:
	if i=="@":
		arroba=True
		break;
else:
	arroba=False

print(arroba)
