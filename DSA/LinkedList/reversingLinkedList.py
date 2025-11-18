class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
list = Node(1)
curr = list
for i in range(2, 11, 2):
    new = Node(i)
    curr.next = new
    curr = new
def reverseList(list):
    prev = None
    curr = list
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev
list = reverseList(list)
curr = list
while curr:
    print(curr.value)
    curr = curr.next