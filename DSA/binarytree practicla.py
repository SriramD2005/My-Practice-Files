class binarytree:
    def __init__(self,root):
        self.root=root
        self.right=None
        self.left=None
    def insertleft(self,left):
        if self.left==None:
            self.left=binarytree(left)
        else:
            temp=binarytree(left)
            temp.left=self.left
            self.left=temp
    def root(self):
        return self.root
tree=binarytree(2)
def preorder(tree):
    
    if tree:
        print(tree.root())
        preorder(tree.left)
        preorder(tree.right)

tree.insertleft(3)
tree.insertleft(5)
preorder(2)