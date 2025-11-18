class ArrayBinaryTree:
    def __init__(self, capacity):
        self.tree = [None] * capacity
        self.size = 0

    def insert(self, key):
        if self.size >= len(self.tree):
            raise Exception("Tree is full")
        self.tree[self.size] = key
        self.size += 1

    def search(self, key):
        for index, value in enumerate(self.tree):
            if value == key:
                return index
        return -1

    def inorder_traversal(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return []
        return (self.inorder_traversal(2 * index + 1) + 
                [self.tree[index]] + 
                self.inorder_traversal(2 * index + 2))

    def preorder_traversal(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return []
        return ([self.tree[index]] + 
                self.preorder_traversal(2 * index + 1) + 
                self.preorder_traversal(2 * index + 2))

    def postorder_traversal(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return []
        return (self.postorder_traversal(2 * index + 1) + 
                self.postorder_traversal(2 * index + 2) + 
                [self.tree[index]])


# Example usage
if __name__ == "__main__":
    capacity = 15  # Adjust capacity as needed
    bt = ArrayBinaryTree(capacity)
    bt.insert(10)
    bt.insert(5)
    bt.insert(20)
    bt.insert(3)
    bt.insert(7)
    bt.insert(15)
    bt.insert(30)

    print("Inorder traversal:", bt.inorder_traversal())
    print("Preorder traversal:", bt.preorder_traversal())
    print("Postorder traversal:", bt.postorder_traversal())

    # Search for a value
    value = 15
    index = bt.search(value)
    if index != -1:
        print(f"Node with value {value} found at index {index}.")
    else:
        print(f"Node with value {value} not found.")
