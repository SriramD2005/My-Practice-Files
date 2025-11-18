#doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        current_index = 0
        while current_index < index - 1 and current.next:
            current = current.next
            current_index += 1

        if current_index != index - 1:
            print("Index out of range")
            return

        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current
    
            
      
    def delete_node(self, value):
        current = self.head

        # Traverse the list to find the node with the given value
        while current:
            if current.data == value:
                # If the node to be deleted is the head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    # Adjust pointers to bypass the current node
                    if current.prev:
                        current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                return  # Exit function after deletion
            current = current.next

        print("Node with value {} not found".format(value))

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
dll = DoublyLinkedList()
dll.insert_at_index(0, 1)  # Insert at index 0
dll.insert_at_index(1, 2)  # Insert at index 1
dll.insert_at_index(2, 3)  # Insert at index 1
dll.insert_at_index(3, 4)  # Insert at index 2
dll.delete_node(3)
dll.display()  # Output: 1 3 4 2
