class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
        else:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                if node.left is None:
                    node.left = new_node
                    break
                else:
                    queue.append(node.left)
                if node.right is None:
                    node.right = new_node
                    break
                else:
                    queue.append(node.right)

    def inorder(self):
        return self._inorder(self.root, [])

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)
        return result

    def preorder(self):
        return self._preorder(self.root, [])

    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
        return result

    def postorder(self):
        return self._postorder(self.root, [])

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)
        return result

# Example usage
bt = BinaryTree()
keys = [10, 5, 20, 3, 7, 15, 25]
for key in keys:
    bt.insert(key)

print("In-order traversal:", bt.inorder())
print("Pre-order traversal:", bt.preorder())
print("Post-order traversal:", bt.postorder())

