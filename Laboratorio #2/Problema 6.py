#Ejercicio 6: Sistema de Gesti´on de Veh´ıculos
# Clase principal para todos los vehículos
# Clase principal para todos los vehículos
class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca      # Ej: "Toyota"
        self.modelo = modelo    # Ej: "Corolla"
        self.año = año          # Ej: 2020
        self.precio = precio    # Ej: 20000
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio: ${self.precio}")

# Clase para autos (hereda de Vehiculo)
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, precio, puertas):
        super().__init__(marca, modelo, año, precio)
        self.puertas = puertas  # Ej: 4
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")

# Clase para motos (hereda de Vehiculo)
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindros):
        super().__init__(marca, modelo, año, precio)
        self.cilindros = cilindros 
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindros: {self.cilindros}cc")

# --- Usamos las clases ---
print("=== VEHÍCULOS ===")

# Creamos un auto
mi_auto = Auto("Toyota", "Corolla", 2020, 20000, 4)

# Creamos una moto
mi_moto = Moto("Honda", "CBR", 2021, 15000, 600)

# Mostramos la información
print("\nMi auto:")
mi_auto.mostrar_info()

print("\nMi moto:")
mi_moto.mostrar_info()