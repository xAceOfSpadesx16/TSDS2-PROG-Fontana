import tkinter as tk
from tkinter import simpledialog, messagebox

class ActividadesMenu(tk.Menu):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, tearoff=0, *args, **kwargs)
        self.root = root
        self.add_command(label="Carga", command=root.abrir_ventana_carga)

class BusquedaMenu(tk.Menu):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, tearoff=0, *args, **kwargs)
        self.root = root
        self.add_command(label="Por día", command=self.buscar_por_dia)
        self.add_command(label="Por día y hora", command=self.buscar_por_dia_y_hora)

    def buscar_por_dia(self):
        dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        if not self.root.tree:
            messagebox.showinfo("Sin datos", "Primero debe cargar actividades.")
            return
        
        dia = simpledialog.askstring("Buscar por día", "Ingrese el día (Lunes a Viernes):", parent=self.root)
        if not dia:
            return
        dia = dia.capitalize()
        if dia not in dias:
            messagebox.showerror("Error", "Día inválido.")
            return
        actividades = []
        for item_id in self.root.tree.get_children():
            hora = self.root.tree.item(item_id, "text")
            valores = self.root.tree.item(item_id, "values")
            idx = dias.index(dia)
            actividad = valores[idx]
            if actividad and actividad.strip():
                actividades.append(f"{hora}: {actividad}")
        if actividades:
            messagebox.showinfo(f"Actividades del {dia}", "\n".join(actividades))
        else:
            messagebox.showinfo(f"Sin actividades", f"No hay actividades programadas para {dia}.")

    def buscar_por_dia_y_hora(self):
        dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        if not self.root.tree:
            messagebox.showinfo("Sin datos", "Primero debe cargar actividades.")
            return
        dia = simpledialog.askstring("Buscar por día y hora", "Ingrese el día (Lunes a Viernes):", parent=self.root)
        if not dia:
            return
        dia = dia.capitalize()
        if dia not in dias:
            messagebox.showerror("Error", "Día inválido.")
            return
        hora = simpledialog.askinteger("Buscar por día y hora", "Ingrese la hora (7 a 23):", parent=self.root, minvalue=7, maxvalue=23)
        if hora is None:
            return
        for item_id in self.root.tree.get_children():
            if self.root.tree.item(item_id, "text") == str(hora):
                valores = self.root.tree.item(item_id, "values")
                idx = dias.index(dia)
                actividad = valores[idx]
                if actividad and actividad.strip():
                    messagebox.showinfo("Actividad", f"Actividad para {dia} a las {hora}: {actividad}")
                else:
                    messagebox.showinfo("Sin actividad", f"No hay actividades programadas para {dia} a las {hora}.")
                return
        messagebox.showinfo("Sin actividad", f"No hay actividades programadas para {dia} a las {hora}.")

class MenuBar(tk.Menu):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.actividades_menu = ActividadesMenu(root)
        self.busqueda_menu = BusquedaMenu(root)
        self.add_cascade(label="Actividades", menu=self.actividades_menu)
        self.add_cascade(label="Búsqueda", menu=self.busqueda_menu)
        self.add_command(label="Salir", command=root.quit)