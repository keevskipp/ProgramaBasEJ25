#Tarea 2 03/Feb
#Realizar 10 problemas

#5. Verificar si un numero es primo.
def es_primo(n):
    if n <= 1:  #Los números menores o iguales a 1 no son primos
        return False
    for i in range(2, n):  #Verificar divisibilidad desde 2 hasta n-1
        if n % i == 0:  #Si es divisible por algún número, no es primo
            return False
    return True  #Si no se encontraron divisores, es primo

#Solicitar al usuario un número
numero = int(input("Ingresa un número para verificar si es primo: "))

#Verificar y mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")