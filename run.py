from tkinter import *
from LinkedList import *
import os



def create_pages(path1, n):
    diary = Doubly_LL()
    diary.add_begin(path1+fr'\1.txt')
    for i in range(2, n+1):
        diary.add_end(path1+fr'\{i}.txt')
    return diary

path1 = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages'

def nop():
    nofip=0
    for i in os.listdir(path1):
        nofip+=1
    return nofip   # global number_of_files_in_pages
number_of_files_in_pages = nop()

page_number=1                     # global page_number

def repeat_process(diary):
    global page_number
    

    root = Tk()
    root.title(f'{page_number}.txt')
    root.geometry('1200x660')


    # create next page button
    def next_page():
        global path2, page_number
        # number_of_files_in_pages=nop()
        # if page_number<number_of_files_in_pages:
        #     page_number+=1
        path2=diary.one_step_forward(path2)
        print(page_number)
        root.destroy()
        page_number+=1
        repeat_process(diary=diary)
    common_img = PhotoImage(width=1, height=1)
    b1 = Button(root, text='Next Page >>', image=common_img, width=100, height=20, compound='c', command=next_page)
    b1.pack()


    # create add page button
    def add_page():
        global path1,path2, page_number, diary
        number_of_files_in_pages=nop()
        for page in range(number_of_files_in_pages, page_number, -1):
            os.rename(fr'{path1}\{page}.txt', fr'{path1}\{page+1}.txt')
        
        open(fr'{path1}\{page_number+1}.txt', 'a')  # OK
        number_of_files_in_pages+=1
        diary = create_pages(path1, n=number_of_files_in_pages)
        page_number+=1
        path2=diary.one_step_forward(path2)
        root.destroy()
        repeat_process(diary=diary)

    b6 = Button(root, text='Add Page', image=common_img, width=100, height=20, compound='c', command=add_page)
    b6.pack()


    # create perivous page button
    def privous_page():
        global path2, page_number
        # if page_number>1:
        #     page_number-=1
        path2=diary.one_step_backward(path2)
        print(page_number)
        root.destroy()
        page_number-=1
        repeat_process(diary=diary)
    b2 = Button(root, text='<< Perivous Page', image=common_img, width=100, height=20, compound='c', command=privous_page)
    b2.pack()


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



diary = create_pages(path1, n=number_of_files_in_pages+1)
path2 = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages\1.txt'
repeat_process(diary=diary)
