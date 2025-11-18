import matplotlib.pyplot as mt
fig,axes=mt.subplots()
def plotter(d1,d2,shape,color):
    axes.scatter(d1,d2,**shape,**color,label='d1',edgecolors='0')
axes.scatter([1,2,3,4,5],[1,2,3,4,5],color='yellow',label='d2',edgecolors=('green'),s=300)
fig.set_facecolor('0.8')
plotter([1,8,3,4],[1,2,7,4],{'marker':'v'},{'color':'red'})
axes.legend()
mt.show()