from numpy import array, concatenate, hstack, vstack
x=array([1,2,3,4,5,6])
x=x.reshape((2,3))
y=array(([7,8,9],[0,9,8]))
print(concatenate([x,y])) #adds the rows, that is vertical concatenation
print("horizontal concatenation:\n",concatenate([x,y],axis=1))
#the concatenation can be used for arrays with same shape, to join arrays with different shape we go with vstack(adds rows) and hstack(adds columns)
a=x
b=array([99,99,99])
print("using vstack\n",vstack([a,b]))
#for hstack we may have more or less number of columns but we should have exactly same number of rows in both arrays to be joined
b=array([[99],[99]])
print("using hstack:\n",hstack([a,b]))

