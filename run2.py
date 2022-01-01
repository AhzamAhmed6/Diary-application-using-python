from tkinter import *
from tkinter import filedialog
from tkinter import font
from LinkedList import *

i = 1
def repeat_process():
    path = fr'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages\{i}.txt'
    def create_pages(path, pages=10):
        diary = Doubly_LL()
        diary.add_begin(path+fr'\1.txt')
        for i in range(2,pages+1):
            diary.add_end(path+fr'\{i}.txt')
        return diary



    root = Tk()
    root.geometry('1200x660')


    # create a quit button
    def quit():
        root.destroy()
    b2 = Button(root, text='Quit', command=quit)
    b2.pack(pady=20)



    # create next page button
    def next_page():
        global i
        i+=1
        root.destroy()
        repeat_process()
    b2 = Button(root, text='Next Page', command=next_page)
    b2.pack(pady=20)



    # create main frome
    my_frame = Frame(root)
    my_frame.pack(pady=5)


    # create text box
    my_text = Text(my_frame, width=97, height=25, undo=True, font=('Helvetica', 16))
    my_text.pack()

    text_file = open(path, 'r+')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


    # create menue
    my_menu = Menu(root)
    root.config(menu=my_menu)

    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='Open diary')
    file_menu.add_command(label='save')

    root.mainloop()

repeat_process()
