# import os
import subprocess
# from tkinter import *

# def myfunc():
#     

# root = Tk()
# mybutton = Button(root, text='Click Me', command=myfunc())
# mybutton.pack()
# root=mainloop()


import tkinter
# import tkMessageBox

top = tkinter.Tk()

def nextpage():
   subprocess.call(['notepad', r"C:\Users\Lenovo\Downloads\visual stdio programs\Python_Programs\Data-Structure-Project-2\pages\fr.txt"])

B = tkinter.Button(top, text ="Next Page", command = nextpage)

B.pack()
top.mainloop()