import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sqlite3
import os
import time
import shutil
 
 
 
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Drill 124")
        self.minsize(300, 250)
        self.var2=StringVar()
        self.var1=StringVar()
        
 
        self.labelFrame = ttk.LabelFrame(self, text = "Select files")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

        
 
        self.button()
        self.button2()
        self.button3()
    
               
 
 
 
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Choose a source directory",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    def button2(self):
        self.button = ttk.Button(self.labelFrame, text = "Choose a destination directory",command = self.fileDialog2)
        self.button.grid(column = 3, row = 1)

    def button3(self):
        self.button = ttk.Button(self.labelFrame, text = "Transfer text files",command = self.sortFunction)
        self.button.grid(column = 2, row = 4)
 
 
    def fileDialog(self):
 
        self.filename = filedialog.askdirectory(initialdir =  "/", title = "Select A directory") 
        self.label = ttk.Label(self.labelFrame, textvariable = self.var1)
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)
        if self.label != "":            
            self.var1.set(self.filename)
            print(self.var1)
            
            
            
        
        

    def fileDialog2(self):
 
        self.filename = filedialog.askdirectory(initialdir =  "/", title = "Select A directory") 
        self.label = ttk.Label(self.labelFrame, textvariable = self.var2)
        self.label.grid(column = 3, row = 2)
        self.label.configure(text = self.filename)        
        self.var2.set(self.filename)
        print(self.var2)

    
           

    #db    
    conn = sqlite3.connect('test11.db')

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_file TEXT NOT NULL, col_time datetime \
            )")
        conn.commit()
    conn.close()


    conn = sqlite3.connect('test11.db')
    #End db
    
    #Sort by txt
    def sortFunction(self):
        source = os.listdir(self.var1.get())
        destination = self.var2.get()        
        for files in source:            
            if files.endswith('.txt'):
                abPath = os.path.join(self.var1.get(), files)
                getTime = os.path.getmtime(abPath)
                print(files)                
                shutil.move(abPath,destination)                
                conn = sqlite3.connect('test11.db')
                with conn:                    
                    cur = conn.cursor()
                    print(getTime)
                    cur.execute("INSERT INTO tbl_files(col_file, col_time) VALUES (?, ?)", \
                        (abPath, getTime))                  
                    
                    conn.commit()
                conn.close()
                    
    #End sort
 
 
 
if __name__ == "__main__":
    root = Root()
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)
    root.columnconfigure(6, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.mainloop()
