import numpy as np
import pandas as ps
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.savetxt("abc.txt",x)
ps.set_option('display.max_columns',500)
ps.set_option("display.max_rows",500)
y=ps.Series([1,3,5,7,9])
#print(y)
z=ps.DataFrame({'A:':5,'B:':ps.Series([1,2,34,5,6,78]),'C:':np.array([1,2,3,4,5,6])})
#print(z)
z=dict()
z['columnA']=12,13,6,8
z['columnB']=24,36,7,9
y=ps.DataFrame(z,index=range(2,6))
#print(y)
columns = list(range(22))
#internet=ps.read_csv('http://archive.ics.uci.edu/dataset/53/iris',names=columns)
#internet.head(10)
x=np.arange(2,10)
print(x)