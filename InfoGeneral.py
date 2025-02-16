#try
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # Esto generará una excepción ZeroDivisionError
except ZeroDivisionError:
    # Código que se ejecuta si ocurre una excepción del tipo especificado
    print("¡No se puede dividir entre cero!")
except Exception as e:
    # Código que se ejecuta si ocurre cualquier otra excepción
    print(f"Ocurrió un error: {e}")
else:
    # Código que se ejecuta si no ocurre ninguna excepción
    print("El cálculo fue exitoso.")
finally:
    # Código que se ejecuta siempre, haya o no ocurrido una excepción
    print("Fin del bloque try.")