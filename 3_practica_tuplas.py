# #####################
# Tuplas
# #####################
miTupla=("Juan",13,1,1995)
print(miTupla[2])

milista=list(miTupla)
print(milista)

# onvertir lista en tupla
milista=["Jorge",14,2,2000]
miTupla2=tuple(milista)
print(miTupla2)

# Saber si un elemento esta en una tupla
print("Juan" in miTupla)

# Saber cuantas veces esta un elemento en una tupla
print(miTupla.count(13))

# Saber la longitud una tupla
print(len(miTupla))

# Tupla unitaria
miTupla3=("Julio",)
print(miTupla3)
print(len(miTupla3))

# Crear variables con tuplas; desempaquetado de tuplas
nombre, dia, mes, agno=miTupla
print(nombre)
print(dia)
print(agno)
print(mes)