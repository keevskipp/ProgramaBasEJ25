#Tarea 6 22/Feb
#Realizar 21 -30 problemas

#29. Generar y analizar datos estad´ısticos
import numpy as np

def generar_datos():
    # Genera una lista de números aleatorios
    cantidad = int(input("Ingrese la cantidad de datos a generar: "))
    datos = np.random.randint(1, 100, cantidad)
    print("Datos generados:", datos)
    return datos

def analizar_datos(datos):
    # Calcula estadísticas básicas
    if len(datos) == 0:
        print("No hay datos para analizar.")
        return
    print(f"Media: {np.mean(datos)}")
    print(f"Mediana: {np.median(datos)}")
    print(f"Desviación estándar: {np.std(datos)}")

def menu():
    datos = []
    while True:
        print("\nMenú de Análisis Estadístico")
        print("1. Generar datos")
        print("2. Analizar datos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            datos = generar_datos()
        elif opcion == "2":
            analizar_datos(datos)
        elif opcion == "3":
            print("Gracias por usar el sistema de análisis estadístico.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciar el programa
menu()
