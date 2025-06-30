import tkinter as tk
# from tkinter import ttk
def validar_entero(P: str):
    return P.isdigit() or P==""

def nueva_conversion():
    pulgadas_input.delete(0, 'end')
    cent_result.config(text="")

def convertir():
    if pulgadas_input.get():
        pulgadas = int(pulgadas_input.get())
        centimetros = pulgadas*2.54
        cent_result.config(text=centimetros)

# main window
root = tk.Tk()
root.geometry("600x300")
root.title('Convertir pulgadas a centimetros')

v_int_cmd = root.register(validar_entero)

# grid 3x2
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# username
pulgadas_label = tk.Label(root, text="Medida en Pulgadas:")
pulgadas_label.grid(column=0, row=0, padx=5, pady=5)

pulgadas_input = tk.Entry(root, validate="key", validatecommand=(v_int_cmd, "%P"))
pulgadas_input.grid(column=1, row=0, sticky=tk.EW, padx=10, pady=5)

# password
cent_label = tk.Label(root, text="Medida en centimetros:")
cent_label.grid(column=0, row=1, padx=5, pady=5)

cent_result = tk.Label(root, text="")
cent_result.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

blank_frame = tk.Frame(root)
blank_frame.grid(row=2, column=0, columnspan=4)

button_frame= tk.Frame(root)
button_frame.rowconfigure(0, weight=1)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

button_frame.grid(row=3, column=0, columnspan=4, sticky=tk.EW)


button_nuevo = tk.Button(button_frame, text="Nuevo", command=nueva_conversion)
button_nuevo.grid(row=0, column=0, ipadx=5, ipady=5)

button_calc = tk.Button(button_frame, text="Calcular", command=convertir)
button_calc.grid(row=0, column=1, ipadx=5, ipady=5)

button_salir = tk.Button(button_frame, text="Salir", command=root.quit)
button_salir.grid(row=0, column=2, ipadx=10, ipady=5)

root.mainloop()


