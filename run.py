from tkinter import *
from LinkedList import *



def create_pages(path1, pages):
    diary = Doubly_LL()
    diary.add_begin(path1+fr'\1.txt')
    for i in range(2,pages+1):
        diary.add_end(path1+fr'\{i}.txt')
    return diary



def repeat_process(diary):

    root = Tk()
    root.geometry('1200x660')


    # # create view all pages button
    # def view_all():
    #     for i in range(1, 10):
    #         root = Tk()
    #         root.geometry('1200x660')
    #         my_frame = Frame(root)
    #         my_frame.pack(pady=5)
    #         # create text box
    #         my_text = Text(my_frame, width=97, height=25, undo=True, font=('Helvetica', 16))
    #         my_text.pack()
    #         path = fr'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages\{i}.txt'
    #         text_file = open(path, 'r+')
    #         stuff = text_file.read()
    #         my_text.insert(END, stuff)
    #         text_file.close() 
    #         root.mainloop()
    #         # repeat_process(diary)
    # common_img = PhotoImage(width=1, height=1)
    # b5 = Button(root, text='View all pages', image=common_img, width=100, height=20, compound='c', command=view_all)
    # b5.pack()


    # create next page button
    def next_page():
        global path2
        path2=diary.one_step_forward(path2)
        root.destroy()
        repeat_process(diary=diary)
    common_img = PhotoImage(width=1, height=1)
    b1 = Button(root, text='Next Page >>', image=common_img, width=100, height=20, compound='c', command=next_page)
    b1.pack()


    # create perivous page button
    def privous_page():
        global path2
        path2=diary.one_step_backward(path2)
        root.destroy()
        repeat_process(diary=diary)
    b2 = Button(root, text='<< Perivous Page', image=common_img, width=100, height=20, compound='c', command=privous_page)
    b2.pack()


    # create add page button
    def add_page():
        global path2
        pages = diary.print_LL_forward()
        path = fr'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages\{pages+1}.txt'
        open(path, 'a')
        diary.add_after(path, path2)        
        pages+=1
        path2=diary.one_step_forward(path2)
        root.destroy()
        repeat_process(diary=diary)

    b6 = Button(root, text='Add Page', image=common_img, width=100, height=20, compound='c', command=add_page)
    b6.pack()


    # create save_file function
    def save_file():
        text_file = open(path2, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
    b3 = Button(root, text='Save', image=common_img, width=100, height=20, compound='c', command=save_file)
    b3.pack()


    # create a quit button
    def quit():
        root.destroy()
    b4 = Button(root, text='Quit !!', image=common_img, width=100, height=20, compound='c', command=quit)
    b4.pack()


    # create main frome
    my_frame = Frame(root)
    my_frame.pack(pady=5)


    # create text box
    my_text = Text(my_frame, width=97, height=25, undo=True, font=('Helvetica', 16))
    my_text.pack()

    text_file = open(path2, 'r+')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()    

    root.mainloop()


path1 = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages'
pages=10
diary = create_pages(path1, pages)
path2 = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages\1.txt'
repeat_process(diary=diary)
