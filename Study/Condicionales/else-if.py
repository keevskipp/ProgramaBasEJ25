ingreso_mensual = 100000
gasto_mensual = 900000
 
if ingreso_mensual > 10000:
    if gasto_mensual - ingreso_mensual < 0:
        print("Estas en deficit")
    
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien")
    else:
        print("gastas mucho")


elif ingreso_mensual > 1000:
    print("Estas bien en Latam")

elif ingreso_mensual > 500:
    print("Estas bien en Argentina")

elif ingreso_mensual > 200:
    print("Estas bien en Venezuela")

else:
    print("sos pobre")
