from LinkedList import *
import tkinter
import subprocess


def create_pages(pages, path):
    '''
    Parameters :
    =====================
    pages : No of pages you want in your diary
    path : path of the diary
    '''

    diary = LinkedList()
    diary.add_begin(path+fr'\1.txt')
    open(path+r'\1.txt', 'w')
    for i in range(2,pages+1):
        diary.add_after(path+fr'\{i}.txt', path+fr'\{i-1}.txt')
        open(path+fr'\{i}.txt', 'w')
    return diary


def nextpage():
    '''
    Parameters : 
    =================================
    page_number : page number you wants to open
    path : path of your diary
    '''

    p = fr'{path}\{page_number-1}.txt'
    p = diary.move_next_node(p)
    subprocess.call(['notepad.exe', p])




page_number = int(input('Enter the page number: '))
path = r'C:\Users\Lenovo\Downloads\visual stdio programs\Python_Programs\Data-Structure-Project-2\pages'
diary = create_pages(10, path)
diary.print_LL()
while True:
    top = tkinter.Tk()
    B = tkinter.Button(top, text = "Next Page", command = nextpage)
    B.pack()
    top.mainloop()