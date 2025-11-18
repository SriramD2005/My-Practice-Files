#slice in place replacement in list, only in list, not in immutables
x=[1,2,3,4,5,6,7,8]
y=x
y[0:4]=[9,9,9,9,9,9,9]
print(x)