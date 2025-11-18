#To display linked list from the end
from LinkedList import *
l = Node(1)
for i in range (2, 10):
    addNode(l, Node(i))
def displayFromEnd(curr):
    if not curr:  #what if the passed list is empty?
        return 
    if curr.next:
        displayFromEnd(curr.next)
    print(curr.value, end = ' ')
displayFromEnd(l)

