def ander(n:int,x:int)->int:
    xbin=bin(x).split('b')
    xbin=list(xbin[1])
    ybin=xbin
    result=[]
    count=0
    while (count<=n):
        filled=count
        for i in range(len(xbin)-1,-1,-1):
            if ybin[i]=='0':
                ybin[i]='1'
                result.append(ybin)
                count+=1
                break
        if filled==count:
            ybin=['1']+xbin
            result.append(ybin)
            count+=1
    retval=''
    for i in result[n-1]:
        retval+=i
    return int(retval,2)
ans=ander(3,4)
print(ans)