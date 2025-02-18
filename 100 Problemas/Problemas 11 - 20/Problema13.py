#Tarea 3 15/Feb
#Realizar 10 - 20 problemas

#13. Convertir una temperatura entre distintas escalas

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

#Menu
def menu():
    print("--- Conversor de Temperatura ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

    while True:
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            print(f"{celsius}°C equivale a {celsius_a_fahrenheit(celsius):.2f}°F\n")

        elif opcion == '2':
            fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
            print(f"{fahrenheit}°F equivale a {fahrenheit_a_celsius(fahrenheit):.2f}°C\n")

        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida\n")

if __name__ == "__main__":
    menu()