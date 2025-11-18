# coding: utf-8
from pandas import DataFrame,Series
df=DataFrame([1,2,3],[4,5,6])
df.values
df.index
df1=DataFrame([[1,2,3],[4,5,6],[7,8,9]])
df1.values
df1.index
#to get the transpose of the dataframe
df1.T
df1
df1[0]
#the loc is used to access the data according to our indexing
df2=DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["col1","col2","col3"],index=[1,2,3)
df2=DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["col1","col2","col3"],index=[1,2,3])
df2["col1"]
del In[16]
df2[:2]
df2[:2,:3]
any([0,0,0,0])
any([0,0,1,0])
raise Exception ("raised exception")
x=2
assert(x<2) "asserted error"
assert(x<2),"asserted error"
assert x==2,"no no"
#to get the values by normal 2-d array like indexing, we use iloc and to access them by our indexing we use loc attribute
df2.iloc[0:2,1:3]
with open("dataframe.py","a") as handle:
    handle.write(In[0:28])
