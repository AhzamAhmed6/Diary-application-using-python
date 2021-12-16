from LinkedList import *
from tkinter import *
import subprocess

def create_pages(pages, path):
    diary = LinkedList()
    diary.add_begin(path+fr'\1.txt')
    open(path+r'\1.txt', 'w')
    for i in range(2,pages+1):
        diary.add_after(path+fr'\{i}.txt', path+fr'\{i-1}.txt')
        open(path+fr'\{i}.txt', 'w')
    return diary

page_number = int(input('Enter the page number: '))
def myClick(page_number=page_number):
    p = fr'{path}\{page_number-1}.txt'
    subprocess.call(['notepad.exe', p])
    p = diary.move_next_node(p)
    page_number += 1

path = r'C:\Users\Lenovo\Downloads\visual stdio programs\Python_Programs\Data-Structure-Project-2\pages'
diary = create_pages(10, path)


root = Tk()
myButton = Button(root, text = 'Click Me!', command=myClick)
myButton.pack()
root.mainloop()