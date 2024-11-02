import random

class Ficha:
    def _init_(self, id, icono):
        self.id = id
        self.icono = icono
        self.estado = False  

class Tablero:
    def _init_(self, tema, tamaño):
        self.tema = tema
        self.tamaño = tamaño
        self.fichas = self.generar_fichas()
        self.tablero_visible = [False] * len(self.fichas)

    def generar_fichas(self):
        temas = {
            'Animales': ['🐶', '🐬', '🐥', '🐠'],
            'Frutas': ['🍓', '🍌', '🍉', '🍍'],
            'Emojis': ['🥰', '😱', '😎', '😋'],
            'Objetos': ['🎈', '🧸', '💡', '📷'],
        }
        iconos = temas.get(self.tema, [])
        if len(iconos) * 2 < (self.tamaño * self.tamaño) // 2:
            raise ValueError("No hay suficientes para la cantidad de fichas seleccionada.")

        fichas = []
        for i in range((self.tamaño * self.tamaño) // 2):
            icono = iconos[i % len(iconos)]
            fichas.append(Ficha(i, icono))
            fichas.append(Ficha(i + (self.tamaño * self.tamaño) // 2, icono)) 

        random.shuffle(fichas)
        return fichas

    def mostrar_tablero(self):
        for i in range(0, len(self.fichas), self.tamaño):
            fila = [ficha.icono if self.tablero_visible[ficha.id] else "X" for ficha in self.fichas[i:i + self.tamaño]]
            print(" ".join(fila))

    def voltear_fichas(self, indice1, indice2):
        self.tablero_visible[indice1] = True
        self.tablero_visible[indice2] = True
        return self.fichas[indice1].icono == self.fichas[indice2].icono

    def eliminar_fichas(self, indice1, indice2):
        self.tablero_visible[indice1] = True
        self.tablero_visible[indice2] = True

    def todas_destapadas(self):
        return all(self.tablero_visible)
