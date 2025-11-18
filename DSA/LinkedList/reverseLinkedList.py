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
curr = list
value = int(input("integer to be inserted: "))
while curr.next:
    if value < curr.next.value:
        curr.next = Node(value, curr.next)
        break
    curr = curr.next
curr = list
while curr:
    print(curr.value)
    curr = curr.next