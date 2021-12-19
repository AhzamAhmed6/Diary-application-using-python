class Node:
    '''This class is just for creating a Node with some data, thats why we set the refrence field to Null'''
    
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class Doubly_LL:
    '''This class is for performing the operations to the node which we create using class Node'''

    def __init__(self):
        self.head = None                # initially we take empty linked list


    def print_LL_forward(self):
        '''This methord is for traversing doubly Linked List in the forward direction'''

        if self.head is None:           # if the linked list is empty
            print('The linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data, end=('  -->  '))
                n = n.nref

    def print_LL_reverse(self):
        '''This methord is for traversing doubly Linked List in the backward direction'''
        print('\n\n\n')
        if self.head == None:           # if the linked list is empty
            print('The linked list is empty')
        else:
            n = self.head               # set the head node as n
            while n.nref is not None:   # first we reach at the last node
                n = n.nref     
            while n is not None:         # then we start reverse traversing
                print(n.data, end='  -->  ')
                n = n.pref


    def add_empty(self, data):
        '''Tis methord is for adding a new node in the empty Linked List'''

        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked List is not empty')


    def add_begin(self, data):
        '''This methord add new node at the begining of the doubly linked list'''
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node


    def add_end(self, data):
        '''This methord add a new node at the end of the doubly linked list'''

        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n


    def add_after(self, x, data):
        n = self.head
        if self.head is None:
            print('Linked list is empty')
        else:
            while n is not None:
                if x==n.data:
                    break
                n = n.nref
            if n is None:
                print('The given node is not present in the Linked List')
            new_node = Node(data)
            new_node.pref = n


    def one_step_forward(self, x):
        '''This step move the current pointer one step forward from the current node'''

        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.nref
        n = n.nref
        next_node = n
        return next_node.data


    def one_step_backward(self, x):
        '''This step move the current pointer one step backward from the current node'''

        n = self.head
        while n is not None:
            if x==n.nref.data:
                break
            n = n.nref
        previous_node = n
        return previous_node.data
        





         
if __name__ == '__main__':
    mynode = Doubly_LL()
    mynode.add_begin('5')
    mynode.add_begin('4')
    mynode.add_begin('3')
    mynode.add_begin('2')
    mynode.add_begin('1')
    print(mynode.one_step_backward('2'))
