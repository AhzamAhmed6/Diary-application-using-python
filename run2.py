from tkinter import *
from tkinter import filedialog
from tkinter import font
from LinkedList import *



def create_pages(path, pages=10):
    diary = Doubly_LL()
    diary.add_begin(path+fr'\1.txt')
    for i in range(2,pages+1):
        diary.add_end(path+fr'\{i}.txt')
    return diary

global open_status
open_status = False

def repeat_process(diary):

    root = Tk()
    root.geometry('1200x660')

    
    # create a quit button
    def quit():
        root.destroy()
    b2 = Button(root, text='Quit', command=quit)
    b2.pack(pady=20)


    # create next page button
    def next_page():
        global path
        path=diary.one_step_forward(path)
        root.destroy()
        repeat_process(diary=diary)
    b2 = Button(root, text='Next Page', command=next_page)
    b2.pack(pady=20)


    # create perivous page button
    def next_page():
        global path
        path=diary.one_step_backward(path)
        root.destroy()
        repeat_process(diary=diary)
    b2 = Button(root, text='Perivous Page', command=next_page)
    b2.pack(pady=20)


    # create main frome
    my_frame = Frame(root)
    my_frame.pack(pady=5)


    # create text box
    my_text = Text(my_frame, width=97, height=25, undo=True, font=('Helvetica', 16))
    my_text.pack()

    text_file = open(path, 'r+')
    global open_status    
    open_status = text_file
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()



    # create save_file function
    def save_file():
        global open_status
        if open_status:
            text_file = open(path, 'r+')
            text_file.write(my_text.get(1.0, END))
            text_file.close()




    # create menue
    my_menu = Menu(root)
    root.config(menu=my_menu)

    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='save', command=save_file)

    root.mainloop()


path = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages'
diary = create_pages(path)
path = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages\1.txt'
repeat_process(diary=diary)
