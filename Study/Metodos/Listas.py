#Creando una lista con list()
lista = list([87812, True, 21])

#Devuelve la cantidad de elementos de la lista
resultado = len(lista)

#Agregando un elemeto a la lisa
lista.append(False)

#Agregando un elemento a la lista en un indice especifico
lista.insert(2, "pivon")

#Agregando varios elementos a la lista ---> dentro de corchetes
lista.extend([False, 2300])

#Eliminando un elemento de la lista (por su indice)
lista.pop(0) # "-1" para eliminar el ultimo elemento, "-2" para el penultimo y asi "-n" elemento

#Removiendo un elemento de la lista por su valor
lista.remove("pivon")

#Eliminando todos los elementos de la lista
#lista.clear()

#Ordenando la lista (si usamos el parametro "reverse = True" lo ordena en reversa (ascendente))
lista.sort(reverse = True)

#Inviertiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(21)

print(lista.index(21))
print(lista)
#print(len(lista))