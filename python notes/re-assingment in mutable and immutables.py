#immutable
x=5
y=x
y+=1
print("x:",x,"y:",y)
# here y, which is a label, points  the memory location of x+1(6)
#so the immutables cannot be changed in place but by changing the ponter to the location where
#it points to the new assingned value
#MUTABLE
x=[1,2,3]
y=x
y[0]=99
print(x)
#As list is mutable(because it is just mapped and the map pointer are changed to
#point different location) it is changed in place and the change in y reflect in x

print("returns 2's complement of 12: ",~12)