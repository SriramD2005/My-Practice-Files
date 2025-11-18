
#binary tree
class BinaryTree:
    def __init__(self,root):
        self.root=root
        self.right_child=None
        self.left_child=None
    def insert_left(self,left):
        if self.left_child==None:
            self.left_child=BinaryTree(left)
        else:
            temp=BinaryTree(left)
            temp.left_child=self.left_child
            self.left_child=temp
    def insert_right(self,right):
        if self.right_child==None:
            self.right_child=BinaryTree(right)
        else:
            temp=BinaryTree(right)
            temp.right_child=self.right_child
            self.right_child=temp
    def getroot(self):
        return self.root
    def getleft(self):
        return self.left_child
    def getright(self):
        return self.right_child
mytree=BinaryTree(1)
def pre_order(tree):
    if tree:
        print(tree.getroot())
        pre_order(tree.getleft())
        pre_order(tree.getright())
mytree.insert_left(2)

mytree.insert_left(3)

pre_order(mytree)





