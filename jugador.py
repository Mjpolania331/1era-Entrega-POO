class Jugador:
    jugadores_registrados = {}

    def _init_(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.puntaje = 0

    @staticmethod
    def registrar(nombre_usuario, contraseña):
        if nombre_usuario in Jugador.jugadores_registrados:
            return None  
        jugador = Jugador(nombre_usuario, contraseña)
        Jugador.jugadores_registrados[nombre_usuario] = jugador
        return jugador

    @staticmethod
    def autenticar(nombre_usuario, contraseña):
        jugador = Jugador.jugadores_registrados.get(nombre_usuario)
        if jugador and jugador.contraseña == contraseña:
            return jugador
        return None

    def agregar_puntos(self, puntos):
        self.puntaje += puntos

    def resetear_puntaje(self):
        self.puntaje = 0

    def _str_(self):
        return f"{self.nombre_usuario}: {self.puntaje} puntos"