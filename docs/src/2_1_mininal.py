#!/usr/bin/env python      # 1
import tkinter as tk       # 2

class Application(tk.Frame):              # 3
    def __init__(self, master=None):
        super().__init__(master)          # 4
        self.grid()                       # 5
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='退出',
            command=self.quit)            # 6
        self.quitButton.grid()            # 7

app = Application()                       # 8
app.master.title('示例应用程序')    # 9
app.mainloop()                            # 10
