import random

class Ficha:
    def __init__(self, id, icono):
        self.id = id
        self.icono = icono
        self.estado = False  # False significa que está cubierta

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
    
    def actualizar_puntaje(self, puntos):
        self.puntaje += puntos

    def resetear_puntaje(self):
        self.puntaje = 0


class Tablero:

    def __init__(self, tema):
        self.tema = tema
        self.fichas = []
        self.tamaño = 4  # Tamaño fijo del tablero (4x4 por ejemplo)
        self.distribuir_fichas_aleatoriamente()
    
    def configurar_tablero(self):
    # Aquí se puede fijar el tamaño a un valor predeterminado o ajustado si es necesario
        self.tamaño = 4  # Por ejemplo, un tablero de 4x4
    
    def elegir_tema(self, tema):
        temas = {
            'Animales': ['🐶', '🐬', '🐥', '🐠'],
            'Frutas': ['🍓', '🍌', '🍉', '🍍'],
            'Emojis': ['🥰', '😱', '😎', '😋'],
            'Objetos': ['🎈', '🧸', '💡', '📷'],
        }
        if tema in temas:
            self.tema = tema
            print(f"Tema seleccionado: {self.tema}")
        else:
            raise ValueError("Tema no válido. Selecciona uno de los temas disponibles.")

    def aplicar_tema(self, tema):
        temas = {
            'Animales': ['🐶', '🐬', '🐥', '🐠'],
            'Frutas': ['🍓', '🍌', '🍉', '🍍'],
            'Emojis': ['🥰', '😱', '😎', '😋'],
            'Objetos': ['🎈', '🧸', '💡', '📷'],
        }
        iconos = temas.get(tema, [])
        if not iconos:
            raise ValueError("No hay suficientes iconos para el tema seleccionado.")
        return iconos

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
        
    def mostrar_tablero(self):
        for i in range(0, len(self.fichas), self.tamaño):
            print(self.fichas[i:i + self.tamaño])
class Sistema:

    def __init__(self):
        self.juegos_activos = []
        self.turno_actual = 0  # Indica el jugador actual en el turno


    def registrar_jugador(self, nombre_usuario, contraseña):
        return Jugador.registrar(nombre_usuario, contraseña)

    def autenticar_jugador(self, nombre_usuario, contraseña):
        return Jugador.autenticar(nombre_usuario, contraseña)

    def iniciar_juego(self, jugador, tema):
        tablero = Tablero(tema)  # Inicializamos el tablero solo con el tema
        self.juegos_activos.append((jugador, tablero))
        return tablero

    def iniciar_multijugador(self, jugador1, jugador2, tema):
        tablero = Tablero(tema)  # Inicializamos el tablero solo con el tema
        self.juegos_activos.append((jugador1, tablero))
        self.juegos_activos.append((jugador2, tablero))
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
    
    def verificar_pareja(self, ficha1, ficha2):
        return ficha1.comparar_ficha(ficha2)

    def eliminar_pareja(self, ficha1, ficha2):
        ficha1.estado = False
        ficha2.estado = False

    def guardar_puntuacion(self, jugador):
        pass

    def mostrar_ranking(self):
        pass
