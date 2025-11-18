def merge(left,right):
    if len(left)==0 or len(right)==0:
        return left or right
    result=[]
    i,j=0,0
    while (len(result)<len(right)+len(left)):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        if len(left)==i or len(right)==j:
            result.extend(left[i:] or right[j:])
            break
    return result
def mergesort(list):
    if len(list)<2:
        return list
    mid=len(list)//2
    
    left=mergesort(list[:mid])
    right=mergesort(list[mid:])
    return merge(left,right)
print(mergesort([4,2,1,7,4,5]))


