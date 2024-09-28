import random


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


class Tablero:

    def __init__(self, tema):
        self.tema = tema
        self.fichas = []
        self.tamaño = 4  # Tamaño fijo del tablero (4x4 por ejemplo)
        self.distribuir_fichas_aleatoriamente()

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

        if len(iconos) * 2 < pares_necesarios:
            raise ValueError(
                "No hay suficientes iconos para la cantidad de fichas seleccionada.")

        for i in range(pares_necesarios):
            icono = iconos[i % len(iconos)]
            fichas_seleccionadas.extend([icono, icono])

        random.shuffle(fichas_seleccionadas)
        self.fichas = fichas_seleccionadas

class Sistema:
    def __init__(self):
        self.juegos_activos = []
        self.jugadores_registrados = {}

    def registrar_jugador(self, nombre_usuario, contraseña):
        """Registra un nuevo jugador si el nombre de usuario no existe."""
        if nombre_usuario in self.jugadores_registrados:
            return None  # Jugador ya registrado
        nuevo_jugador = Jugador(nombre_usuario, contraseña)
        self.jugadores_registrados[nombre_usuario] = nuevo_jugador
        return nuevo_jugador

    def autenticar_jugador(self, nombre_usuario, contraseña):
        """Autentica a un jugador usando su nombre de usuario y contraseña."""
        jugador = self.jugadores_registrados.get(nombre_usuario)
        if jugador and jugador.contraseña == contraseña:
            return jugador
        return None

    def iniciar_multijugador(self, jugador1, jugador2, dificultad, tema):
        """Inicia una partida multijugador entre dos jugadores."""
        tablero = Tablero(dificultad, tema)
        self.juegos_activos.append((jugador1, jugador2, tablero))
        return tablero

    def alternar_turnos(self, jugador1, jugador2):
        """Alterna turnos entre dos jugadores."""
        pass

    def calcular_ganador(self, jugador1, jugador2):
        """Calcula el ganador en función del puntaje."""
        if jugador1.puntaje > jugador2.puntaje:
            return jugador1
        elif jugador2.puntaje > jugador1.puntaje:
            return jugador2
        else:
            return None  # Empate
