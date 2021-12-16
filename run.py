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


def mydiary(access):
    page_number = int(input('Enter the page number: '))
    if page_number>5:
        print('Page limit reached')



    '''For read only option'''

    if access == 'r':
        p = f'{path}\\{page_number}.txt'
        file = open(p, 'r')
        print(file.read())
        while True:        
                next_page = input('Do you wants to go to next page (y/n): ')
                if next_page == 'y':
                    mydiary(access=access)
                    # print(file.read())
                elif next_page == 'n':
                    return
                else:
                    print('Please chose valid option')

        file.close()


    if access == 'w':
        p = f'{path}\\{page_number}.txt'
        file = open(p, 'w')
        text = input(f'Input your text for page no {page_number}: ')
        file.write(text)

        while True:        
                next_page = input('Do you wants to go to next page (y/n): ')
                if next_page == 'y':
                    p = diary.move_next_node(p)
                    file = open(p, 'r')
                    print(file.read())
                elif next_page == 'n':
                    break
                else:
                    print('Please chose valid option')

        file.close()

access = input('Read(r), Write(w), Append(a) : ')
mydiary(access=access)