import random
import tkinter as tk
from tkinter import messagebox

class Ficha:
    def _init_(self, id, icono):
        self.id = id
        self.icono = icono
        self.estado = False  
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
    
    def actualizar_puntaje(self, puntos):
        self.puntaje += puntos

    def resetear_puntaje(self):
        self.puntaje = 0

class Tablero:
    def _init_(self, tema, tamaño):
        self.tema = tema
        self.fichas = []
        self.tamaño = tamaño
        self.distribuir_fichas_aleatoriamente()
    
    def distribuir_fichas_aleatoriamente(self):
        temas = {
            'Animales': ['🐶', '🐬', '🐥', '🐠', '🐱', '🐰', '🐻', '🦁'],
            'Frutas': ['🍓', '🍌', '🍉', '🍍', '🍏', '🍊', '🍒', '🍇'],
            'Emojis': ['🥰', '😱', '😎', '😋', '😍', '😜', '😳', '😇'],
            'Objetos': ['🎈', '🧸', '💡', '📷', '📚', '⚽', '🚗', '💻'],
        }
        pares_necesarios = (self.tamaño * self.tamaño) // 2
        fichas_seleccionadas = []
        iconos = temas.get(self.tema, [])

        if len(iconos) * 2 < pares_necesarios:
            raise ValueError("No hay suficientes iconos para la cantidad de fichas seleccionada.")

        for i in range(pares_necesarios):
            icono = iconos[i % len(iconos)]
            fichas_seleccionadas.extend([Ficha(i, icono), Ficha(i, icono)])  

        random.shuffle(fichas_seleccionadas)
        self.fichas = fichas_seleccionadas

class Sistema:
    def _init_(self):
        self.juegos_activos = []
        self.turno_actual = 0  

    def registrar_jugador(self, nombre_usuario, contraseña):
        return Jugador.registrar(nombre_usuario, contraseña)

    def autenticar_jugador(self, nombre_usuario, contraseña):
        return Jugador.autenticar(nombre_usuario, contraseña)

    def iniciar_juego(self, jugador, tema, tamaño):
        tablero = Tablero(tema, tamaño)
        self.juegos_activos.append((jugador, tablero))
        return tablero

class JuegoGUI:
    def _init_(self, master):
        self.master = master
        self.master.title("Juego de Memoria")
        self.sistema = Sistema()
        
        self.frame_login = tk.Frame(self.master)
        self.frame_login.pack()

        self.label_usuario = tk.Label(self.frame_login, text="Usuario:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(self.frame_login)
        self.entry_usuario.pack()

        self.label_contraseña = tk.Label(self.frame_login, text="Contraseña:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(self.frame_login, show="*")
        self.entry_contraseña.pack()

        self.boton_login = tk.Button(self.frame_login, text="Iniciar Sesión", command=self.login)
        self.boton_login.pack()

        self.boton_registrar = tk.Button(self.frame_login, text="Registrar", command=self.registrar)
        self.boton_registrar.pack()

        self.frame_juego = None
        self.tablero = None
        self.botones_fichas = []
        self.fichas_reveladas = []

    def login(self):
        nombre_usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        jugador = self.sistema.autenticar_jugador(nombre_usuario, contraseña)

        if jugador:
            messagebox.showinfo("Éxito", f"Bienvenido {jugador.nombre_usuario}!")
            self.iniciar_juego(jugador)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def registrar(self):
        nombre_usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        jugador = self.sistema.registrar_jugador(nombre_usuario, contraseña)

        if jugador:
            messagebox.showinfo("Éxito", f"Registro exitoso para {jugador.nombre_usuario}.")
        else:
            messagebox.showerror("Error", "El usuario ya existe.")

    def iniciar_juego(self, jugador):
        self.frame_login.pack_forget()
        self.frame_juego = tk.Frame(self.master)
        self.frame_juego.pack()

        self.label_tema = tk.Label(self.frame_juego, text="Selecciona un tema:")
        self.label_tema.pack()

        self.tema_var = tk.StringVar(value="Animales")
        self.tema_opciones = tk.OptionMenu(self.frame_juego, self.tema_var, 'Animales', 'Frutas', 'Emojis', 'Objetos')
        self.tema_opciones.pack()

        self.label_dificultad = tk.Label(self.frame_juego, text="Selecciona la dificultad:")
        self.label_dificultad.pack()

        self.dificultad_var = tk.StringVar(value="Fácil")
        self.dificultad_opciones = tk.OptionMenu(self.frame_juego, self.dificultad_var, 'Fácil', 'Medio', 'Difícil')
        self.dificultad_opciones.pack()

        self.boton_comenzar = tk.Button(self.frame_juego, text="Comenzar Juego", command=lambda: self.comenzar_juego(jugador))
        self.boton_comenzar.pack()

    def comenzar_juego(self, jugador):
        tema = self.tema_var.get()
        dificultad = self.dificultad_var.get()
        tamaño = 4  

        if dificultad == "Medio":
            tamaño = 6
        elif dificultad == "Difícil":
            tamaño = 8

        self.tablero = self.sistema.iniciar_juego(jugador, tema, tamaño)
        self.mostrar_tablero(self.tablero)

    def mostrar_tablero(self, tablero):
        for widget in self.frame_juego.winfo_children():
            widget.destroy()  

        self.label_tablero = tk.Label(self.frame_juego, text=f"Tablero de {tablero.tema}:")
        self.label_tablero.pack()

        self.botones_fichas = []
        self.fichas_reveladas = []

        for i in range(tablero.tamaño):
            fila = tk.Frame(self.frame_juego)
            fila.pack()
            for j in range(tablero.tamaño):
                index = i * tablero.tamaño + j
                boton = tk.Button(fila, text="❓", width=5, height=2, command=lambda idx=index: self.revelar_ficha(idx))
                boton.pack(side="left")
                self.botones_fichas.append(boton)

    def revelar_ficha(self, index):
        ficha = self.tablero.fichas[index]
        if not ficha.estado and len(self.fichas_reveladas) < 2:
            ficha.estado = True
            self.botones_fichas[index].config(text=ficha.icono)
            self.fichas_reveladas.append(ficha)

            if len(self.fichas_reveladas) == 2:
                self.master.after(1000, self.comprobar_pareja)

    def comprobar_pareja(self):
        jugador_actual = self.sistema.juegos_activos[-1][0]  
        if self.fichas_reveladas[0].icono == self.fichas_reveladas[1].icono:
            for ficha in self.fichas_reveladas:
                ficha.estado = True
            jugador_actual.actualizar_puntaje(5)  
            messagebox.showinfo("¡Bien Hecho!", f"Puntaje: {jugador_actual.puntaje}") 
        else:
            for i, ficha in enumerate(self.tablero.fichas):
                if not ficha.estado:
                    self.botones_fichas[i].config(text="❓")

        self.fichas_reveladas.clear()

if _name_ == "_main_":
    root = tk.Tk()
    app = JuegoGUI(root)
    root.mainloop()
