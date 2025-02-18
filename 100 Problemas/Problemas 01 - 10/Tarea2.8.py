#Tarea 2 03/Feb
#Realizar 10 problemas

#8. Calcular el ´area y la circunferencia de un c´ırculo.
import math # Libreria de matematicas

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_circunferencia(radio):
    return 2 * math.pi * radio

# Pedir el radio al usuario
radio = float(input("Ingresa el radio del círculo: "))

# Calcular área y circunferencia
area = calcular_area_circulo(radio)
circunferencia = calcular_circunferencia(radio)

# Mostrar resultados
print(f"\nEl área del círculo es: {area:.2f}")
print(f"La circunferencia del círculo es: {circunferencia:.2f}") #:.2f funciona para que salgan 2 decimales