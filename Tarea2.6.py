#Tarea 2 03/Feb
#Realizar 10 problemas

#6. Calcular el inter´es compuesto dado un capital, tasa y tiempo
def calcular_interes_compuesto(capital, tasa, tiempo):
    return capital * (1 + tasa / 100) ** tiempo

#Pedir datos al usuario
capital = float(input("Ingresa el capital inicial: "))
tasa = float(input("Ingresa la tasa de interés anual (%): "))
tiempo = float(input("Ingresa el tiempo en años: "))

#Calcular el monto total
monto_final = calcular_interes_compuesto(capital, tasa, tiempo)

#Mostrar resultado
print(f"\nDespués de {tiempo} años, el monto total es: ${monto_final:.2f}") #:.2f sirve para dar 2 decimales