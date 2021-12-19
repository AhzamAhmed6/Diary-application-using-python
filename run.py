from LinkedList import *
from tkinter import *
import subprocess
import os

def create_pages(path, pages=10):
    diary = LinkedList()
    diary.add_begin(path+fr'\1.txt')
    # open(path+r'\1.txt', 'w')/
    for i in range(2,pages+1):
        diary.add_after(path+fr'\{i}.txt', path+fr'\{i-1}.txt')
        # open(path+fr'\{i}.txt', 'w')
    return diary


page_number = int(input('Enter the page number: '))
path = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages'
diary = create_pages(path, 10)

p = fr'{path}\{page_number}.txt'
os.system(p)
while True:    
    next_page = input('Next Page?\nYes(y),   No(n)  : ')
    if next_page == 'y':
        p = diary.move_next_node(p)
        # p = fr'{path}\{page_number}.txt'
        os.system(p)       
    else:
        break
