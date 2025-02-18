#Creando una lista (se pueden modificar) 
list = ["Kevin Adair", "Soy Kevin", True, 1.78]
print(list[2])

#Creando una tupla (no se puede modificar)
tupla = ["Kevin Adair", "Soy Kevin", True, 1.78]

#Esto es valido
list[3] = "titina"

#Esto no
#tulpla[3] = "titina"

#Creando un conjunto (set) 
#(no se accede a elementos por indice, no almacena datos duplicados, se puede reconstruir)
cojunto = {"Kevin Adair", "Soy Kevin", True, 1.78}

#print(conjunto[3]) ----> no se puede acceder al elemento

#Creando un diccionario (dict) ----> la estructura es "key" : "value" [para numeros no lleva ""] y separamos con comas
diccionario =  {
    'nombre' : "Kevin",             
    'edad' : 18,
    'altura' : 1.77,
    'esta_emocionado' : True,
    'dato_duplicado' : 18
 }
print(diccionario['altura'])


