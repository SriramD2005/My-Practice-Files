#another list adt
import array
#create
list=array.array('i',[3,6,4,1,2,8])
#insert
list.insert(5,29)
#erase erasing 6
list.remove(6)
#search searching 4
print('4 found at',list.index(3)+1)
#traverse
for i in list:
    print(i,end=' ')