from tkinter import *
from LinkedList import *
import os



def create_pages(path1, n):
    diary = Doubly_LL()
    diary.add_begin(path1+fr'\1.txt')
    for i in range(2, n):
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
        path2=diary.one_step_forward(path2)
        print(page_number)
        root.destroy()
        page_number+=1
        repeat_process(diary=diary)


    # create add page button
    def add_page():
        global path1,path2, page_number, diary
        number_of_files_in_pages=nop()
        for page in range(number_of_files_in_pages, page_number, -1):
            os.rename(fr'{path1}\{page}.txt', fr'{path1}\{page+1}.txt')
        
        open(fr'{path1}\{page_number+1}.txt', 'a')  # OK
        number_of_files_in_pages+=1
        diary = create_pages(path1, n=number_of_files_in_pages+1)
        page_number+=1
        path2=diary.one_step_forward(path2)
        root.destroy()
        repeat_process(diary=diary)



    # create delete page button
    def delete_page():
        global path1,path2, page_number, diary
        number_of_files_in_pages=nop()
        if number_of_files_in_pages == page_number:
            path2=diary.one_step_backward(path2)
            os.remove(fr'{path1}\{page_number}.txt')
            root.destroy()
            page_number-=1
            repeat_process(diary=diary)
        else:
            os.remove(fr'{path1}\{page_number}.txt')
            for page in range(page_number, number_of_files_in_pages):
                os.rename(fr'{path1}\{page+1}.txt', fr'{path1}\{page}.txt')
            
            open(fr'{path1}\{page_number}.txt', 'r+')  # OK
            number_of_files_in_pages-=1
            diary = create_pages(path1, n=number_of_files_in_pages+1)
            # page_number+=1
            # path2=diary.one_step_forward(path2)
            root.destroy()
            repeat_process(diary=diary)


    # # create perivous page button
    def privous_page():
        global path2, page_number
        # if page_number>1:
        #     page_number-=1
        path2=diary.one_step_backward(path2)
        print(page_number)
        root.destroy()
        page_number-=1
        repeat_process(diary=diary)


    # # create save_file function
    def save_file():
        text_file = open(path2, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()


    # create a quit button
    def quit():
        root.destroy()



    # create main frome
    my_frame = Frame(root)
    my_frame.grid(row=2, column=0, sticky="ns")


    # create text box
    my_text = Text(my_frame, width=97, height=25, undo=True, font=('Helvetica', 16))
    my_text.pack()

    text_file = open(path2, 'r+')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()  

    my_menu = Menu(root)
    root.config(menu=my_menu)


    # create menue bar
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='New', command=add_page) 
    file_menu.add_command(label='Delete', command=delete_page)
    file_menu.add_command(label='Next Page', command=next_page) 
    file_menu.add_command(label='Perivous Page', command=privous_page)
    file_menu.add_command(label='Save', command=save_file)  
    file_menu.add_command(label='Exit', command=quit) 

    root.mainloop()



diary = create_pages(path1, n=number_of_files_in_pages+1)
path2 = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages\1.txt'
repeat_process(diary=diary)
