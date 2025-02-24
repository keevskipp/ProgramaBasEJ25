#Tarea 6 22/Feb
#Realizar 21 -30 problemas

#
def convertir_longitud(valor, unidad_origen, unidad_destino):
    factores = {
        "m": 1, "cm": 100, "mm": 1000, "km": 0.001,
        "pulgadas": 39.37, "pies": 3.281, "yardas": 1.094
    }
    return valor * (factores[unidad_destino] / factores[unidad_origen])

def convertir_peso(valor, unidad_origen, unidad_destino):
    factores = {
        "kg": 1, "g": 1000, "mg": 1000000, "lb": 2.205, "oz": 35.274
    }
    return valor * (factores[unidad_destino] / factores[unidad_origen])

def menu():
    while True:
        print("\nConversor de Unidades")
        print("1. Longitud")
        print("2. Peso")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            valor = float(input("Ingrese el valor a convertir: "))
            unidad_origen = input("Unidad de origen (m, cm, mm, km, pulgadas, pies, yardas): ")
            unidad_destino = input("Unidad de destino: ")
            print(f"Resultado: {convertir_longitud(valor, unidad_origen, unidad_destino)} {unidad_destino}")
        elif opcion == "2":
            valor = float(input("Ingrese el valor a convertir: "))
            unidad_origen = input("Unidad de origen (kg, g, mg, lb, oz): ")
            unidad_destino = input("Unidad de destino: ")
            print(f"Resultado: {convertir_peso(valor, unidad_origen, unidad_destino)} {unidad_destino}")
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
