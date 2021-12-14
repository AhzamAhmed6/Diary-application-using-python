

class Node:
    '''This class is just for creating a Node with some data, thats why we set the refrence field to Null'''
    
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    '''This class is for performing the operations to the node which we create using class Node'''

    def __init__(self):
        self.head = None           # we are creating an empty linked list (remember we are not creating a node, we are creating linked list, for creating node we already have method above)

    def print_LL(self):
        '''This methord is for traversing Linked List'''

        if self.head == None:      # if the linked list is empty
            print('The linked list is empty')

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)     # we create new node with data=data  and  ref=Null
        new_node.ref = self.head  # we set the refrence of new node to the head
        self.head = new_node      # set the head to the new node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # if linked list is empty, then we set newely created node as head
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref         # to reach to the last node
            n.ref = new_node      # set the refrence of last node to the new node

    def add_after(self, data, x):
        n = self.head
        while n is not None:      # first we find the node after which we wants to add the new_node
            if x==n.data:         # if we found the new node then we set the node name as n and break the loop
                break    
            n = n.ref             # else we are constantly updating the current node until we reach the required node
        if n is None:             # if n is still empty after traversing the whole linked list, it's mean the node is not present
            print('The linked list is empty')
        else:
            new_node = Node(data) # if we found the required node, only then we create new node
            new_node.ref = n.ref  # set the refrence of new node to the next node (the addres of next node is initially stored in the n.ref)
            n.ref = new_node      # set the refrence of perivous node to the new_node

    def add_before(self, data, x):
        if self.head is None:
            print('The linked list is empty')
            return
        if self.head.data==x:
            new_node = Node(data)     # we create new node with data=data  and  ref=Null
            new_node.ref = self.head  # we set the refrence of new node to the head
            self.head = new_node 
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n = n.ref
        if n.ref==None:
            print('The targeted node not found')
        else:
            new_node = Node(data) # if we found the required node, only then we create new node
            new_node.ref = n.ref  # set the refrence of new node to the next node (the addres of next node is initially stored in the n.ref)
            n.ref = new_node

    def move_next_node(self, x):
        n = self.head
        while n is not None:      # first we find the node after which we wants to add the new_node
            if x==n.data:         # if we found the new node then we set the node name as n and break the loop
                break    
            n = n.ref 
        next_node = n.ref # if we found the required node, only then we create new node
        return next_node.data

            
                

if __name__ == '__main__':
    ll = LinkedList()
    ll.add_begin('this is first node')
    ll.add_end('this is the end node')
    ll.add_before('this is second last node', 'this is the end node')
    ll.add_after('this is second node', 'this is first node')
    ll.print_LL()