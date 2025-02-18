#Tarea 2 03/Feb
#Realizar 10 problemas

#9. Generar una lista de n´umeros pares e impares hasta un lımite dado.
def generar_pares_impares(limite):
    pares = []  # Lista para almacenar números pares
    impares = []  # Lista para almacenar números impares

    for numero in range(1, limite + 1):  # Recorrer desde 1 hasta el límite
        if numero % 2 == 0:  # Si es divisible por 2, es par
            pares.append(numero)
        else:  # Si no, es impar
            impares.append(numero)

    return pares, impares

# Pedir el límite al usuario
limite = int(input("Ingresa el límite: "))

# Generar listas de pares e impares
pares, impares = generar_pares_impares(limite)

# Mostrar resultados
print(f"Números pares hasta {limite}: {pares}")
print(f"Números impares hasta {limite}: {impares}")