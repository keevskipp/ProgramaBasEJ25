#Ejercicio 9: Implementaci´on de M´ultiples Paradigmas

# 1. ESTILO IMPERATIVO (paso a paso)
print("1. Estilo Imperativo:")
numero = 5
doble = numero * 2
print(f"El doble de {numero} es {doble}")

# 2. ESTILO ESTRUCTURADO (con funciones)
print("\n2. Estilo Estructurado:")
def calcular_triple(n):
    return n * 3

print(f"El triple de 4 es {calcular_triple(4)}")

# 3. ESTILO MODULAR (agrupando funciones)
print("\n3. Estilo Modular:")
class Calculadora:
    @staticmethod
    def cuadruple(n):
        return n * 4

print(f"El cuádruple de 2 es {Calculadora.cuadruple(2)}")

# 4. ESTILO ORIENTADO A OBJETOS (con clases y objetos)
print("\n4. Estilo Orientado a Objetos:")
class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        return f"Hola soy {self.nombre}"

gato = Mascota("Michi")
print(gato.saludar())