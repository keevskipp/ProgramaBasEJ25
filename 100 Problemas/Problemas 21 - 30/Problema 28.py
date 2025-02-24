#Tarea 6 22/Feb
#Realizar 21 -30 problemas

#28. Simular una cuenta bancaria con dep´ositos y retiros

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        # Inicializa la cuenta con un saldo inicial
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        # Aumenta el saldo con el monto depositado
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: ${self.saldo}")
        else:
            print("El monto debe ser positivo.")
    
    def retirar(self, cantidad):
        # Reduce el saldo si hay suficiente dinero en la cuenta
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes o cantidad no válida.")
    
    def mostrar_saldo(self):
        # Muestra el saldo actual de la cuenta
        print(f"Saldo actual: ${self.saldo}")

# Función para mostrar el menú y gestionar las opciones
def menu():
    cuenta = CuentaBancaria(float(input("Ingrese el saldo inicial: ")))
    while True:
        print("\nMenú de Cuenta Bancaria")
        print("1. Mostrar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cuenta.mostrar_saldo()
        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "3":
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "4":
            print("Gracias por usar el sistema de cuenta bancaria.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciar el programa
menu()
