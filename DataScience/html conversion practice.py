import pandas as ps
x=ps.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,0],'c':[11,22,33,44,55],'D':[66,77,88,99,11]})
xhtml=x.to_html()
with open("new.html","+w") as new:
    new.write(xhtml)
