#Tarea 6 22/Feb
#Realizar 21 -30 problemas

#25. Generar y analizar histogramas de datos.
import numpy as np
import matplotlib.pyplot as plt

def generar_datos(cantidad, rango):
    """Genera una lista de datos aleatorios dentro de un rango especificado."""
    return np.random.randint(rango[0], rango[1] + 1, cantidad)

def mostrar_histograma(datos, bins):
    """Genera y muestra un histograma a partir de los datos proporcionados."""
    plt.hist(datos, bins=bins, edgecolor='black', alpha=0.7)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Datos')
    plt.grid(True)
    plt.show()

def main():
    """Función principal para generar y analizar histogramas de datos."""
    cantidad = int(input("Ingrese la cantidad de datos a generar: "))
    min_val = int(input("Ingrese el valor mínimo del rango: "))
    max_val = int(input("Ingrese el valor máximo del rango: "))
    bins = int(input("Ingrese el número de intervalos (bins) para el histograma: "))
    
    datos = generar_datos(cantidad, (min_val, max_val))
    print(f"Datos generados: {datos}")
    mostrar_histograma(datos, bins)

# Ejecutar el programa
if __name__ == "__main__":
    main()