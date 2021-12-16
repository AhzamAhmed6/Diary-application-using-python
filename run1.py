from LinkedList import *


def create_pages(pages, path):
    diary = LinkedList()
    diary.add_begin(path+fr'\1.txt')
    open(path+r'\1.txt', 'w')
    for i in range(2,pages+1):
        diary.add_after(path+fr'\{i}.txt', path+fr'\{i-1}.txt')
        open(path+fr'\{i}.txt', 'w')
    return diary
# diary.print_LL()

path = r'C:\Users\Lenovo\Downloads\visual stdio programs\Python_Programs\Data-Structure-Project-2\pages'
diary = create_pages(10, path)
def mydiary(access):
    page_number = int(input('Enter the page number: '))
    if page_number>5:
        print('Page limit reached')

    if access == 'r':
        p = f'{path}\\{page_number}.txt'
        file = open(p, 'r')
        print(file.read())
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