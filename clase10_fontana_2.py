import tkinter as tk
from tkinter import messagebox
from statistics import mean

BOLETINES: dict[str, list] = {}

def validar_entero(P: str):
    return P == "" or P.isdigit()


def validar_requeridos(codigo, prim_trim, seg_trim, terc_trim):
    return all([codigo, prim_trim, seg_trim, terc_trim])


def limpiar_campos():
    alumno_cod_input.delete(0, 'end')
    primer_tri_input.delete(0, 'end')
    seg_tri_input.delete(0, 'end')
    tercer_tri_input.delete(0, 'end')


def calcular():
    codigo = alumno_cod_input.get()
    prim_tri = primer_tri_input.get()
    seg_tri = seg_tri_input.get()
    terc_tri = tercer_tri_input.get()

    if not validar_requeridos(codigo, prim_tri, seg_tri, terc_tri):
        mensaje = "Todos los campos son requeridos."
        messagebox.showerror(title="Campos requeridos", message= mensaje)
        return
    
    notas = [int(prim_tri), int(seg_tri), int(terc_tri)]
    if any(nota < 0 or nota > 10 for nota in notas):
        messagebox.showerror("Error de nota", "Todas las notas deben ser mayores o iguales a 0 y menores o iguales a 10.")
        return
    
    BOLETINES[codigo] = mean(notas)
    messagebox.showinfo("Promedio de alumno", message=f"El promedio de {codigo} es {BOLETINES[codigo]}")
    limpiar_campos()


def totalizar():
    # Cantidad de alumnos aprobados "promedio >= 7"
    aprobados = len([x for x in BOLETINES.values() if x >=7])

    # Rinde en diciembre "4<= promedio < 7"
    diciembre = len([x for x in BOLETINES.values() if 4 <= x < 7])

    # Rinde en marzo "promedio < 4"
    marzo = len([x for x in BOLETINES.values() if x < 4])

    messagebox.showinfo("Totalizador", f"Aprobados: {aprobados}.\nA diciembre: {diciembre}.\nA marzo: {marzo}.")

# main window
root = tk.Tk()
root.geometry("600x300")
root.title('Situacion de los alumnos')

v_int_cmd = root.register(validar_entero)

# grid 6x2
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# Codigo alumno
alumno_cod_label = tk.Label(root, text="Codigo de alumno:")
alumno_cod_label.grid(column=0, row=0, padx=5, pady=5)

alumno_cod_input = tk.Entry(root)
alumno_cod_input.grid(column=1, row=0, sticky=tk.EW, padx=10, pady=5)


# 1° trimestre
primer_tri_label = tk.Label(root, text="Nota 1° trimestre:")
primer_tri_label.grid(column=0, row=1, padx=5, pady=5)

primer_tri_input =  tk.Entry(root, validate="key", validatecommand=(v_int_cmd, "%P"))
primer_tri_input.grid(column=1, row=1, sticky=tk.EW, padx=10, pady=5)


# 2° trimestre
seg_tri_label = tk.Label(root, text="Nota 2° trimestre:")
seg_tri_label.grid(column=0, row=2, padx=5, pady=5)

seg_tri_input =  tk.Entry(root, validate="key", validatecommand=(v_int_cmd, "%P"))
seg_tri_input.grid(column=1, row=2, sticky=tk.EW, padx=10, pady=5)


# 3° trimestre
tercer_tri_label = tk.Label(root, text="Nota 3° trimestre:")
tercer_tri_label.grid(column=0, row=3, padx=5, pady=5)

tercer_tri_input =  tk.Entry(root, validate="key", validatecommand=(v_int_cmd, "%P"))
tercer_tri_input.grid(column=1, row=3, sticky=tk.EW, padx=10, pady=5)


# Frame en blanco para espaciado.
blank_frame = tk.Frame(root)
blank_frame.grid(row=4, column=0, columnspan=4)

# Botonera
button_frame= tk.Frame(root)
button_frame.rowconfigure(0, weight=1)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

button_frame.grid(row=5, column=0, columnspan=4, sticky=tk.EW)


button_nuevo = tk.Button(button_frame, text="Calcular", command=calcular)
button_nuevo.grid(row=0, column=0, ipadx=5, ipady=5)

button_calc = tk.Button(button_frame, text="Totalizar", command=totalizar)
button_calc.grid(row=0, column=1, ipadx=5, ipady=5)

button_salir = tk.Button(button_frame, text="Salir", command=root.quit)
button_salir.grid(row=0, column=2, ipadx=10, ipady=5)

root.mainloop()