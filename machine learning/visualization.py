import matplotlib.pyplot as plt
import pandas as ps
data=ps.read_csv('C:/coding/machine learning/diabetes.csv')
df=ps.DataFrame(data)
print(df)
x=[df.iloc[x,0] for x in range(767) if df.iloc[x,8]==0]
y=[df.iloc[x,1] for x in range(767) if df.iloc[x,8]==0]
a=[df.iloc[x,0] for x in range(767) if df.iloc[x,8]==1]
b=[df.iloc[x,1] for x in range(767) if df.iloc[x,8]==1]
plt.scatter(x,y,color='red',marker='x')
plt.scatter(a,b)
plt.show()