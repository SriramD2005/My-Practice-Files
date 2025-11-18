#SETS
#Accesing an element in a set (also called hashset) takes only O(1) time
#EXCLUSIVE OR
x={1,2,3,4}
y={1,2}
z={2,3}
print('excllusive or:',x^y^z)#returns inteegers occured odd number of times
#difference
x={1,2,3,4}
y={2,3}
print(y-x)
y={5,6}
#union
print('union:',x|y)
y=set((2,4,6))
#intersection
print(x&y)


