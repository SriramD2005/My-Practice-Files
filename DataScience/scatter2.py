import matplotlib.pyplot as mt
import pandas as ps
iris=ps.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
fig,axes=mt.subplots()
clist=iris['species'].map({'setosa':'red','virulosa':'green','virginica':'blue'})
axes.scatter(x=iris['sepal_length'],y=iris['petal_length'],c=clist)
mt.show()