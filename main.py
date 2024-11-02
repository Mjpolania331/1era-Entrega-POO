import tkinter as tk

class JuegoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de Memoria")
        self.master.geometry("500x300")  

        self.label = tk.Label(self.master, text="Bienvenido al Juego de Memoria", font=("Arial", 15))
        self.label.pack(pady=20)

        self.boton = tk.Button(self.master, text="Iniciar Juego", command=self.iniciar_juego)
        self.boton.pack(pady=20)

    def iniciar_juego(self):
        print("El juego ha comenzado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoGUI(root)
    root.mainloop()






