import random

# Clase Jugador: Maneja los jugadores y su registro
class Jugador:
    jugadores_registrados = {}

    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.puntaje = 0

    @staticmethod
    def registrar(nombre_usuario, contraseña):
        if nombre_usuario in Jugador.jugadores_registrados:
            return None  # Ya existe un jugador con ese nombre
        jugador = Jugador(nombre_usuario, contraseña)
        Jugador.jugadores_registrados[nombre_usuario] = jugador
        return jugador

    @staticmethod
    def autenticar(nombre_usuario, contraseña):
        jugador = Jugador.jugadores_registrados.get(nombre_usuario)
        if jugador and jugador.contraseña == contraseña:
            return jugador
        return None

# Clase Tablero: Configuración del juego
class Tablero:
    def __init__(self, dificultad, tema):
        self.dificultad = dificultad
        self.tema = tema
        self.fichas = []
        self.tamaño = 0
        self.configurar_tablero()
        self.distribuir_fichas_aleatoriamente()

    def configurar_tablero(self):
        dificultades = {
            'Facil': 4,    # 4x4 fichas
            'Medio': 6,    # 6x6 fichas
            'Dificil': 8   # 8x8 fichas
        }
        if self.dificultad in dificultades:
            self.tamaño = dificultades[self.dificultad]

    def distribuir_fichas_aleatoriamente(self):
        temas = {
            'Animales': ['🐶', '🐬', '🐥', '🐠'],
            'Frutas': ['🍓', '🍌', '🍉', '🍍'],
            'Emojis': ['🥰', '😱', '😎', '😋'],
            'Objetos': ['🎈', '🧸', '💡', '📷'],
        }
        pares_necesarios = (self.tamaño * self.tamaño) // 2
        fichas_seleccionadas = []
        iconos = temas.get(self.tema, [])

        for i in range(pares_necesarios):
            icono = iconos[i % len(iconos)]
            fichas_seleccionadas.extend([icono, icono])

        random.shuffle(fichas_seleccionadas)
        self.fichas = fichas_seleccionadas

    def mostrar_tablero(self):
        return self.fichas

# Clase Sistema: Controla el flujo general del juego
class Sistema:
    def __init__(self):
        self.juegos_activos = []

    def registrar_jugador(self, nombre_usuario, contraseña):
        return Jugador.registrar(nombre_usuario, contraseña)

    def autenticar_jugador(self, nombre_usuario, contraseña):
        return Jugador.autenticar(nombre_usuario, contraseña)

    def iniciar_juego(self, jugador, dificultad, tema):
        tablero = Tablero(dificultad, tema)
        return tablero

    def guardar_progreso(self, jugador, puntaje):
        jugador.puntaje = puntaje
        pass  # Se puede implementar un sistema de almacenamiento persistente

# Clase Juego: Maneja el flujo de una partida
class Juego:
    def __init__(self, jugador, dificultad, tema):
        self.jugador = jugador
        self.tablero = Tablero(dificultad, tema)

    def jugar(self):
        pass  # Se implementará en requisitos funcionales posteriores

    def verificar_pareja(self):
        pass  # Se implementará en requisitos funcionales posteriores

    def mostrar_puntuacion(self):
        pass  # Se implementará en requisitos funcionales posteriores
