def insertion(l):
    isort(l,len(l)-1)
    print(l)
def isort(l,k):
    if k>1:
        isort(l,k-1)
        insert(l,k-1)
def insert(l,k):
    current=l[k]
    while k>0 and l[k-1]>l[k]:
        l[k],l[k-1]=l[k-1],l[k]
        k-=1
insertion([8,1,6,4,3,9,5])