#LIST MANUPULATION
#THE MAP FUCTION
lis=[2,3,4,5,6,7,8]
modifiedL=list(map(lambda x:x*3,lis))
print(modifiedL)
def square(x):
    return x**2
squarelist=list(map(square,lis))
print(squarelist)
#SHALLOW COPY IN LIST COMPREHENSION
list=[[0,0,0] for i in range(3)]#deep copy
print(list)
list[1][1]=7
print(list)
#shallow copy
zerolist=[0 for i in range(3)]
matrix=[zerolist for i in range(3)]
matrix[1][1]=7
print(matrix)
#so if you try to iterate a variable it just makes a shallow copy, so do all 
#operations in one short
