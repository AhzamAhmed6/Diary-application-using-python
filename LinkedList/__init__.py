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
            pn=0
            n = self.head
            while n is not None:
                print(n.data, end=('  -->  '))
                n = n.nref
                pn+=1
            print()
        return pn

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


    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nref
        if n is None:
            print("Given Node is not presnt in Linked List!")
        elif n.nref is None:
            new_node = Node(data)
            n.nref = new_node
            new_node.pref = n
        else:
            new_node = Node(data)
            n.nref.pref = new_node
            new_node.nref = n.nref
            n.nref = new_node
            new_node.pref = n
        





         
if __name__ == '__main__':
    mynode = Doubly_LL()
    mynode.add_begin('5')
    mynode.print_LL_forward()
    mynode.add_begin('4')
    mynode.print_LL_forward()
    mynode.add_begin('3')
    mynode.print_LL_forward()
    mynode.add_begin('2')
    mynode.print_LL_forward()
    mynode.add_begin('1')
    mynode.print_LL_forward()
    mynode.add_end('6')
    mynode.print_LL_forward()
    mynode.add_end('7')
    mynode.print_LL_forward()
    print(mynode.one_step_backward('2'))
    print(mynode.one_step_forward('4'))