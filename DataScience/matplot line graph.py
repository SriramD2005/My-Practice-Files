import pandas as ps
import matplotlib.pyplot as mt 
import calendar
import random
xaxis=list(range(1,13))
yaxis=[round(random.uniform(100,200)) for i in xaxis]
figure,axis=mt.subplots()
print(axis)
plot=axis.bar(xaxis,yaxis)
mt.xticks(xaxis,calendar.month_name[1:13])
axis.set_title('my bar graph')
for bar in plot:
    height=bar.get_height()
    textheight=height*1.5
    axis.text(bar.get_x(),height,'%.2f'%textheight)
mt.show()