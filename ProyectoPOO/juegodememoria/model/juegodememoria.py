import random

# ------------------------------
# Clase Jugador: Registro y autenticación
# ------------------------------
class Jugador:
    jugadores_registrados = {}

    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.puntaje = 0
        self.tablero = None

    @staticmethod
    def crear_cuenta(nombre_usuario, contraseña):
        if nombre_usuario in Jugador.jugadores_registrados:
            return None  # El nombre de usuario ya existe
        nuevo_jugador = Jugador(nombre_usuario, contraseña)
        Jugador.jugadores_registrados[nombre_usuario] = nuevo_jugador
        return nuevo_jugador

# ------------------------------
# Clase Tablero: Configuración del juego
# ------------------------------
class Tablero:
    def __init__(self, dificultad, tema):
        self.fichas = []
        self.tamaño = 0
        self.tema = tema
        self.dificultades = {
            'Facil': (4, 60),    # 4x4 fichas, 60 segundos
            'Medio': (6, 120),   # 6x6 fichas, 120 segundos
            'Dificil': (8, 180)  # 8x8 fichas, 180 segundos
        }
        self.temas = {
            'Animales': ['🐶', '🐬', '🐥', '🐠'],
            'Frutas': ['🍓', '🍌', '🍉', '🍍'],
            'Emojis': ['🥰', '😱', '😎', '😋'],
            'Objetos': ['🎈', '🧸', '💡', '📷'],
        }
        self.configurar_tablero(dificultad)

    def configurar_tablero(self, dificultad):
        if dificultad not in self.dificultades:
            raise ValueError("Dificultad no válida.")
        self.tamaño, self.tiempo_limite = self.dificultades[dificultad]

    def distribuir_fichas_aleatoriamente(self):
        pares_necesarios = (self.tamaño * self.tamaño) // 2
        self.fichas = []

        for i in range(pares_necesarios):
            icono = self.temas[self.tema][i % len(self.temas[self.tema])]
            ficha1 = Ficha(i, icono)
            ficha2 = Ficha(i, icono)
            ficha1.pareja = ficha2
            ficha2.pareja = ficha1
            self.fichas.extend([ficha1, ficha2])

        random.shuffle(self.fichas)  # Mezclar fichas

    def mostrar_tablero(self):
        tablero_visible = []
        for i, ficha in enumerate(self.fichas):
            if ficha.estado:
                tablero_visible.append(f"| {ficha.icono} |")
            else:
                tablero_visible.append("| ? |")
            if (i + 1) % self.tamaño == 0:
                tablero_visible.append("\n")
        return "".join(tablero_visible)

    def aplicar_tema(self, tema):
        if tema not in self.temas:
            raise ValueError("Tema no válido.")
        self.tema = tema

# ------------------------------
# Clase Ficha: Representa cada ficha del tablero
# ------------------------------
class Ficha:
    def __init__(self, id_ficha, icono):
        self.id_ficha = id_ficha
        self.icono = icono
        self.estado = False
        self.pareja = None

# ------------------------------
# Clase Juego: Gestión del flujo del juego
# ------------------------------
class Juego:
    def __init__(self):
        self.jugadores = []

    def registrar_jugador(self, nombre_usuario, contraseña):
        jugador = Jugador.crear_cuenta(nombre_usuario, contraseña)
        if jugador:
            self.jugadores.append(jugador)
        return jugador

    def iniciar_partida(self, jugador, dificultad, tema):
        jugador.tablero = Tablero(dificultad, tema)
        jugador.tablero.aplicar_tema(tema)
        jugador.tablero.distribuir_fichas_aleatoriamente()
        return jugador.tablero.mostrar_tablero()
