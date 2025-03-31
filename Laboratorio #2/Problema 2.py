#Ejercicio 2: Manejo de Inventario con Listas y Diccionarios

# Lista vacía para guardar nuestros productos
inventario = []

def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")
    
    # Pedimos los datos del producto
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría (ej. comida, electrónica, ropa): ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad en stock: "))
    
    # Creamos un diccionario con los datos
    producto = {
        'nombre': nombre,
        'categoria': categoria,
        'precio': precio,
        'cantidad': cantidad
    }
    
    # Lo agregamos al inventario
    inventario.append(producto)
    print(f"¡{nombre} agregado correctamente!")

def ver_productos():
    print("\n--- TODOS LOS PRODUCTOS ---")
    
    if len(inventario) == 0:
        print("No hay productos en el inventario.")
        return
    
    # Ordenamos por precio (de más barato a más caro)
    inventario_ordenado = sorted(inventario, key=lambda x: x['precio'])
    
    for producto in inventario_ordenado:
        print(f"Nombre: {producto['nombre']}")
        print(f"Categoría: {producto['categoria']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        print("--------------------")

def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")
    nombre_buscar = input("Nombre del producto a buscar: ")
    
    encontrado = False
    
    for producto in inventario:
        if producto['nombre'].lower() == nombre_buscar.lower():
            print("\nInformación del producto:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        print("Producto no encontrado.")

def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    nombre_eliminar = input("Nombre del producto a eliminar: ")
    
    for producto in inventario:
        if producto['nombre'].lower() == nombre_eliminar.lower():
            inventario.remove(producto)
            print(f"¡{producto['nombre']} eliminado correctamente!")
            return
    
    print("Producto no encontrado.")

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar producto")
        print("2. Ver todos los productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Iniciamos el programa
menu()