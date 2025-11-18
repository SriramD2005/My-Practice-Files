#list adt 3rd
import array
#creation
x=array.array('i',[10,20,30,40,50])
#find 30 element
print('found at',x.index(30)+1)
#delete 20
x.remove(20)
#display
print(x.tolist())