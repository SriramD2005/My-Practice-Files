#here the append method does not creates a new list and return. Instead, it just modifying the list in place.
#So, changing of the value to the variable(pointer change of the label) depends on wether, the operation returns a new list or not
x=[1,2,3,4]
y=x
y=x.extend([99])
print(x)
print(y)