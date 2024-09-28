from juegodememoria import Sistema
class UIConsola:
    def __init__(self):
        self.sistema = Sistema()

    def mostrar_menu(self):
        print("=== Bienvenido al Juego de Memoria ===")
        print("1. Registrar Jugador")
        print("2. Iniciar Sesión")
        print("3. Iniciar Juego Multijugador")
        print("4. Salir")

    def menu_tema(self):
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

    def iniciar_juego(self, jugador):
        tema = self.menu_tema()  # Elige el tema
        tablero = self.sistema.iniciar_juego(jugador, tema)  # Inicia el juego sin dificultad
        print("\nCartas distribuidas aleatoriamente:")
        self.mostrar_tablero(tablero)

    def iniciar_juego_multijugador(self, jugador1, jugador2):
        tema = self.menu_tema()  # Elige el tema
        tablero = self.sistema.iniciar_multijugador(jugador1, jugador2, tema)  # Inicia multijugador
        print("\nCartas distribuidas aleatoriamente para ambos jugadores:")
        self.mostrar_tablero(tablero)

    def mostrar_tablero(self, tablero):
        tamaño = tablero.tamaño
        fichas = tablero.fichas
        for i in range(0, len(fichas), tamaño):
            print(fichas[i:i + tamaño])

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":  # Registrar Jugador
                nombre_usuario = input("Nombre de usuario: ")
                contraseña = input("Contraseña: ")
                jugador = self.sistema.registrar_jugador(
                    nombre_usuario, contraseña)
                if jugador:
                    print(f"¡Jugador '{nombre_usuario}' registrado con éxito!")
                else:
                    print(f"El nombre de usuario '{nombre_usuario}' ya está registrado.")

            elif opcion == "2":  # Iniciar Sesión y Juego Individual
                nombre_usuario = input("Nombre de usuario: ")
                contraseña = input("Contraseña: ")
                jugador = self.sistema.autenticar_jugador(
                    nombre_usuario, contraseña)
                if jugador:
                    print(f"¡Bienvenido {nombre_usuario}!")
                    self.iniciar_juego(jugador)
                else:
                    print("Credenciales incorrectas. Por favor intenta nuevamente.")

            elif opcion == "3":  # Iniciar Juego Multijugador
                print("\n=== Iniciar Juego Multijugador ===")
                nombre_usuario1 = input("Nombre de usuario del Jugador 1: ")
                contraseña1 = input("Contraseña del Jugador 1: ")
                jugador1 = self.sistema.autenticar_jugador(
                    nombre_usuario1, contraseña1)

                if not jugador1:
                    print("Credenciales incorrectas para Jugador 1. Por favor intenta nuevamente.")
                    continue

                nombre_usuario2 = input("Nombre de usuario del Jugador 2: ")
                contraseña2 = input("Contraseña del Jugador 2: ")
                jugador2 = self.sistema.autenticar_jugador(
                    nombre_usuario2, contraseña2)

                if not jugador2:
                    print("Credenciales incorrectas para Jugador 2. Por favor intenta nuevamente.")
                    continue

                print(f"¡Bienvenidos {nombre_usuario1} y {nombre_usuario2}!")
                self.iniciar_juego_multijugador(jugador1, jugador2)

            elif opcion == "4":  # Salir del juego
                print("Gracias por jugar. ¡Hasta luego!")
                break

            else:
                print("Opción inválida. Por favor selecciona una opción válida.")
