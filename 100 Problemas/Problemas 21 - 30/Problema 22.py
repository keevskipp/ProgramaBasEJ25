#Tarea 6 22/Feb
#Realizar 21 -30 problemas

#22. Simular el lanzamiento de un dado y una moneda.
import random

#Simula el lanzamiento de un dado de seis caras
def lanzar_dado():
    return random.randint(1, 6)

#Simula el lanzamiento de una moneda
def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

#Menu
def main():
    print("Simulación de lanzamiento de un dado y una moneda")
    dado = lanzar_dado()
    moneda = lanzar_moneda()
    print(f"Resultado del dado: {dado}")
    print(f"Resultado de la moneda: {moneda}")

# Ejecutar la simulación
if __name__ == "__main__":
    main()