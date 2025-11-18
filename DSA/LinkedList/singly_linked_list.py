class Node:
    def __init__(self,data=None,next=None):
        self.next=next
        self.data=data
    def has_next(self):
        return self.next
class llist:
    def __init__(self):
        self.head=None
        self.length=0
    def MA(self,index):
        count=0
        current=self.head
        while count!=index and current:
            current=current.next
            count+=1
        return current
    def insert(self,data,index):
        if index==self.length and index!=0:
            last=self.MA(self.length-1)
            last.next=Node(data)
            self.length+=1
        elif index==0:
            if self.length>=1:
                newnode=Node(data,self.head)
                self.head=newnode
                self.length+=1
            else:
                self.head=Node(data)
                self.length+=1
        else:

            count=0
            current=self.MA(index-1)
            newnode=Node(data,current.next)
            current.next=newnode
    def __str__(self):
        current=self.head
        list=[]
        while current:
            list.append(current.data)
            current=current.next
        return str(list)
    def delete(self,index):
        if index==0:
            self.head=self.head.next
        elif index==self.length:
            last=self.MA(index-1)
            last.next=None
        else:
            prev=self.MA(index-1)
            prev.next=prev.next.next
        self.length-=1
mylist=llist()
mylist.insert(1,0)
mylist.insert(3,1)
mylist.insert(2,1)
print(mylist)
mylist.delete(2)
print(mylist.length)
print(mylist)
#help(map)