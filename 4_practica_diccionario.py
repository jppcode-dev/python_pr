# #####################
# Diccionario
# #####################

# Clave - Valor
miDiccionario={"Alemania":"Berlín","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
print(miDiccionario["Francia"])
print(miDiccionario)

# Agregar Elemento al Diccionario
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

# Modificar un elemento del Diccionario
miDiccionario["Italia"]="Roma"
print(miDiccionario)

# Eliminar un elemento del Diccionario
del miDiccionario["Reino Unido"]
print(miDiccionario)

miDiccionario2={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}
print(miDiccionario2)

# Crear Tupla
miTupla=["España","Francia","Reino Unido","Alemania"]
# Asignar la Tupla al Diccionario
miDiccionario3={miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlín"}
print(miDiccionario3)

# claves y valores de Diccionario y longitud
print (miDiccionario3.keys())
print (miDiccionario3.values())
print (len(miDiccionario3))