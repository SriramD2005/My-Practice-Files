class bstnode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
class bst:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=bstnode(data)
        else:
            self._insert(self.root,data)
    def _insert(self,node,data):
        if data<node.data:
            if node.left is None:
                node.left=bstnode(data)
            else:
                self._insert(node.left,data)
        if data>node.data:
            if node.right is None:
                node.right=bstnode(data)
            else:
                self._insert(node.right,data)
    def delete(self,data):
        if self.root==None:
            return 
        else:
            self.root=self._delete(self.root,data)
            print(self.root)
    def _delete(self,node,data):
        if node is None:
            return node
        if data<node.data:
            self._delete(node.left,data)
        elif data>node.data:
            self._delete(node.right,data)
        else:
            if node.left is None:
                node=node.right
            elif node.right is None:
                node=node.left
            else:
                temp=self._minchild(node.right)
                node.data=temp
                node.right=self._delete(node.right,temp)
        return node
    def _minchild(self,node):
        if node.left and node.right is None:
            return node.key
        else:
            node.left=self._minchild(node.left)
    def inorder(self):
        print(self.root)
        if self.root==None:
            return
        else:
            self._inorder(self.root)
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            print(node.data,end=' ')
            self._inorder(node.right)
bs=bst()
bs.insert(10)
bs.insert(5)
bs.insert(15)
bs.insert(3)
bs.insert(8)
bs.insert(1)
bs.delete(3)
bs.inorder()