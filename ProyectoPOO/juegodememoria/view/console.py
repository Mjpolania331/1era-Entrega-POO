from modelo import Sistema

def mostrar_menu():
    print("=== Bienvenido al Juego de Memoria ===")
    print("1. Registrar Jugador")
    print("2. Iniciar Sesión")
    print("3. Salir")

def menu_dificultad():
    print("\n=== Selecciona la Dificultad ===")
    print("1. Fácil (4x4)")
    print("2. Medio (6x6)")
    print("3. Difícil (8x8)")

    opcion = input("Elige una opción: ")
    if opcion == "1":
        return "Facil"
    elif opcion == "2":
        return "Medio"
    elif opcion == "3":
        return "Dificil"
    else:
        print("Opción inválida. Se seleccionará Fácil por defecto.")
        return "Facil"

def menu_tema():
    print("\n=== Selecciona el Tema del Juego ===")
    print("1. Animales")
    print("2. Frutas")
    print("3. Emojis")
    print("4. Objetos")

    opcion = input("Elige una opción: ")
    temas = ['Animales', 'Frutas', 'Emojis', 'Objetos']
    try:
        return temas[int(opcion) - 1]
    except (ValueError, IndexError):
        print("Opción inválida. Se seleccionará 'Animales' por defecto.")
        return 'Animales'

def iniciar_juego(sistema, jugador):
    dificultad = menu_dificultad()
    tema = menu_tema()
    tablero = sistema.iniciar_juego(jugador, dificultad, tema)
    print("\nCartas distribuidas aleatoriamente:")
    print(tablero.mostrar_tablero())
