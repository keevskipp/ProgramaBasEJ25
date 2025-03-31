'''
1.1 Estructuras de Datos
Ejercicio 1: An´alisis de Texto con Diccionarios y Conjuntos
Desarrolla un programa que analice un texto ingresado por el usuario y determine:
 El n´umero total de palabras en el texto.
 La cantidad de palabras ´unicas, utilizando un conjunto para evitar repeticiones.
 La frecuencia de cada palabra usando un diccionario donde la clave sea la
palabra y el valor la cantidad de veces que aparece.
 La palabra m´as frecuente y cu´antas veces aparece.
El programa debe mostrar un resumen con estos datos
'''
def analizar_texto():
    # Solicitar texto al usuario
    texto = input("Ingrese el texto a analizar: ")
    
    # Dividir el texto en palabras
    palabras = texto.lower().split()     #---> split() quita los espacios
    
    # 1. Numero total de palabras      
    total_palabras = len(palabras)      # --->len() cuenta lo que este dentro del objeto
    
    # 2. Palabras unicas usando un conjunto
    palabras_unicas = set(palabras)             # --->set() crea un objeto de un conjunto
    cantidad_unicas = len(palabras_unicas)
    
    # 3. Frecuencia de cada palabra usando diccionario
    frecuencia = {}     # Crea una lista vacia
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1  # fuction.get()  
    
    # 4. Palabra más frecuente
    if frecuencia:
        palabra_mas_frecuente = max(frecuencia, key=frecuencia.get)
        max_frecuencia = frecuencia[palabra_mas_frecuente]
    else:
        palabra_mas_frecuente = ""
        max_frecuencia = 0
    
    print("\nResumen de análisis:")
    print(f"1. Total de palabras: {total_palabras}")
    print(f"2. Palabras unicas: {cantidad_unicas}")
    print("3. Frecuencia de palabras:")
    for palabra, count in frecuencia.items():
        print(f"   '{palabra}': {count} veces")
    print(f"4. Palabra más frecuente: '{palabra_mas_frecuente}' (aparece {max_frecuencia} veces)")

# Ejecuta la función
analizar_texto()