class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_node(self, value):
        if not self.head:
            print("Circular Linked List is empty")
            return

        if self.head.data == value:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return

        prev = None
        current = self.head
        while current.next != self.head:
            if current.data == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

        if current.data == value:
            prev.next = self.head

    def display(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(Back to head)")

# Example usage:
cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.insert_at_end(4)

cll.display()  # Output: 1 -> 2 -> 3 -> 4 -> (Back to head)

cll.delete_node(3)

cll.display()  # Output: 1 -> 2 -> 4 -> (Back to head)
