#Tarea 6 22/Feb
#Realizar 21 -30 problemas

#30. Implementar funciones recursivas. 
def factorial(n):
    # Calcula el factorial de un número de forma recursiva
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    # Calcula el término n de la serie de Fibonacci de forma recursiva
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def menu():
    while True:
        print("\nMenú de Funciones Recursivas")
        print("1. Calcular Factorial")
        print("2. Calcular Fibonacci")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            num = int(input("Ingrese un número: "))
            print(f"Factorial de {num}: {factorial(num)}")
        elif opcion == "2":
            num = int(input("Ingrese un número: "))
            print(f"Fibonacci de {num}: {fibonacci(num)}")
        elif opcion == "3":
            print("Gracias por usar el sistema de funciones recursivas.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciar el programa
menu()
