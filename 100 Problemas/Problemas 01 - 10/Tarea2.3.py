#Tarea 2 03/Feb
#Realizar 10 problemas

#3. Calcular el factorial de un numero dado.
def factorial(n):
    if n == 0 or n == 1:  #El factorial de 0 y 1 es 1
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):  #Multiplica los números desde 2 hasta n
            resultado *= i
        return resultado

#Solicitar al usuario un número
numero = int(input("Ingresa un número para calcular su factorial: "))

#Calcular y mostrar el factorial
print(f"El factorial de {numero} es: {factorial(numero)}")