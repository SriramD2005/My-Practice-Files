def quicksort(A,l,r):#A[l:r]
    if l>=r:
        return 
    yellow=l+1
    pivot=A[l]
    for green in range(l,r):
        if A[green]<pivot:
            A[green],A[yellow]=A[yellow],A[green]
            yellow+=1
    A[l],A[yellow-1]=A[yellow-1],A[l]
    quicksort(A,l,yellow-1)
    quicksort(A,yellow,r)
l=[3,1,4,2,6,8,7]
quicksort(l,0,len(l))
print(l)

