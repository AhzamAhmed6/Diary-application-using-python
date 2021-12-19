from LinkedList import *
from tkinter import *
import subprocess
import os

def create_pages(path, pages=10):
    diary = Doubly_LL()
    diary.add_begin(path+fr'\1.txt')
    # open(path+r'\1.txt', 'w')/
    for i in range(2,pages+1):
        diary.add_end(path+fr'\{i}.txt')
        # open(path+fr'\{i}.txt', 'w')
    return diary


page_number = int(input('Enter the page number: '))
path = r'C:\Users\Lenovo\Downloads\visual_stdio_programs\Python_Programs\Data-Structure-Project-2\pages'
diary = create_pages(path, 10)

p = fr'{path}\{page_number}.txt'
os.system(p)
while True:    
    next_page = input('Next Page(n), Perivous Page(p), Exit(e): ')
    if next_page == 'n':
        p = diary.one_step_forward(p)
        # p = fr'{path}\{page_number}.txt'
        os.system(p)
    elif next_page == 'p':
        p = diary.one_step_backward(p)
        os.system(p)       
    elif next_page == 'e':
        break
    else:
        print('chose valid option')
