#Ejercicio 8: Implementaci´on de Mergesort
"""
Mergesort es un algoritmo de ordenamiento eficiente que sigue el paradigma
"divide y vencerás". Funciona así:
1. Divide la lista en dos mitades
2. Ordena cada mitad recursivamente
3. Combina (merge) las dos mitades ordenadas
"""
def mergesort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        # Ordenar recursivamente cada mitad
        mergesort(izquierda)
        mergesort(derecha)

        # Combinar las mitades ordenadas
        i = j = k = 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Copiar los elementos restantes
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Programa principal
print("ORDENAMIENTO CON MERGESORT")
numeros = input("Ingresa números separados por espacios: ").split()
numeros = [int(num) for num in numeros]  # Convertir a enteros

print("\nLista original:", numeros)
mergesort(numeros)
print("Lista ordenada:", numeros)