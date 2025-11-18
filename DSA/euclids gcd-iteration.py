m=24
n=16
while m%n!=0:
    
    if m<n:
        m,n=n,m
    dif=m-n
    m=max(dif,n)
    n=min(dif,n)
print(n)