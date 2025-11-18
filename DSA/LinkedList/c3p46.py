from LinkedList import *
l = Node(1)
for i in range (2, 10):
    addNode(l, Node(i))
printList(l)
def findingModular(l, k):#find modular from last
    first = second = l
    count = 1
    while (second.next):
        second = second.next
        count += 1
        if (count == k and second.next):
            first = second
            count = 0
    if (k == 1):
        return second.value
    return first.value
print(findingModular(l, 4))