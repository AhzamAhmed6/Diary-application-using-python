from LinkedList import Doubly_LL



def test_one_step_forward():
    mynode = Doubly_LL()
    mynode.add_begin('ahzam')
    mynode.add_end('ahmed')
    a = mynode.head.data
    b = mynode.head.nref.data
    assert mynode.one_step_forward(x = str(a)) == str(b)