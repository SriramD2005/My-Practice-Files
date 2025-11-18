#checking whether the length of the list even or odd
from LinkedList import *
l = Node(1)
for i in range (2, 10):
    addNode(l, Node(i))
#Method we think - Traversing the list and counting the length then using count % 2
#Complexity = O(n)
#More Efficient Method - using the Fast Pointer, traverse the list with step 2. increment it by to nodes if the 
#at the end if the pointer is in the last node then it is even else if it is in the Node it is odd
#Complexity = O(n/2)
def parityOfList(l):
    Fastptr = l
    while Fastptr:
        Fastptr = Fastptr.next
        if not Fastptr:
            return "odd"
        Fastptr = Fastptr.next
    return "even"
print(parityOfList(l))
printList(l)