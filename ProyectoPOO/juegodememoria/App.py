from consola import mostrar_menu, iniciar_juego
from modelo import Sistema

def app():
    sistema = Sistema()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":  # Registrar Jugador
            nombre_usuario = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ")
            jugador = sistema.registrar_jugador(nombre_usuario, contraseña)
            if jugador:
                print(f"¡Jugador '{nombre_usuario}' registrado con éxito!")
            else:
                print(f"El nombre de usuario '{nombre_usuario}' ya está registrado.")

        elif opcion == "2":  # Iniciar Sesión y Partida
            nombre_usuario = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ")
            jugador = sistema.autenticar_jugador(nombre_usuario, contraseña)
            if jugador:
                print(f"¡Bienvenido {nombre_usuario}!")
                iniciar_juego(sistema, jugador)
            else:
                print("Credenciales incorrectas. Por favor intenta nuevamente.")

        elif opcion == "3":  # Salir del juego
            print("Gracias por jugar. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor selecciona una opción válida.")

if __name__ == "__main__":
    app()
