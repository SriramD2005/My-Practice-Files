x=44
y=55
facx=[i for i in range(1,x+1) if x%i==0]
facy=[i for i in range(1,y+1) if y%i==0]
x=set(facx)
y=set(facy)
z=x & y
z=list(z)
print(max(z))