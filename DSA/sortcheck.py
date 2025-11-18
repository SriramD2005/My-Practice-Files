def checksort(list,n=1):
    if n>=len(list):
        print('sorted')
        return 
    if list[n]<list[n-1]:
        print('not sorted')
        return
    checksort(list,n+1)
tlist=eval(input("list:"))
checksort(tlist)   
        