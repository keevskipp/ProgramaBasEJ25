#Tarea 6 22/Feb
#Realizar 21 -30 problemas

#24. Calcular la suma de una serie numerica
def suma_serie(n):
    """Calcula la suma de la serie 1 + 2 + 3 + ... + n."""
    return sum(range(1, n + 1))

def main():
    n = int(input("Ingrese el número hasta donde quiere sumar la serie: "))
    resultado = suma_serie(n)
    print(f"La suma de la serie hasta {n} es: {resultado}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
