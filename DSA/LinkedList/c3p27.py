#finding the middle of the linked list
from LinkedList import *
l = Node(1)
for i in range (2, 10):
    addNode(l, Node(i))
def findMiddle(l):
    fastptr = l 
    slowptr = l
    while fastptr:
        fastptr = fastptr.next
        if not fastptr:
            return slowptr.value
        fastptr = fastptr.next
        slowptr = slowptr.next
print(findMiddle(l))
    