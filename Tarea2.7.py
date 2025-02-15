#Tarea 2 03/Feb
#Realizar 10 problemas

# 7. Determinar si un n´umero es par, impar o m´ultiplo de otro
def verificar_numero(numero, multiplo_de):
    # Verificar si es par o impar
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

    # Verificar si es múltiplo de otro número
    if numero % multiplo_de == 0:
        print(f"{numero} es múltiplo de {multiplo_de}.")
    else:
        print(f"{numero} NO es múltiplo de {multiplo_de}.")

# Pedir datos al usuario
numero = int(input("Ingresa un número: "))
multiplo_de = int(input("Ingresa otro número para verificar si es múltiplo: "))

# Verificar el número
verificar_numero(numero, multiplo_de)