#binary operation in dataframes with difference shapes
import pandas as pd
import numpy as np
a = np.random.randint(10,(3,4))
a = np.random.randint(1,10,(3,4))
a
df = pd.DataFrame(a)
a = np.random.randint(1,10,(3,4))
b = ones((3,1))
b = np.ones((3,1))
#by rules of broadcasting of numpy arrays, the dimension with 1 in the shape, is streched to the corresponding dimension of the other array
a - b
b = np.arange(3)
a - b
#this will throw an error because while brodcasting the leftmost dimension is replaced with 1(for 1-dimensional arrays with shapes like (3,)) now the shape of the array b will (1,3) and which in turn stretched to (3,3) which is a mismatch for array a of shape (3,4) this could be resolved as:
b = np.arange(3).reshape(3,1)
a-b
#this could also be done by subract method of dataframe object
df.subract(b,axis =1) #by default axis = 1 only
df.subtract(b,axis =1) #by default axis = 1 only
