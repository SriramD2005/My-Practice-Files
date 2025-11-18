x=24
y=9
for i in reversed(range(1,min(x,y)+1)):
    if x%i==0 and y%i==0:
        print(i)
        break

