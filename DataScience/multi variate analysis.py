import pandas as ps
import matplotlib.pyplot as plt
import seaborn as sea
x={"x":[1,3,3,4,5],"y":[5,6,7,8,20]}
df=ps.DataFrame(x)
sea.pairplot(df,vars=['x','y'],diag_kind='kde',kind='reg')
plt.show()
