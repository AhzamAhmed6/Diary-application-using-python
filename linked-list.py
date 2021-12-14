class Node:
    '''This class is just for creating a Node, thats why we set the refrence field to Null'''
    
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    '''This class is for linked the nodes which we create using class Node'''

    def __init__(self):
        self.head = None  # we are creating an empty linked list

    def print_LL(self):
        '''This methord is for traversing Linked List'''

        if self.head == None:    # if the linked list is empty
            print('The linked list is empty')

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref



        # self.head is just store the refrence of first node 

