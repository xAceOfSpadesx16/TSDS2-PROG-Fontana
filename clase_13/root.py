import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from table import HorariosTable
import os
from menu import MenuBar

class Root(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("800x600")
        self.title("Gestión de Actividades")
        self.tree = None  # Solo almacena los datos, no se muestra
        self.tree_style()
        self.table_window = None

        # --- Muestra de logo.png ---
        self.logo_img = None
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        try:
            # Intentar cargar con PIL si está disponible
            try:
                from PIL import Image, ImageTk
                image = Image.open(logo_path)
                image = image.resize((150, 150))
                self.logo_img = ImageTk.PhotoImage(image)
            except ImportError:
                # Si no hay PIL, intentar con PhotoImage estándar
                self.logo_img = tk.PhotoImage(file=logo_path)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.logo_img = None

        if self.logo_img:
            self.logo_label = tk.Label(self, image=self.logo_img)
            self.logo_label.pack(pady=20)
        # --- Fin imagen ---

        # Usar la barra de menú modular
        self.config(menu=MenuBar(self))

    def abrir_ventana_carga(self):
        if self.table_window and tk.Toplevel.winfo_exists(self.table_window):
            self.table_window.lift()
            return
        self.table_window = tk.Toplevel(self)
        self.table_window.title("Carga de Actividades")
        self.table_window.geometry("700x500")
        self.table_window.transient(self)
        self.table_window.grab_set()
        self.table_window.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_carga)
        self.table = HorariosTable(self.table_window)
        self.table.pack(fill="both", expand=True)
        # Copiar datos actuales si existen
        if self.tree:
            for idx, item_id in enumerate(self.tree.get_children()):
                valores = self.tree.item(item_id, "values")
                self.table.item(self.table.get_children()[idx], values=valores)

    def cerrar_ventana_carga(self):
        # Guardar los datos cargados en la tabla principal
        if self.table:
            if not self.tree:
                # Crear tabla oculta para almacenar datos
                self.tree = HorariosTable(self)
                self.tree.pack_forget()
            for idx, item_id in enumerate(self.tree.get_children()):
                valores = self.table.item(self.table.get_children()[idx], "values")
                self.tree.item(item_id, values=valores)
        self.table_window.destroy()
        self.table_window = None

    def initialize_ui(self):
        if self.tree:
            self.tree.destroy()
        self.tree = HorariosTable(self)
        self.tree.pack_forget()

    def tree_style(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Custom.Treeview",
                        background="white",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="white",
                        bordercolor="black",
                        borderwidth=1)
        style.configure("Custom.Treeview.Heading",
                        background="#F4B400",
                        foreground="black",
                        font=("Arial", 10, "bold"),
                        )
        style.layout("Custom.Treeview", [
            ('Treeview.field', {'sticky': 'nswe', 'children': [
                ('Treeview.padding', {'sticky': 'nswe', 'children': [
                    ('Treeview.treearea', {'sticky': 'nswe'})
                ]})
            ]})
        ])