
import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(1510, 610))
        self.master.title("Check files")
        self.master.config(bg='lightgray')

        

        self.txtBrowse1 = Entry(self.master,text='', font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse1.grid(row=1, column=2, rowspan=2, columnspan=8, padx=(170,0), pady=(75,0), sticky="NSEW")

        self.txtBrowse2 = Entry(self.master,text='', font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse2.grid(row=3, column=2, rowspan=2, columnspan=8, padx=(170,0), pady=(70,0), sticky="NSEW")

        





        self.btnSubmit = Button(self.master, text="Browse...", width=18, height=2, font=("Helvetica", 20))
        self.btnSubmit.grid(row=2, column=0, rowspan=10, columnspan=4, padx=(0,0), pady=(0,0), sticky="NW")

        self.btnSubmit2 = Button(self.master, text="Browse...", width=18, height=2, font=("Helvetica", 20))
        self.btnSubmit2.grid(row=4, column=0, rowspan=10, columnspan=4, padx=(0,0), pady=(0,0), sticky="NW")

        self.btnSubmit = Button(self.master, text="Check for files...", width=18, height=3, font=("Helvetica", 20))
        self.btnSubmit.grid(row=8, column=0, rowspan=10, columnspan=4, padx=(0,0), pady=(80,0), sticky="NW")

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=2, command=self.cancel, font=("Helvetica", 20))
        self.btnCancel.grid(row=10, column=9, padx=(100,0), pady=(0,0), sticky="SE")

    

    def cancel(self):
        self.master.destroy()




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)
    root.columnconfigure(6, weight=1)
    root.columnconfigure(7, weight=1)
    root.columnconfigure(8, weight=1)
    root.columnconfigure(9, weight=1)
    root.columnconfigure(10, weight=1)
    root.columnconfigure(11, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)
    root.rowconfigure(9, weight=1)
    root.rowconfigure(10, weight=1)
    root.rowconfigure(11, weight=1)
    root.rowconfigure(12, weight=1)
    root.rowconfigure(13, weight=1)
    root.mainloop()
