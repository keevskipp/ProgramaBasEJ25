#Ejercicio 5: M´odulo para Conversi´on de Unidades
from conversor import km_a_millas, celsius_a_fahrenheit, litros_a_galones

def menu():
    print("\n=== CONVERSOR DE UNIDADES ===")
    print("1. Kilómetros a Millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a Galones")
    print("4. Salir")
    
    while True:
        try:
            opcion = int(input("Elige una opción (1-4): "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Por favor ingresa un número del 1 al 4.")
        except ValueError:
            print("¡Debes ingresar un número!")

def main():
    while True:
        opcion = menu()
        
        if opcion == 1:
            km = float(input("\nIngresa los kilómetros: "))
            print(f"{km} km = {km_a_millas(km):.2f} millas")
        elif opcion == 2:
            celsius = float(input("\nIngresa los grados Celsius: "))
            print(f"{celsius}°C = {celsius_a_fahrenheit(celsius):.2f}°F")
        elif opcion == 3:
            litros = float(input("\nIngresa los litros: "))
            print(f"{litros} litros = {litros_a_galones(litros):.2f} galones")
        elif opcion == 4:
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    print("¡Bienvenido al Conversor de Unidades!")
    main()