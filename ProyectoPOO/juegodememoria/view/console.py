from modelo_juego import Juego

# ------------------------------
# Funciones de la vista en consola
# ------------------------------
def mostrar_menu_principal():
    print("=== Bienvenido al Juego de Memoria ===")
    print("1. Crear una cuenta")
    print("2. Iniciar una partida")
    print("3. Salir")

def crear_cuenta(juego):
    print("\n=== Crear una cuenta ===")
    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    jugador = juego.registrar_jugador(nombre_usuario, contraseña)
    if jugador:
        print(f"Cuenta creada exitosamente, ¡bienvenido {nombre_usuario}!")
    else:
        print("Error: El nombre de usuario ya existe.")

def seleccionar_dificultad():
    print("\n=== Selecciona la dificultad ===")
    print("1. Fácil (4x4)")
    print("2. Medio (6x6)")
    print("3. Difícil (8x8)")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        return 'Facil'
    elif opcion == "2":
        return 'Medio'
    elif opcion == "3":
        return 'Dificil'
    else:
        print("Opción inválida. Se seleccionará dificultad Fácil por defecto.")
        return 'Facil'

def seleccionar_tema():
    print("\n=== Selecciona el tema del juego ===")
    print("1. Animales")
    print("2. Frutas")
    print("3. Emojis")
    print("4. Objetos")
    opcion = input("Selecciona una opción: ")
    temas = ['Animales', 'Frutas', 'Emojis', 'Objetos']
    try:
        return temas[int(opcion) - 1]
    except (ValueError, IndexError):
        print("Opción inválida. Se seleccionará el tema 'Animales' por defecto.")
        return 'Animales'

def iniciar_partida(juego, jugador):
    print("\n=== Iniciar partida ===")
    dificultad = seleccionar_dificultad()
    tema = seleccionar_tema()
    tablero = juego.iniciar_partida(jugador, dificultad, tema)
    print("\nTablero de juego:")
    print(tablero)

# ------------------------------
# Programa principal
# ------------------------------
def main():
    juego = Juego()
    while True:
        mostrar_menu_principal()
        opcion = input("\nSelecciona una opción: ")
        if opcion == "1":
            crear_cuenta(juego)
        elif opcion == "2":
            if len(juego.jugadores) == 0:
                print("Primero debes crear una cuenta.")
            else:
                jugador = juego.jugadores[0]  # Para simplificar, usamos el primer jugador
                iniciar_partida(juego, jugador)
        elif opcion == "3":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción inválida. Por favor selecciona una opción válida.")

if __name__ == "__main__":
    main()

