diccionario =  {
        "nombre" : 'Kevin',
        "apellido" : 'Cruz',
        "subs" : 1000000
    }
#.keys() ---> Devuelve las claves (tambien sirve para iterar)
claves = diccionario.keys()

#.get("clave") ---> Devuelve el valor de una clave (si no encuentra nada el programa continua)
valor_de_ksajl = diccionario.get("ksajl")

#.pop("clave","clave") ---> Elimina un elemento del diccionario
diccionario.pop("nombre")

#.item() ---> Obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()

#clear() ---> Elimina los elementos de el diccionario
#diccionario.clear()

print(diccionario)