from tkinter import ttk
from entry_pop import EntryPopup

class HorariosTable(ttk.Treeview):

    def __init__(self, parent, *args, **kwargs):
        columns = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        super().__init__(parent, columns=columns, show="tree headings", style="Custom.Treeview", *args, **kwargs)
        self.column("#0", width=60, anchor="center")
        self.heading("#0", text="HORARIO")
        for col in columns:
            self.column(col, anchor="center", width=100)
            self.heading(col, text=col)
        self.tag_configure("hora", background="#F4B400", foreground="black", font=("Arial", 10, "bold"))
        for hora in range(7, 24):
            self.insert("", "end", text=str(hora), values=["" for _ in columns])
        self.bind("<Double-1>", self.on_double_click)
        



    def on_double_click(self, event):
        try:
            self.entryPopup.destroy()
        except AttributeError:
            pass
        rowid = self.identify_row(event.y)
        column = self.identify_column(event.x)
        if not rowid or column == "#0":
            return
        x, y, width, height = self.bbox(rowid, column)
        pady = height // 2
        col_index = int(column[1:]) - 1
        text = self.item(rowid, 'values')[col_index]
        self.entryPopup = EntryPopup(self, rowid, col_index, text)
        self.entryPopup.place(x=x, y=y + pady, width=width, height=height, anchor='w')


    def get_column(self, column_name):
        return [
            self.item(id_, "values")[self["columns"].index(column_name)]
            for id_ in self.get_children()
        ]

    def get_row(self, row_index):
        return self.item(self.get_children()[row_index], "values")
    
    def get_horario_completo(self):
        horarios = {}
        for item_id in self.get_children():
            hora = self.item(item_id, "text")  # texto = hora (7, 8, ...)
            valores = self.item(item_id, "values")  # lista de valores por día
            horarios[hora] = dict(zip(self["columns"], valores))
        return horarios