#Tarea 2 03/Feb
#Realizar 10 problemas

#10. Leer, escribir y modificar un archivo de texto.
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(f"Contenido del archivo '{nombre_archivo}':\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

def escribir_archivo(nombre_archivo, texto):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)
    print(f"Texto escrito en el archivo '{nombre_archivo}'.")

def agregar_a_archivo(nombre_archivo, texto):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(texto)
    print(f"Texto agregado al archivo '{nombre_archivo}'.")

# Menú principal
def menu():
    nombre_archivo = input("Ingresa el nombre del archivo de texto: ")

    while True:
        print("\n--- Menú ---")
        print("1. Leer archivo")
        print("2. Escribir en archivo")
        print("3. Agregar al archivo")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            leer_archivo(nombre_archivo)
        elif opcion == '2':
            texto = input("Ingresa el texto a escribir: ")
            escribir_archivo(nombre_archivo, texto)
        elif opcion == '3':
            texto = input("Ingresa el texto a agregar: ")
            agregar_a_archivo(nombre_archivo, texto)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()