class heap:
    def __init__(self):
        self.heap=[0]
        self.currentsize=0
    def insert(self,key):
        self.heap.append(key)
        self.currentsize+=1
        self.percup(self.currentsize)
    def percup(self,i):
        while i//2>0:
            if self.heap[i]<self.heap[i//2]:
                self.heap[i],self.heap[i//2]=self.heap[i//2],self.heap[i]
            i=i//2
    def delete(self,key):
        i=self.heap.index(key)
        
        self.heap[i]=self.heap[self.currentsize]
        self.heap.pop()
        self.currentsize-=1
        self.percdown(i)
    def 
        
h=heap()
h.insert(2)
h.insert(1)
print(h.heap)               