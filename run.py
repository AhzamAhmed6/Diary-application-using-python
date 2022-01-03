from tkinter import *
from LinkedList import *



def create_pages(path, pages=10):
    diary = Doubly_LL()
    diary.add_begin(path+fr'\1.txt')
    for i in range(2,pages+1):
        diary.add_end(path+fr'\{i}.txt')
    return diary



def repeat_process(diary):

    root = Tk()
    root.geometry('1200x660')


    # create next page button
    def next_page():
        global path
        path=diary.one_step_forward(path)
        root.destroy()
        repeat_process(diary=diary)
    b1 = Button(root, text='Next Page >>', command=next_page)
    b1.pack()


    # create perivous page button
    def privous_page():
        global path
        path=diary.one_step_backward(path)
        root.destroy()
        repeat_process(diary=diary)
    b2 = Button(root, text='<< Perivous Page', command=privous_page)
    b2.pack()


# create save_file function
    def save_file():
        text_file = open(path, 'r+')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
    b3 = Button(root, text='Save', command=save_file)
    b3.pack()


    # create a quit button
    def quit():
        root.destroy()
    b4 = Button(root, text='Quit !!', command=quit)
    b4.pack()


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

    root.mainloop()


path = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages'
diary = create_pages(path)
path = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages\1.txt'
repeat_process(diary=diary)
