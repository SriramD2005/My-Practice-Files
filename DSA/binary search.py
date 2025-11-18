list=[1,2,3,4,5,6,7,8]
x=int(input('x:'))
found=False
left=0
right=len(list)-1
while not found and left<=right:
    mid=(left+right)//2
    if list[mid]<x:
        left=mid-1
    elif list[mid]>x:
        right=mid+1
    else:
        print('found',x,'at',mid)
        found=True
    
if found==False:
    print('not in list')
