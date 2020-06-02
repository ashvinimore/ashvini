''''
Author : Ashvini More
Problem statement : Insert data in Doubly Circular Linked List
1. append = insert last
2. append_first = insert first
3. insert = insert at perticular position
'''
# Class for linked list structure
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
def append(val):
    global head,tail,length
    temp = Node(0)
    temp.val = val
    if head == None and tail == None:
       temp.prev=temp.next = val
       length = 1
       head=tail = temp
    elif length == 1:  #====special case for tail
        head.next = temp
        temp.prev = head
        tail = temp
        length = length + 1
    else:
        temp.next = head
        temp.prev = tail
        tail.next = temp
        tail = temp
        length = length + 1
def append_first(val):
    global head,tail,length
    if length:
        temp = Node(0)
        temp.val = val
        head.prev = temp
        temp.next = head
        temp.prev = tail
        head = temp
        length = length + 1
    else:
        append(val)
def insert(val,pos):
    global head, tail, length
    currnode = head
    temp = Node(0)
    temp.val = val
    if length and pos <= length-1:
        if pos == 0:
            append_first(val)
            return
        for i in range(0,pos-1):
            currnode = currnode.next
        temp.next = currnode.next
        currnode.next.prev = temp
        currnode.next = temp
        temp.prev = currnode
        length = length + 1

def traverse():
    global head,tail,length
    temp = head
    length1 = length
    while length1 :
        # while(length1 > 0):
            print(temp.val,end = " ")
            temp = temp.next
            length1 = length1 -1
    return
if __name__ == '__main__':
    global head
    # Start with the an empty list
    length = 0
    head = None
    tail = None
    # append(1)
    # append(2)
    # append(3)
    # append(4)
    # append(5)
    # append(7)
    val = [7, 12, 8, 12, 8, 13, 8, 13, 7, 13]
    a = [append(i) for i in val]
    append_first("first")
    insert('insert',3)
    traverse()
    # traverse()

