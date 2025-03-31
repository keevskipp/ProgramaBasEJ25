#Ejercicio 7: Ordenamiento y B´usqueda
# Clase principal para todos los vehículos
import random

# 1. Generamos números aleatorios
numeros = [random.randint(1, 50) for _ in range(10)]
print("Lista original:", numeros)

# 2. Ordenamos la lista (forma fácil con sort())
numeros.sort()
print("Lista ordenada:", numeros)

# 3. Buscamos un número
buscar = int(input("\n¿Qué número quieres buscar? "))

# Búsqueda sencilla (como buscar en una lista)
encontrado = False
for i, num in enumerate(numeros):
    if num == buscar:
        print(f"¡Encontrado! El número {buscar} está en la posición {i}")
        encontrado = True
        break

if not encontrado:
    print(f"El número {buscar} no está en la lista.")