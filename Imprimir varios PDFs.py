import os, re, time
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory(initialdir='c://',title="arquivos pdf, impressora padrao")

    
directory = os.listdir(folder_selected)
os.chdir(folder_selected)

for file in directory:
    os.startfile(file, "print")
    time.sleep(1)


