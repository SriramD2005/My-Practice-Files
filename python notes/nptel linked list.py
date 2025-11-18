class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
    def append(self,val):
        if not self.data:
            self.data=val
        else:
            nn=Node(val)
            if not self.next:
                self.next=nn
            else:
                self.next.append(val)
    def insert(self,val):
        nn=Node(val)
        self.data,nn.data=nn.data,self.data
        nn.next=self.next
        self.next=nn
    def delete(self,val):
        if self.data==val and not self.next:
            self.data=None
        else:
            if self.data==val:
                self.data,self.next.data=self.next.data,self.data
                self.next=self.next.next
            else:
                self.next.delete(val)
                if self.next.data==None:
                    self.next=None

    #for printing the list print function calls str() str inturn calls __str__() of class
    def __str__(self):
        temp=self
        list=[]
        if not self.data:
            return []
        else:
            while temp!=None:
                list.append(temp.data)
                temp=temp.next
            return str(list)
myl=Node(1)
for i in range(2,12):
    myl.append(i)
myl.delete(11)
print(myl)

