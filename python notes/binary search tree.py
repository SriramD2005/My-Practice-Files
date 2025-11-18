class binstreenode:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,val):
        if self.data==None:
            self.data=val
            self.left=binstreenode()
            self.right=binstreenode()
        else:
            if self.data>val:
                self.left.insert(val)
            else:
                self.right.insert(val)
    list=[]
    def display(self):
        if self.data==None:
            return
        self.left.display() 
        binstreenode.list.append(self.data)
        self.right.display()
    def __str__(self):
        self.display()
        return str(binstreenode.list)
y=binstreenode(5)
print(y)

        
        

