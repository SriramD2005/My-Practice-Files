import pandas as ps
import seaborn as sea

x=ps.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,0],'c':[11,22,33,44,55],'D':[66,77,88,99,11]})
def bgcolor(val):
    if val%2:
        color='red'
    else:
        color='green'#for even 
    return f'background-color:{color}'
styledx=x.style.applymap(bgcolor)
colormap=sea.light_palette("yellow",as_cmap=True)
styledsee=x.background_gradient(colormap)
styledx=styledsee.to_html()
with open("red.html","+w") as red:
    red.write(styledx)

