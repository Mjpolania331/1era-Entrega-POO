
class Juego:
    def iniciar(self):
        print("El juego ha inicidado")  


from jugador import Jugador
from tablero import Tablero

class Juego:
    def _init_(self):
        self.jugadores = []
        self.tablero = None

    def registrar_jugador(self, nombre_usuario, contraseña):
        return Jugador.registrar(nombre_usuario, contraseña)

    def autenticar_jugador(self, nombre_usuario, contraseña):
        return Jugador.autenticar(nombre_usuario, contraseña)

    def iniciar_juego(self, jugador1, jugador2, tema, tamaño):
        self.tablero = Tablero(tema, tamaño)
        self.jugadores = [jugador1, jugador2]
        return self.tablero

    def jugar_turno(self, jugador):
        self.tablero.mostrar_tablero()
        try:
            indice1 = int(input(f"{jugador.nombre_usuario}, selecciona la primera ficha (índice): "))
            indice2 = int(input(f"{jugador.nombre_usuario}, selecciona la segunda ficha (índice): "))

            if self.tablero.voltear_fichas(indice1, indice2):
                print("¡Coincidencia!")
                jugador.agregar_puntos(10)
                self.tablero.eliminar_fichas(indice1, indice2)
            else:
                print("No coincide.")
                jugador.agregar_puntos(-5)

        except (IndexError, ValueError):
            print("Selección no válida. Intenta de nuevo.")

    def mostrar_ranking(self):
        print("Tabla de posiciones:")
        for jugador in sorted(self.jugadores, key=lambda j: j.puntaje, reverse=True):
            print(jugador)

    def jugar(self):
        turno_actual = 0
        while not self.tablero.todas_destapadas():
            self.jugar_turno(self.jugadores[turno_actual])
            turno_actual = 1 - turno_actual  
        self.mostrar_ranking()
        