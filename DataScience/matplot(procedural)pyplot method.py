#procedural(pyplot method)
import matplotlib.pyplot as mt
import numpy as np
mt.plot([1,2,3,4],[1,2,3,4],color='red',linestyle='-.',label='m=1')
mt.legend()
x=np.linspace(10,2,100)
fig=mt.figure(figsize=(5,5))
fig.set_label("empty")
mt.show()