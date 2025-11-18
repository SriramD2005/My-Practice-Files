from LinkedList import *
l = Node(0)
for i in range(1, 25):
    addNode(l, Node(i))
curr = l
while curr.next:
    curr = curr.next
curr.next = l
start = l
curr = l.nextn
count = 1
while curr.value != start.value:
    