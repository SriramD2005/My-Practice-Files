class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
def printList(list):
    curr = list
    while curr.next:
        print(curr.value, end = ' -> ')
        curr = curr.next
    print(curr.value)
def addNode(list, node):
    temp = list
    while True:
        if not temp.next:
            temp.next = node
            break
        temp = temp.next
#print(__name__)
l = Node(1)
for i in range (2, 10):
    addNode(l, Node(i))