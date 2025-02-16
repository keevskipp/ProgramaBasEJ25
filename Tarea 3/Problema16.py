#Tarea 3 15/Feb
#Realizar 10 - 20 problemas

#17. Contar el numero de vocales y consonantes en una cadena
def contar_vocalesyconsonantes(cadena):
    vocales = 0
    consonantes = 0

    # Convertir la cadena a minúsculas para simplificar la comparacion
    cadena = cadena.lower()

    # Recorrer cada caracter de la cadena
    for caracter in cadena:
        if caracter in "aeiou":  # Verificar si es una vocal
            vocales += 1
        elif caracter.isalpha():  # Verificar si es una letra ".isalpha():"  (pero no una vocal)
            consonantes += 1

    return vocales, consonantes

#Pedir la cadena al usuario
cadena = input("Ingresa una cadena de texto: ")

#Contar vocales y consonantes
vocales, consonantes = contar_vocalesyconsonantes(cadena)

#Imprime los resultados
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")