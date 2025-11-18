from LinkedList import *
l = Node(1)
for i in range (2, 10):
    addNode(l, Node(i))
for i in range(2, 20, 2):
    addNode(l, Node(i))
printList(l)
printList(l)
def seperatingParityValueSwap(l):
    f = l
    s = l.next
    while s:
        if not s.value % 2:
            f.value, s.value = s.value, f.value
            f = f.next
            s = s.next
        else:
            s = s.next
    return l
printList(seperatingParityValueSwap(l))