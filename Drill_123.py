
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
 
 
 
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.minsize(300, 250)
        self.var1=StringVar()
        
 
        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
 
        self.button()
 
 
 
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Choose a source directory",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
 
 
    def fileDialog(self):
 
        self.filename = filedialog.askdirectory(initialdir =  "/", title = "Select A directory") 
        self.label = ttk.Label(self.labelFrame, textvariable = self.var1)
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)
        if self.label != "":            
            self.var1.set(self.filename)
 
 
 
 
if __name__ == "__main__":
    root = Root()
    root.mainloop()
