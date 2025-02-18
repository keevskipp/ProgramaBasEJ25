#Tarea 2 03/Feb
#Realizar 10 problemas

#4. Generar la secuencia de Fibonacci hasta un numero dado de terminos.
def fibonacci(n):
    secuencia = []  #Lista para almacenar la secuencia
    a, b = 0, 1     #Inicializamos los dos primeros términos de Fibonacci

    for _ in range(n):  #Generamos "n" términos
        secuencia.append(a)  #Agregamos el término actual a la lista
        a, b = b, a + b      #Calculamos el siguiente término

    return secuencia

#Solicitar al usuario el número de términos
n = int(input("Ingresa el número de términos de Fibonacci que deseas generar: "))

#Generar y mostrar la secuencia
print(f"Secuencia de Fibonacci con {n} términos: {fibonacci(n)}")