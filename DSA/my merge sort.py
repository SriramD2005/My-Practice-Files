result=[]
def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        mergesort(left)
        mergesort(right)
    
        i,j=0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while i<len(left):
            result.append(left[i])
            i+=1
        while j<len(right):
            result.append(right[j])
            j+=1
    
    
l=[6,3,6,3,2,1,7,8]
mergesort(l)
print(result)