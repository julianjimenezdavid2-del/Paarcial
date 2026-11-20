import tkinter as tk
from tkinter import ttk, messagebox

from modelos.personajes import Guerrero, Mago
from servicios.gestor_batalla import GestorBatalla


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Arena Elemental - Batallas RPG")
        self.geometry("620x510")
        self.resizable(False, False)
        self.jugador = None
        self.gestor = None
        self._construir_interfaz()

    def _construir_interfaz(self):
        contenedor = ttk.Frame(self, padding=18)
        contenedor.pack(fill="both", expand=True)
        ttk.Label(contenedor, text="ARENA ELEMENTAL", font=("Segoe UI", 20, "bold")).pack(pady=(0, 4))
        ttk.Label(contenedor, text="Juego de combate por turnos desarrollado con POO").pack(pady=(0, 12))

        seleccion = ttk.LabelFrame(contenedor, text="1. Elige tu personaje", padding=10)
        seleccion.pack(fill="x")
        self.tipo_personaje = tk.StringVar(value="Guerrero")
        ttk.Radiobutton(seleccion, text="Guerrero (120 de vida)", variable=self.tipo_personaje, value="Guerrero").pack(side="left", padx=12)
        ttk.Radiobutton(seleccion, text="Mago (90 de vida)", variable=self.tipo_personaje, value="Mago").pack(side="left", padx=12)
        ttk.Button(seleccion, text="Iniciar batalla", command=self.iniciar_batalla).pack(side="right")

        estado = ttk.LabelFrame(contenedor, text="Estado del combate", padding=10)
        estado.pack(fill="x", pady=12)
        self.lbl_jugador = ttk.Label(estado, text="Jugador: --")
        self.lbl_jugador.pack(anchor="w")
        self.barra_jugador = ttk.Progressbar(estado, maximum=120, length=550)
        self.barra_jugador.pack(fill="x", pady=(2, 8))
        self.lbl_enemigo = ttk.Label(estado, text="Enemigo: --")
        self.lbl_enemigo.pack(anchor="w")
        self.barra_enemigo = ttk.Progressbar(estado, maximum=105, length=550)
        self.barra_enemigo.pack(fill="x", pady=2)

        acciones = ttk.Frame(contenedor)
        acciones.pack(fill="x", pady=(0, 10))
        self.btn_atacar = ttk.Button(acciones, text="Atacar", command=self.atacar, state="disabled")
        self.btn_atacar.pack(side="left", expand=True, fill="x", padx=(0, 5))
        self.btn_pocion = ttk.Button(acciones, text="Usar poción (+25)", command=self.usar_pocion, state="disabled")
        self.btn_pocion.pack(side="left", expand=True, fill="x", padx=5)
        self.btn_nueva = ttk.Button(acciones, text="Nueva batalla", command=self.iniciar_batalla, state="disabled")
        self.btn_nueva.pack(side="left", expand=True, fill="x", padx=(5, 0))

        registro = ttk.LabelFrame(contenedor, text="Registro de eventos", padding=8)
        registro.pack(fill="both", expand=True)
        self.registro = tk.Text(registro, height=9, wrap="word", state="disabled", font=("Consolas", 9))
        self.registro.pack(fill="both", expand=True)

    def _registrar(self, mensaje):
        self.registro.configure(state="normal")
        self.registro.insert("end", mensaje + "\n")
        self.registro.see("end")
        self.registro.configure(state="disabled")

    def iniciar_batalla(self):
        self.jugador = Guerrero() if self.tipo_personaje.get() == "Guerrero" else Mago()
        self.gestor = GestorBatalla(self.jugador)
        enemigo = self.gestor.iniciar()
        self._registrar(f"Comienza la batalla: {self.jugador.nombre} contra {enemigo.nombre}.")
        self.btn_atacar.configure(state="normal")
        self.btn_pocion.configure(state="normal")
        self.btn_nueva.configure(state="disabled")
        self._actualizar_estado()

    def atacar(self):
        if not self.gestor:
            return
        try:
            for mensaje in self.gestor.turno_jugador():
                self._registrar(mensaje)
            self._actualizar_estado()
            self._comprobar_fin()
        except RuntimeError as error:
            messagebox.showwarning("Aviso", str(error))

    def usar_pocion(self):
        if not self.gestor:
            return
        try:
            curacion = self.gestor.usar_pocion()
            self._registrar(f"Usaste una poción y recuperaste {curacion} puntos de vida.")
            if curacion == 0:
                self._registrar("Tu vida ya está al máximo.")
            if self.gestor.enemigo.esta_vivo:
                danio, descripcion = self.gestor.enemigo.atacar()
                recibido = self.jugador.recibir_danio(danio)
                self._registrar(f"{descripcion} Daño recibido: {recibido}.")
                if not self.jugador.esta_vivo:
                    self.gestor.terminada = True
            self._actualizar_estado()
            self._comprobar_fin()
        except RuntimeError as error:
            messagebox.showwarning("Aviso", str(error))

    def _actualizar_estado(self):
        if not self.jugador or not self.gestor or not self.gestor.enemigo:
            return
        enemigo = self.gestor.enemigo
        self.lbl_jugador.configure(text=f"{self.jugador.nombre}: {self.jugador.vida}/{self.jugador.vida_maxima} HP")
        self.barra_jugador.configure(maximum=self.jugador.vida_maxima, value=self.jugador.vida)
        self.lbl_enemigo.configure(text=f"{enemigo.nombre}: {enemigo.vida}/{enemigo.vida_maxima} HP")
        self.barra_enemigo.configure(maximum=enemigo.vida_maxima, value=enemigo.vida)

    def _comprobar_fin(self):
        if self.gestor.terminada:
            self.btn_atacar.configure(state="disabled")
            self.btn_pocion.configure(state="disabled")
            self.btn_nueva.configure(state="normal")
            if self.jugador.esta_vivo:
                self._registrar("Combate finalizado: ganaste.")
            else:
                self._registrar("Combate finalizado: perdiste. ¡Inténtalo otra vez!")
