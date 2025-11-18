import matplotlib.pyplot as mt
import pandas as ps
x=ps.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
fig,axes=mt.subplots()
def plotter(d1,d2,lab,col):
    return axes.plot(d1,d2,**lab,**col)
plotter(list(range(50)),list(x.iloc[:50,2]),{'label':'petal height'},{'color':'red'})
plotter(list(range(50)),list(x.iloc[:50,0]),{'label':'sepal height'},{'color':'green'})
fig.set_label('setosa')
axes.legend()
axes.grid(visible='hi')
axes.set_xlabel('index',color='red')
mt.show()
