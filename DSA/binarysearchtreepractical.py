class bstnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self,root):
        self.root=bstnode(root)
    def insert(self,data):
        if self.root==None:
            self.root=bstnode(data)
        else:
            self._insert(self.root,data)
    def _insert(self,node,data):
        if data<node.data:
            if node.left==None:
                node.left=bstnode(data)
            else:
                self._insert(node.left,data)
        if data>node.data:
            if node.right==None:
                node.right=bstnode(data)
            else:
                self._insert(node.right,data)
    def inorder(self):
        if self.root==None:
            return
        else:
            self._inorder(self.root)
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            print(node.data)
            self._inorder(node.right)
    def delete(self,data):
        if self.root==None:
            return
        else:
            self.root=self._delete(self.root,data)
    def _delete(self,node,data):
        if node==None:
            return node
        if data<node.data:
            node.left=self._delete(node.left,data)
        elif data>node.data:
            node.right=self._delete(node.right,data)
        else:
            if node.left is None:
                node=node.right
            elif node.right is None:
                node=node.left
            else:
                t=self.minchild(node.right)
                node.data=t.data 
                node.right=self._delete(node.right,t.data)
        return node
    def minchild(self,node):
        if node:
            if node.left==None:

                return node
            else:
                node.left=self.minchild(node.left)

bs=bst(4)
bs.insert(5)
bs.insert(6)
bs.insert(8)
bs.insert(2)
bs.insert(9)
bs.inorder()
bs.delete(4)
            