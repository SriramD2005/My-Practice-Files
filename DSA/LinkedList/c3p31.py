#merging two sorted linked list
from LinkedList import *
l1 = Node(0)
for i in range(1, 15, 3):
    addNode(l1, Node(i))
#printList(l1)
l2 = Node(1)
for i in range(2, 20, 2):
    addNode(l2, Node(i))
#printList(l2)
def mergeList(l1, l2):
    p1 = l1
    p2 = l2
    l3 = Node(-1)
    p3 = l3
    while p1 and p2:
        if p1.value < p2.value:
            p3.next = p1
            p1 = p1.next
        elif p1.value > p2.value:
            p3.next = p2
            p2 = p2.next
        else:
            p3.next = p1
            p1 = p1.next
            p2 = p2.next
        p3 = p3.next
    if not p1:
        p3.next = p2
    elif not p2:
        p3.next = p1
    return l3.next
printList(mergeList(l1, l2))