#Tarea 3 15/Feb
#Realizar 10 - 20 problemas

#18. Resolver ecuaciones cuadraticas.
import math #funciones matemáticas avanzadas, como raíces cuadradas, trigonometría, logaritmos

# Pedir los coeficientes al usuario
a = float(input("Ingresa el coeficiente a (coeficiente con x al cuadrado): "))
b = float(input("Ingresa el coeficiente b(coeficiente con x): "))
c = float(input("Ingresa el coeficiente c(coefeciente sin x): "))

# Calcular el discriminante
discriminante = b**2 - 4*a*c

# Verificar el tipo de raíces
if discriminante > 0:
    x1 = (-b + math.sqrt(discriminante)) / (2*a) #math.sqrt calcula la raiz
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Las soluciones son: x1 = {x1}, x2 = {x2}")
elif discriminante == 0:
    x = -b / (2*a)
    print(f"La solución es una raíz doble: x = {x}")
else:
    print("La ecuación no tiene raíces reales.")