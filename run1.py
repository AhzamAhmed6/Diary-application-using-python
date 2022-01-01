from LinkedList import *
from tkinter import *
from tkinter import filedialog

global open_sataus_name
open_status_name = False
path = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages\1.txt'

def create_pages(path, pages=10):
    diary = Doubly_LL()
    diary.add_begin(path+fr'\1.txt')
    for i in range(2,pages+1):
        diary.add_end(path+fr'\{i}.txt')
    return diary

def open_file():
    text_file = open(path, 'r+')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

    global open_sataus_name
    open_status_name = text_file

def save_file():
    global open_status_name
    text_file = open(open_status_name, 'w')
    text_file.write(my_text.get(1.0, END))
    text_file.close()


root = Tk()
root.geometry("500x600")
b1 = Button(root, text='open diary', command=open_file)
b1.pack(pady=20)

b2 = Button(root, text='save', command=save_file)
b2.pack(pady=20)

my_text = Text(root, width=40, height=10, font=('Helvetica', 16))
my_text.pack(pady=20)
root.mainloop()


