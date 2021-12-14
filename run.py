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
access = int(input('To read, press 1 \n To write, press 2 \n'))


