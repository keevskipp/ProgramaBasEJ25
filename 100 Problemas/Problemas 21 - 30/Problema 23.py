#Tarea 6 22/Feb
#Realizar 21 -30 problemas

#23. Implementar y operar con matrices.
import numpy as np

#Crea una matriz con valores ingresados por el usuario
def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los elementos de la fila {i+1} separados por espacio: ").split()))
        matriz.append(fila)
    return np.array(matriz)

#Suma de matrices
def sumar_matrices(matriz1, matriz2):
    return matriz1 + matriz2

#Multiplica dos matrices
def multiplicar_matrices(matriz1, matriz2):
    return np.dot(matriz1, matriz2)

#Menu
def main():
    filas = int(input("Ingrese el número de filas de las matrices: "))
    columnas = int(input("Ingrese el número de columnas de las matrices: "))
    print("Ingrese los elementos de la primera matriz:")
    matriz1 = crear_matriz(filas, columnas)
    print("Ingrese los elementos de la segunda matriz:")
    matriz2 = crear_matriz(filas, columnas)
    
    print("\nMatriz 1:")
    print(matriz1)
    print("\nMatriz 2:")
    print(matriz2)
    
    print("\nSuma de matrices:")
    print(sumar_matrices(matriz1, matriz2))
    
    if columnas == filas:  #Para multiplicación, columnas de A deben ser igual a filas de B
        print("\nMultiplicación de matrices:")
        print(multiplicar_matrices(matriz1, matriz2))
    else:
        print("\nNo es posible multiplicar estas matrices debido a sus dimensiones.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
