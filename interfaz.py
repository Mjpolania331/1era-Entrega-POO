from juego import Juego

def main():
    juego = Juego()

    while True:
        print("1. Registrar Jugador")
        print("2. Iniciar Juego")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            jugador = juego.registrar_jugador(username, password)
            if jugador:
                print("Jugador registrado con éxito.")
            else:
                print("Error: Ya existe un jugador con ese nombre.")

        elif choice == "2":
            username1 = input("Ingrese el nombre de usuario del Jugador 1: ")
            password1 = input("Ingrese la contraseña del Jugador 1: ")
            jugador1 = juego.autenticar_jugador(username1, password1)
            if jugador1 is None:
                print("Jugador 1 no registrado")
                continue
            
            username2 = input("Ingrese el nombre de usuario del Jugador 2: ")
            password2 = input("Ingrese la contraseña del Jugador 2: ")
            jugador2 = juego.autenticar_jugador(username2, password2)
            if jugador2 is None:
                print("Jugador 2 no registrado")
                continue
            
            tema = input(
            'Animales': ['🐶', '🐬', '🐥', '🐠'],
            'Frutas': ['🍓', '🍌', '🍉', '🍍'],
            'Emojis': ['🥰', '😱', '😎', '😋'],
            'Objetos': ['🎈', '🧸', '💡', '📷'],)
            tamaño = int(input("Seleccione el tamaño del tablero (2, 4, 6, ...): "))
            juego.iniciar_juego(jugador1, jugador2, tema, tamaño)
            juego.jugar()
        

if __name__ == "_main_":
    main()
