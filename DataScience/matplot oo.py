#object oriented
import matplotlib.pyplot as mt
fig,(axes,axe2)=mt.subplots(1,2)
fig.set_facecolor(color='0.8')
axe2.plot([2,3,4,5],[1,7,3,0],color='red')
axes.bar([2,3,4,5],[1,7,3,0],color='red',label='bar')
axes.grid(color='0.8')
mt.legend()
mt.show()