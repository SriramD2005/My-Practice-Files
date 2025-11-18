#handle edge cases like inserting before the edge and at the end
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
def printList(list):
    curr = list
    while curr:
        print(curr.value)
        curr = curr.next
def addNode(list, node):
    while True:
        if not list.next:
            list.next = node
            break
        list = list.next
if __name__ == "main":
    value = int(input("integer to be inserted: "))
    curr = list
    while curr.next:
        if value < curr.next.value:
            curr.next = Node(value, curr.next)
            break
        curr = curr.next
    curr = list
    printList()