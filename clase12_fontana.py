import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Label, Entry, Frame, Button, Combobox

SALARIO_MINIMO = 250_000

class EncuestaApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x300")
        self.root.title('Encuesta')

        self.ENCUESTADOS = []
        self.salario_total = 0

        self.estrato_social = [
            "1 - Bajo", 
            "2 - Medio/Bajo", 
            "3 - Medio", 
            "4 - Medio/Alto", 
            "5 - Alto"
        ]
        self.tipo_trabajo = [
            "1 - Sin trabajo", 
            "2 - Independiente", 
            "3 - Empleado publico", 
            "4 - Empleo privado"
        ]

        self.v_int_cmd = self.root.register(self.validar_entero)
        self.crear_interfaz()

    def validar_entero(self, P: str):
        return P == "" or P.isdigit()

    def limpiar_campos(self):
        self.estrato_dropdown.set(self.estrato_social[0])
        self.tipo_dropdown.set(self.tipo_trabajo[0])
        self.salario_input.delete(0, 'end')

    def guardar(self):
        salario = int(self.salario_input.get() or 0)
        estrato = self.estrato_dropdown.get()
        tipo = self.tipo_dropdown.get()

        if tipo != self.tipo_trabajo[0] and salario < SALARIO_MINIMO:
            messagebox.showerror(title="Salario", message="El salario debe ser Mayor o Igual a $250.000")
            return
        elif salario < 0:
            messagebox.showerror(title="Salario", message="El salario debe ser Mayor o Igual a $0")
            return

        self.ENCUESTADOS.append(estrato)
        self.salario_total += salario

        mensaje = f"Se guardó encuestado:\nEstrato: {estrato}\nSalario: ${salario}"
        messagebox.showinfo(title="Guardado", message=mensaje)
        self.limpiar_campos()

    def calcular(self):
        cant_enc = len(self.ENCUESTADOS)
        if cant_enc == 0:
            messagebox.showinfo(title="Calculo", message="No hay encuestados aún.")
            return

        estrato_bajo = len([x for x in self.ENCUESTADOS if x == self.estrato_social[0]])
        promedio = self.salario_total / cant_enc

        mensaje = (
            f"Cantidad de encuestados: {cant_enc}\n"
            f"Cantidad personas estrato bajo 1: {estrato_bajo}\n"
            f"Promedio: {promedio:.2f}"
        )
        messagebox.showinfo(title="Calculo", message=mensaje)

    def crear_interfaz(self):
        self.root.rowconfigure([0,1,2,3,4], weight=1)
        self.root.columnconfigure([0,1], weight=1)

        Label(self.root, text="Estrato Social:").grid(column=0, row=0, padx=5, pady=5)
        self.estrato_dropdown = Combobox(self.root, values=self.estrato_social, state="readonly")
        self.estrato_dropdown.grid(column=1, row=0, sticky=tk.EW, padx=10, pady=5)
        self.estrato_dropdown.set(self.estrato_social[0])

        Label(self.root, text="Tipo de trabajo:").grid(column=0, row=1, padx=5, pady=5)
        self.tipo_dropdown = Combobox(self.root, values=self.tipo_trabajo, state="readonly")
        self.tipo_dropdown.grid(column=1, row=1, sticky=tk.EW, padx=10, pady=5)
        self.tipo_dropdown.set(self.tipo_trabajo[0])

        Label(self.root, text="Salario mensual (>= $250.000):").grid(column=0, row=2, padx=5, pady=5)
        self.salario_input = Entry(self.root, validate="key", validatecommand=(self.v_int_cmd, "%P"))
        self.salario_input.grid(column=1, row=2, sticky=tk.EW, padx=10, pady=5)

        Frame(self.root).grid(row=3, column=0, columnspan=4)

        button_frame = Frame(self.root)
        button_frame.grid(row=4, column=0, columnspan=4, sticky=tk.EW)

        button_frame.rowconfigure(0, weight=1)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        Button(button_frame, text="Guardar", command=self.guardar).grid(row=0, column=0, ipadx=5, ipady=5)
        Button(button_frame, text="Calcular", command=self.calcular).grid(row=0, column=1, ipadx=5, ipady=5)
        Button(button_frame, text="Salir", command=self.root.quit).grid(row=0, column=2, ipadx=10, ipady=5)


root = tk.Tk()
app = EncuestaApp(root)
root.mainloop()
