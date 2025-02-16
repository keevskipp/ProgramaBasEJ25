#Tarea 3 15/Feb
#Realizar 10 - 20 problemas

#12. Encontrar el mayor entre tres numeros dados.

def encontrar_numero_mayor(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c: 
        return b
    else:  # Si no, "c" es el mayor
        return c

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

mayor = encontrar_numero_mayor(num1, num2, num3)

print(f"El mayor número es: {mayor}")