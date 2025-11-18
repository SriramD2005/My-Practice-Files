from LinkedList import *
l = Node(1)
for i in range (2, 65):
    addNode(l, Node(i))
def rootN(l):
    first = l
    second = l
    while (second):
        nextvalue = first.next.value
        if second.value == nextvalue ** 2:
            first = first.next
            second = second.next
        else:
            second = second.next
    return first.value
print(rootN(l))