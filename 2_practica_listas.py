# #####################
# Listas; lo que equivale en otros lenguajes a un array

# Elementos 0 1 2 3
miLista = ["María","Pepe","Marta","Antonio"]

print(miLista[:])

print(miLista[2])

print(miLista[-1])

# Porción de Lista
print(miLista[0:3]) # Excluye el 3; 0 1 y 2
print(miLista[:2]) # 0 y 1
print(miLista[1:2]) # Muestra 1 y excluye 2
print(miLista[2:]) # Muestra 2 en adelante

# Agregar Elementos al final de la lista
miLista.append("Sandra")

print(miLista[:])

# Agregar Elementos en la posición 2 de la lista
miLista.insert(2,"Sandra")

print(miLista[:])

# Agregar Varios Elementos a la lista
miLista.extend(["Ana","Imelda","Lucia"])

print(miLista[:])

# Saber el índice del elemento de la lista
print(miLista.index("Ana"))

# Saber si un elemento esta en la lista
print("María" in miLista)

# Se pueden incluir en la lista elementos string int float boolean, etc

# Remover un elemento de la lista
miLista.remove("Sandra")
print(miLista[:])

# Remover el último elemento de la lista
miLista.pop()
print(miLista[:])

# Sumar Listas
miLista2 = ["María", 5, True, 78.35]
miLista3 = ["Sandra", "Lucía"]
miLista4 = miLista2 + miLista3
print(miLista4[:])

# Repetir una lista 3 veces
miLista5 = ["Robert", 2, 69.52] * 3
print(miLista5[:])