x=int(input('x:'))
y=int(input('y:'))
breakpoint()
x=99
y=999
breakpoint()
for i in range(1,min(x,y)+1):
    if x%i==0 and y%i==0:
        gcd=i
print(gcd)