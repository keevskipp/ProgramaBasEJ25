#Ejercicio 4: Calculadora de Estad´ısticas
import math

def calcular_estadisticas(*args):
    """
    Calcula el promedio, mediana y desviación estándar de una lista de números.
    - Usa *args para aceptar cualquier cantidad de números.
    - Usa funciones lambda para cálculos simples.
    """
    
    # Verificamos que haya al menos un número
    if not args:
        return None, None, None
    
    # Ordenamos los números para facilitar cálculos
    numeros_ordenados = sorted(args)
    n = len(numeros_ordenados)
    
    # ---- Cálculo del Promedio (Media) con lambda ----
    promedio = (lambda x: sum(x) / len(x))(numeros_ordenados)
    
    # ---- Cálculo de la Mediana ----
    if n % 2 == 1:  # Si es impar
        mediana = numeros_ordenados[n // 2]
    else:  # Si es par
        mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
    
    # ---- Cálculo de la Desviación Estándar ----
    # Primero calculamos la varianza (promedio de las diferencias al cuadrado)
    varianza = sum((x - promedio) ** 2 for x in numeros_ordenados) / n
    desviacion_estandar = math.sqrt(varianza)
    
    return promedio, mediana, desviacion_estandar

def main():
    print("Calculadora de Estadisticas")
    print("Ingresa los números separados por espacios (ejemplo: 5 10 15 20):")
    
    try:
        # Leemos los números ingresados por el usuario
        entrada = input(">> ").strip()
        numeros = [float(num) for num in entrada.split()]
        
        # Calculamos las estadísticas
        promedio, mediana, desviacion = calcular_estadisticas(*numeros)
        
        # Mostramos los resultados
        print("\n Resultados:")
        print(f"Promedio (Media): {promedio:.2f}")
        print(f"Mediana: {mediana:.2f}")
        print(f"Desviación Estándar: {desviacion:.2f}")
    except ValueError:
        print("Error: Asegúrate de ingresar solo números separados por espacios.")

if __name__ == "__main__":
    main()