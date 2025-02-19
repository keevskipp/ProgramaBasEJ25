cadena1 = "Hola,Soy,Kevin"
cadena2 = "Bienvenido champ"
cadena3 = "wsaknc"

"""Variable.Funciones(propiedades)"""
#Convierte a mayusculas
mayus = cadena2.upper()

#Convierte a minusculas
min = cadena2.lower()

#Primera lera en mayusculas
primer_letra_mayus = cadena1.capitalize()

#Buscamos una cadena en otra cadena, si no hay concidencias devuelve "-1"
busqueda_find = cadena1.find("D")

#Buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_find = cadena2.index("B")

#Si es numerico, devolvemos TRUE, sino devolvemos FALSE
es_numerico = cadena3.isnumeric()

#Si es Alfanumerico devolvemos TRUE, sino devolvemos FALSE
es_alfanumerico = cadena3.isalpha()

#Contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("o")

#Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve TRUE
empieza_con = cadena1.startswith("Hola")

#Verificamos si una cadena termina con otra cadena dada, si es asi devuelve TRUE
termina_con = cadena1.endswith("sja")

#Si el valor se encuentra en la cadena original, remplaza el valor "1" de la misma, por el valor 2
cadena_nueva = cadena1.replace("Hola", "holUuuu")

#Separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada[2])


"""Metodos.(variable)"""
#jcoen
resultado = dir(cadena1)

#Contamos las coincidencias de una cadena
contar_caracteres = len(cadena1)



print(cadena_nueva)