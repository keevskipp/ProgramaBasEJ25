#Tarea 2 03/Feb
#Realizar 10 problemas

#2. Crear una calculadora simple que realice operaciones basicas.
def suma(a, b):
    return a + b
def resta(a,b):
    return a - b
def multi(a,b):
    return a * b
def calculadora():
    print("Calculadora de Suma")
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    print(f"El resultado de la suma es: {suma(num1, num2)}")
    print(f"El resultado de la resta es: {resta(num1, num2)}")
    print(f"El resultado de la multi es: {multi(num1, num2)}")
#Llamada directa a la función calculadora
calculadora()