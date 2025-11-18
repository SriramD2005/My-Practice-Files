def mergesort(l):
    if len(l)<=1:
        return l
    mid=len(l)//2
    left=mergesort(l[0:mid])
    right=mergesort(l[mid:len(l)])
    return merge(left,right)
def merge(left,right):
    if not left or not right:
        return left or right
    i,j=0,0
    result=[]
    while i<len(left) and j<len(right):
        
        if left[i]<right[j]:
            result.append(left[i])
            
            i+=1
        else:
            result.append(right[j])
            j+=1
    print(result)
    result.extend(left[i:] or right[j:])
    return result
print(mergesort([3,4,1,7,2]))
