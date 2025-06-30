from tkinter import ttk

class EntryPopup(ttk.Entry):
    def __init__(self, tree, iid, column, text, **kw):
        super().__init__(tree, **kw)
        self.tv = tree
        self.iid = iid
        self.column = column

        self.insert(0, text) 
        self['exportselection'] = False 
        self.focus_force()
        self.select_all()
        self.bind("<Return>", self.on_return)
        self.bind("<Control-a>", self.select_all)
        self.bind("<Escape>", lambda *ignore: self.destroy())

    def on_return(self, event):
        '''Insert text into treeview, and delete the entry popup'''
        rowid = self.iid
        vals = self.tv.item(rowid, 'values')
        vals = list(vals)
        vals[self.column] = self.get()
        self.tv.item(rowid, values=vals)
        self.destroy()
        
    def select_all(self, *ignore):
        ''' Set selection on the whole text '''
        self.selection_range(0, 'end')
        return 'break'


