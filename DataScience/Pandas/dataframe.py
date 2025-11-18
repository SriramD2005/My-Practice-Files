# coding: utf-8
#data frames
from pandas import DataFrame
df=DataFrame([1,2,3],[4,5,6])
df
df.col()
df.columns()
df=DataFrame([1,2,3],index=['a','b','c'],columns=['c1','c2','c3'])
df=DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=['a','b','c'],columns=['c1','c2','c3'])
df
df.columns()
get_ipython().run_line_magic('pinfo', '%xmode')
get_ipython().run_line_magic('xmode', 'Context')
df.columns()
df.columns
df.index
#methods of creating dataframe

