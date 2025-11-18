#binary search
l=[1,2,3,4,5]
def bs(l,left,right,se):
    
    if left>right:
        print('not in list')
        return "not in list"
    mid=(left+right)//2
    if l[mid]<se:
        
        return bs(l,mid+1,right,se)
        
    elif l[mid]>se:
        right=mid-1
        return bs(l,left,mid-1,se)
    else:
        return mid
print(bs(l,0,len(l)-1,4))