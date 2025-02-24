#Tarea 6 22/Feb
#Realizar 21 -30 problemas

#21. Calcular el area y volumen de distintas figuras geometricas.
import math

#Calcula el área y volumen de una esfera
def calcular_esfera():
    radio = float(input("Ingrese el radio de la esfera: "))
    area = 4 * math.pi * radio ** 2  #Fórmula del área de una esfera
    volumen = (4/3) * math.pi * radio ** 3  #Fórmula del volumen de una esfera    "math.pi es pi"
    print(f"Área de la esfera: {area:.2f}")
    print(f"Volumen de la esfera: {volumen:.2f}")

#Calcula el área y volumen de un cubo
def calcular_cubo():
    lado = float(input("Ingrese la longitud de un lado del cubo: "))
    area = 6 * lado ** 2  #Fórmula del área de un cubo
    volumen = lado ** 3  #Fórmula del volumen de un cubo
    print(f"Área del cubo: {area:.2f}")
    print(f"Volumen del cubo: {volumen:.2f}")

#Calcula el área y volumen de un cilindro
def calcular_cilindro():
    radio = float(input("Ingrese el radio de la base del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    area = 2 * math.pi * radio * (radio + altura)  # Fórmula del área de un cilindro
    volumen = math.pi * radio ** 2 * altura  # Fórmula del volumen de un cilindro
    print(f"Área del cilindro: {area:.2f}")
    print(f"Volumen del cilindro: {volumen:.2f}")

#Muestra un menú para que el usuario elija una figura geométrica
def menu():
    while True:
        print("\nMenú de cálculo de área y volumen")
        print("1. Esfera")
        print("2. Cubo")
        print("3. Cilindro")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            calcular_esfera()
        elif opcion == "2":
            calcular_cubo()
        elif opcion == "3":
            calcular_cilindro()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menu
menu()