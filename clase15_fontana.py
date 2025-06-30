import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def validar_entero(P: str):
    return P.isdigit() or P == ""

class EstilosApp(ttk.Style):
    def __init__(self, root):
        super().__init__()
        self.theme_use('clam')
        self.configure('TFrame', background='#f4f6fb')
        self.configure('TLabel', background='#f4f6fb', font=("Arial", 11))
        self.configure('Title.TLabel', font=("Arial", 14, "bold"), foreground="#2a3d66")
        self.configure('TButton', font=("Arial", 11, "bold"), background="#2a3d66", foreground="#fff")
        self.map('TButton', background=[('active', '#3e5c99')])
        self.configure('Localidad.TLabel', font=("Arial", 12, "bold"), foreground="#1a237e", background='#f4f6fb')
        self.configure('Modern.TEntry', font=("Arial", 12), fieldbackground="#fff", borderwidth=2, relief="flat", padding=6)
        self.map(
            'Modern.TEntry',
            fieldbackground=[('active', '#e3eaff'), ('focus', '#e3eaff')],
            bordercolor=[('focus', '#3e5c99')]
        )

class BoleteriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Boletería - Evento Deportivo")
        self.root.geometry("540x370")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6fb")

        self.estilos = EstilosApp(root)

        self.precios = {
            'General': 20000,
            'Tribuna': 40000,
            'Platea': 70000
        }

        self.entradas_vendidas = {
            'General': 0,
            'Tribuna': 0,
            'Platea': 0
        }

        self.entries = {}

        main_frame = ttk.Frame(root)
        main_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Título
        title_label = ttk.Label(main_frame, text="Ingrese cantidad de entradas que desea el comprador:", style='Title.TLabel', anchor='center', justify='center')
        title_label.grid(row=0, column=0, columnspan=2, pady=(18, 8), sticky='ew')
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Frame de localidades
        frame = ttk.Frame(main_frame)
        frame.grid(row=1, column=0, columnspan=2, pady=5, sticky='ew')
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        v_int_cmd = root.register(validar_entero)

        # Entradas de localidades
        for idx, localidad in enumerate(self.precios):
            label = ttk.Label(frame, text=localidad, width=10, anchor='e', style='Localidad.TLabel')
            label.grid(row=idx, column=0, padx=(0, 10), pady=8, sticky='e')

            entry = ttk.Entry(frame, width=10, justify='center', style='Modern.TEntry', validate='key', validatecommand=(v_int_cmd, '%P'))
            entry.insert(0, '0')
            entry.grid(row=idx, column=1, padx=(10, 0), pady=8, ipady=2, sticky='w')

            self.entries[localidad] = entry

        sep = ttk.Separator(main_frame, orient='horizontal')
        sep.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10, pady=12)

        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)

        cobrar_btn = ttk.Button(button_frame, text="Cobrar", width=14, command=self.cobrar)
        cobrar_btn.grid(row=0, column=0, padx=8, pady=2, sticky='ew')

        totalizar_btn = ttk.Button(button_frame, text="Totalizar", width=14, command=self.totalizar)
        totalizar_btn.grid(row=0, column=1, padx=8, pady=2, sticky='ew')

        salir_btn = ttk.Button(button_frame, text="Salir", width=14, command=self.root.quit)
        salir_btn.grid(row=0, column=2, padx=8, pady=2, sticky='ew')

    def cobrar(self):
        total_persona = 0
        mensaje = "Detalle de la compra:\n"
        cantidades_temp = {}
        for localidad, entry in self.entries.items():
            valor = entry.get()
            if valor == "":
                cantidad = 0
            else:
                cantidad = int(valor)
            cantidades_temp[localidad] = cantidad

        for localidad, cantidad in cantidades_temp.items():
            if cantidad > 0:
                precio = self.precios[localidad]
                subtotal = cantidad * precio
                total_persona += subtotal
                self.entradas_vendidas[localidad] += cantidad
                mensaje += f"{localidad}: {cantidad} x ${precio:,} = ${subtotal:,}\n"

        mensaje += f"\nTotal a pagar: ${total_persona:,}"
        messagebox.showinfo("Cobro", mensaje)
        self.reset_entries()

    def totalizar(self):
        mensaje = "Boletos vendidos por localidad:\n"
        total_general = 0

        for localidad, cantidad in self.entradas_vendidas.items():
            total_local = cantidad * self.precios[localidad]
            mensaje += f"{localidad}: {cantidad} entradas - Total: ${total_local:,}\n"
            total_general += total_local

        mensaje += f"\nTotal general vendido: ${total_general:,}"
        messagebox.showinfo("Totalización", mensaje)

    def reset_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
            entry.insert(0, '0')

if __name__ == "__main__":
    root = tk.Tk()
    app = BoleteriaApp(root)
    root.mainloop()