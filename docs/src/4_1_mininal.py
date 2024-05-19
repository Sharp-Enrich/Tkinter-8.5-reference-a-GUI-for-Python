def createWidgets(self):
    top=self.winfo_toplevel()               # 1
    top.rowconfigure(0, weight=1)           # 2
    top.columnconfigure(0, weight=1)        # 3
    self.rowconfigure(0, weight=1)          # 4
    self.columnconfigure(0, weight=1)       # 5
    self.quit = Button(self, text='Quit', command=self.quit)
    self.quit.grid(row=0, column=0,          # 6
        sticky=tk.N+tk.S+tk.E+tk.W)