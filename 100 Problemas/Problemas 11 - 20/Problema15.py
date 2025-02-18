#Tarea 3 15/Feb
#Realizar 10 - 20 problemas

#15. Determinar si un ano es bisiesto
def es_bisiesto(anio):

    # Un año es bisiesto es divisible por 4, pero no por 100, a menos que también sea divisible por 400
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Pide el anio
anio = int(input("Ingresa un año: "))

# Verificar e imprimirlo
if es_bisiesto(anio):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")