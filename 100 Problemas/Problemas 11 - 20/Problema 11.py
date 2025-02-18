#Tarea 3 15/Feb
#Realizar 10 - 20 problemas

#11. Verificar si una cadena es un palindromo.

def es_palindromo(cadena):
    #Eliminar espacios y convertir a minúsculas para evitar errores de comparación
    cadena = cadena.replace(" ", "").lower()
            #funcion.replace("lo que busca", "lo que va a sustituir").lower()lo pone minusculas
    #Comparar la cadena con su versión invertida
    return cadena == cadena[::-1]

#Pedir al usuario la palabra
cadena = input("Ingresa una palabra para verificar si es un palíndromo: ")

#Verifica y muestra el resultado
if es_palindromo(cadena):
    print(f'"{cadena}" es un palíndromo.')
else:
    print(f'"{cadena}" no es un palíndromo.')
