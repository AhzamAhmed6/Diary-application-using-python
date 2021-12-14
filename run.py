from LinkedList import *
import sys


path = r'C:\Users\Lenovo\Downloads\visual stdio programs\Python_Programs\Data-Structure-Project-2\pages'
diary = LinkedList()
diary.add_begin(path+'\\1.txt')
diary.add_after(path+'\\2.txt', path+'\\1.txt')
diary.add_after(path+'\\3.txt', path+'\\2.txt')
diary.add_after(path+'\\4.txt', path+'\\3.txt')
diary.add_after(path+'\\5.txt', path+'\\4.txt')
diary.print_LL()


page_number = int(input('Enter the page number: '))
access = input('Read(r), Write(w) : ')

if access == 'r':
    file = open(path+f'\\{page_number}.txt', 'r')
    print(file.read())

    while True:        
            next_page = input('Do you wants to go to next page (y/n): ')
            if next_page == 'y':
                page_number = page_number+1
                file = open(diary.move_next_node(path+f'\\{page_number}.txt'))
                print(file.read())
            elif next_page == 'n':
                break