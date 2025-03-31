#Ejercicio 3: Gestion de Contactos con Tuplas y Estructuras Anidadas
# Lista para almacenar los contactos (cada contacto es una tupla)
agenda = []

def agregar_contacto():
    print("\n--- AGREGAR CONTACTO ---")
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    correo = input("Correo electrónico: ")
    
    # Creamos una tupla con los datos y la agregamos a la agenda
    contacto = (nombre, telefono, correo)
    agenda.append(contacto)
    print(f" Contacto '{nombre}' agregado correctamente.")

def buscar_contacto():
    print("\n--- BUSCAR CONTACTO ---")
    nombre_buscar = input("Nombre del contacto a buscar: ")
    
    encontrado = False
    
    for contacto in agenda:
        if contacto[0].lower() == nombre_buscar.lower():
            print("\n Informacion del contacto:")
            print(f" Nombre: {contacto[0]}")
            print(f" Telefono: {contacto[1]}")
            print(f" Correo: {contacto[2]}")
            encontrado = True
            break
    
    if not encontrado:
        print(" Contacto no encontrado.")

def listar_contactos():
    print("\n--- LISTA DE CONTACTOS (Orden alfabético) ---")
    
    if not agenda:
        print("La agenda está vacia.")
        return
    
    # Ordenamos la agenda por nombre (primer elemento de la tupla)
    agenda_ordenada = sorted(agenda, key=lambda contacto: contacto[0].lower())
    
    for contacto in agenda_ordenada:
        print(f"\n {contacto[0]}")
        print(f" {contacto[1]}")
        print(f" {contacto[2]}")

def menu():
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar todos los contactos")
        print("4. Salir")
        
        opcion = input("Elige una opcion (1-4): ")
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            listar_contactos()
        elif opcion == "4":
            print("Saliendo del programa... ")
            break
        else:
            print("Opcion no valida. Intentalo de nuevo.")

# Iniciamos el programa
print("Agenda de contactos")
menu()