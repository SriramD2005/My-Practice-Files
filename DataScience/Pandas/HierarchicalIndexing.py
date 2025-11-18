#Hierarchical indexing
import pandas as pd
#bad way:(in series object)
index = [('California', 2000), ('California', 2010),
 ('New York', 2000), ('New York', 2010),
 ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
 18976457, 19378102,
 20851820, 25145561]
pop = pd.Series(populations, index = index)
pop
#to select the population in 2010 from all countries:
pop.loc[i for i in pop.index if i[1] == 2010]
pop.loc[[i for i in pop.index if i[1] == 2010]]
#better way:
#there is a pandas object called MultiIndex, which is used for efficient data management
mIndex = pd.MultiIndex.from_tuples(index)
mIndex
pop.index = mIndex
pop
pop.index
pop.index.levels
pop.index.labels
#stack and unstack method:
#these methods are used to convert a multiIndexed series to DataFrame and vice-versa
pop2 = pop
pop2.unstack()
pop2
pop2 = pop.unstack()
pop2
pop2.stack()
import pandas as pd
import numpy as np
# Methods of MUlti Index Creation
# from tuples
popData = np.random.randint(2,1000,(6,1))
popData
index = [('California', 2000), ('California', 2010),
 ('New York', 2000), ('New York', 2010),
 ('Texas', 2000), ('Texas', 2010)]
mIndex = pd.MultiIndex.from_tuples(index)
mIndex
mIndex.labels
mIndex.levels
# from nDarrays
index = [['California', 'California', 'New York', 'New York', 'Texas', 'Texas'], [2000, 2010, 2000, 2010, 2000, 2010]]
mIndex_from_arrays = pd.MultiIndex.from_arrays(index)
mIndex_from_arrays
# from cartesian product
mIndex_from_CProduct = pd.MultiIndex.from_product([['California','New York', 'Texas'], [2000, 2010]])
mIndex_from_CProduct
# to name the levels of the MultiIndex
popDf = pd.DataFrame(popData, index = mIndex)
popDf
# lets name the levels of the index
popDf
popDf.index.names = ['City', 'Year']
popDf
popDf.index.levels
# from constructor itself
mIndex_constructor = pd.MultiIndex(levels = [['California', 'New York', 'Texas'], ['2000', '2010']], labels = [[0,0,1,1,2,2],[0,1,0,1]])
mIndex_constructor = pd.MultiIndex(levels = [['California', 'New York', 'Texas'], ['2000', '2010']], codes = [[0,0,1,1,2,2],[0,1,0,1,0,1]])
mIndex_constructor
mIndex_constructor.codes

import numpy as np
import pandas as pd
# in pandas rows and columns both are treated same. So columns can also have Hierarchical Index.
healthData = np.round(np.random.randn(4,6),1)
df_hD = pd.DataFrame(healthData)
df_hD
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']])
index.names = ['Year', 'visits']
columns.names = ['subject', 'type']
df_hD.index = index
df_hD
df_hD.columns = columns
df_hD
df_hD['Bob']
df_hD.iloc[:, :3]
df_hD.index = index
df_hD.columns = columns
df_hD.iloc[:, :3]
df_hD.loc[(2013,:)]
df_hD.loc[:, ('Bob','HR')]
df_hD.columns
df_hD.loc[:, 'Bob']
df_hD.index.levels
df_hD.columns.levels
